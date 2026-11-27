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
