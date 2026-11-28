import pandas as pd

RAW_ORDERS_CSV = """\
order_id,order_date,customer,region,product,quantity,unit_price
1001,2024-01-05,Alice,North,Widget,2,10.00
1002,2024-01-05,Bob,South,Gadget,1,25.00
1002,2024-01-05,Bob,South,Gadget,1,25.00
1003,2024-01-20,Carol,North,Gadget,,25.00
1004,2024-02-03,Alice,North,Widget,5,10.00
1005,2024-02-14,Dave,,Widget,3,10.00
1006,2024-02-28,Bob,South,Gizmo,4,7.50
"""

PRODUCT_CATALOG_JSON = """[
    {
        "product_id": "P100",
        "product": "Keyboard",
        "opening_stock": 20,
        "reorder_level": 8
    },
    {
        "product_id": "P200",
        "product": "Mouse",
        "opening_stock": 12,
        "reorder_level": 5
    },
    {
        "product_id": "P300",
        "product": "Monitor",
        "opening_stock": 6,
        "reorder_level": 4
    },
    {
        "product_id": "P400",
        "product": "Dock",
        "opening_stock": 3,
        "reorder_level": 3
    }
]"""

STOCK_MOVEMENTS_CSV = """transaction_id,product_id,quantity_change
T001,P100,-5
T002,P100,10
T002,P100,10
T003,P200,-8
T004,P200,-2
T005,P300,-1
T006,P300,2
T007,P999,4
T008,P400,
"""

# Black-box system test for an end-to-end sales-reporting workflow.
def test_sales_csv_to_monthly_region_report_end_to_end(tmp_path):
    raw_path = tmp_path / "orders.csv"
    raw_path.write_text(RAW_ORDERS_CSV, encoding="utf-8")
    report_path = tmp_path / "revenue_report.csv"

    # 1. Ingest
    orders = pd.read_csv(raw_path, parse_dates=["order_date"])

    assert orders.shape == (7, 7)
    assert pd.api.types.is_datetime64_any_dtype(orders["order_date"])

    # 2. Clean: the duplicated order 1002 is removed, order 1003 has no
    # quantity and is dropped, and order 1005 has no region.
    orders = orders.drop_duplicates()
    orders = orders.dropna(subset=["quantity"])
    orders["region"] = orders["region"].fillna("Unknown")
    orders["quantity"] = orders["quantity"].astype("int64")

    assert orders["order_id"].tolist() == [1001, 1002, 1004, 1005, 1006]
    assert orders["region"].tolist() == ["North", "South", "North", "Unknown", "South"]
    assert not orders.isna().any().any()

    # 3. Enrich
    orders["revenue"] = orders["quantity"] * orders["unit_price"]
    orders["month"] = orders["order_date"].dt.strftime("%Y-%m")

    assert orders["revenue"].tolist() == [20.0, 25.0, 50.0, 30.0, 30.0]

    # 4. Report
    report = orders.pivot_table(
        index="region",
        columns="month",
        values="revenue",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="Total",
    )

    expected_report = pd.DataFrame(
        {
            "2024-01": [20.0, 25.0, 0.0, 45.0],
            "2024-02": [50.0, 30.0, 30.0, 110.0],
            "Total": [70.0, 55.0, 30.0, 155.0],
        },
        index=pd.Index(["North", "South", "Unknown", "Total"], name="region"),
    ).rename_axis(columns="month")
    pd.testing.assert_frame_equal(report, expected_report)

    top_customers = (
        orders.groupby("customer")["revenue"].sum().sort_values(ascending=False)
    )
    assert top_customers.to_dict() == {"Alice": 70.0, "Bob": 55.0, "Dave": 30.0}
    assert top_customers.index[0] == "Alice"

    # 5. Export and read back
    report.to_csv(report_path)

    assert report_path.exists()
    restored = pd.read_csv(report_path, index_col="region").rename_axis(
        columns="month"
    )
    pd.testing.assert_frame_equal(restored, report)


# Suite 2: system test for an end-to-end inventory reconciliation workflow.
def test_inventory_sources_to_reorder_report_end_to_end(tmp_path):
    catalog_path = tmp_path / "product_catalog.json"
    movements_path = tmp_path / "stock_movements.csv"
    report_path = tmp_path / "inventory_report.json"

    catalog_path.write_text(PRODUCT_CATALOG_JSON, encoding="utf-8")
    movements_path.write_text(STOCK_MOVEMENTS_CSV, encoding="utf-8")

    # 1. Ingest: Load product catalog and stock movement data.
    products = pd.read_json(catalog_path, orient="records")
    movements = pd.read_csv(movements_path)

    assert products.shape == (4, 4)
    assert movements.shape == (9, 3)
    assert products["product_id"].is_unique

    # 2. Clean: Remove duplicated transactions and discard movements
    # with missing quantities.
    movements = movements.drop_duplicates(subset=["transaction_id"])
    movements = movements.dropna(subset=["quantity_change"])
    movements["quantity_change"] = movements["quantity_change"].astype("int64")

    assert movements.shape == (7, 3)
    assert movements["transaction_id"].tolist() == [
        "T001", "T002", "T003", "T004", "T005", "T006", "T007"
    ]
    assert movements["quantity_change"].tolist() == [-5, 10, -8, -2, -1, 2, 4]

    # 3. Aggregate: Calculate the net stock movement for each product.
    net_changes = (
        movements.groupby("product_id", as_index=False)["quantity_change"]
        .sum()
        .rename(columns={"quantity_change": "net_change"})
    )

    expected_changes = {
        "P100": 5,
        "P200": -10,
        "P300": 1,
        "P999": 4,
    }
    assert net_changes.set_index("product_id")["net_change"].to_dict() == expected_changes

    # 4. Reconcile: Merge the aggregated movements with the product
    # catalog. Products without valid movements retain their opening stock.
    inventory = products.merge(
        net_changes,
        on="product_id",
        how="left",
        validate="one_to_one",
    )

    inventory["net_change"] = inventory["net_change"].fillna(0).astype("int64")
    inventory["closing_stock"] = (
        inventory["opening_stock"] + inventory["net_change"]
    )
    inventory["needs_reorder"] = (
        inventory["closing_stock"] <= inventory["reorder_level"]
    )

    assert inventory["product_id"].tolist() == ["P100", "P200", "P300", "P400"]
    assert inventory["net_change"].tolist() == [5, -10, 1, 0]
    assert inventory["closing_stock"].tolist() == [25, 2, 7, 3]
    assert inventory["needs_reorder"].tolist() == [False, True, False, True]

    # 5. Report: Generate a sorted inventory report containing the
    # reconciled stock levels and reorder recommendations.
    report = (
        inventory[
            [
                "product_id",
                "product",
                "opening_stock",
                "net_change",
                "closing_stock",
                "reorder_level",
                "needs_reorder",
            ]
        ]
        .sort_values("product_id")
        .reset_index(drop=True)
    )

    expected_report = pd.DataFrame(
        {
            "product_id": ["P100", "P200", "P300", "P400"],
            "product": ["Keyboard", "Mouse", "Monitor", "Dock"],
            "opening_stock": [20, 12, 6, 3],
            "net_change": [5, -10, 1, 0],
            "closing_stock": [25, 2, 7, 3],
            "reorder_level": [8, 5, 4, 3],
            "needs_reorder": [False, True, False, True],
        }
    )

    pd.testing.assert_frame_equal(report, expected_report)

    reorder_products = report.loc[
        report["needs_reorder"], "product"
    ].tolist()

    assert reorder_products == ["Mouse", "Dock"]

    # 6. Export and read back: Save the report as JSON and verify
    # that the restored data matches the original report.
    report.to_json(report_path, orient="records", indent=2)

    assert report_path.exists()

    restored = pd.read_json(report_path, orient="records")
    pd.testing.assert_frame_equal(restored, report)
