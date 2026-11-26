"""
Integration tests for a small sales-report pipeline.

Each test passes data across several pandas modules without stubbing any of
them, so the tests check that the modules agree on the data they exchange:

- ``pandas.io.parsers`` (``read_csv``) and ``pandas.io.json`` (``read_json``)
  produce the input frames;
- ``pandas.core.tools.datetimes`` converts parsed date strings;
- ``pandas.core.reshape.merge`` joins the inputs;
- ``pandas.core.groupby`` and ``pandas.core.resample`` aggregate the result;
- ``pandas.io.json._table_schema`` writes the output and reads it back.
"""

from io import StringIO

import numpy as np
import pytest

from pandas.errors import MergeError

import pandas as pd
import pandas._testing as tm

SALES_CSV = """\
date,store_id,units,price
2024-01-01,1,3,2.50
2024-01-01,2,1,10.00
2024-01-02,1,2,2.50
2024-01-04,2,4,10.00
"""

STORES_JSON = (
    '[{"store_id": 1, "region": "North"}, {"store_id": 2, "region": "South"}]'
)


@pytest.fixture
def sales():
    return pd.read_csv(StringIO(SALES_CSV), parse_dates=["date"])


@pytest.fixture
def stores():
    return pd.read_json(StringIO(STORES_JSON), orient="records")


# CSV and JSON inputs are merged, aggregated by region, and the
# report survives a round trip through the JSON table schema.
def test_csv_json_merge_groupby_table_round_trip(sales, stores):
    merged = sales.merge(stores, on="store_id", how="left", validate="many_to_one")
    merged["revenue"] = merged["units"] * merged["price"]

    report = merged.groupby("region").agg(
        units=("units", "sum"), revenue=("revenue", "sum")
    )

    expected = pd.DataFrame(
        {"units": [5, 5], "revenue": [12.5, 50.0]},
        index=pd.Index(["North", "South"], name="region"),
    )
    tm.assert_frame_equal(report, expected)

    serialized = report.to_json(orient="table")
    restored = pd.read_json(StringIO(serialized), orient="table")
    tm.assert_frame_equal(restored, report)


# Dates parsed by read_csv drive a daily resample, and the day with
# no sales (2024-01-03) is filled in by the resampler.
def test_csv_date_parsing_feeds_daily_resample(sales):
    assert sales["date"].dtype.kind == "M"

    daily = sales.set_index("date").resample("D")["units"].sum()

    expected = pd.Series(
        [4, 2, 0, 4],
        index=pd.DatetimeIndex(
            ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"],
            name="date",
            freq="D",
        ),
        name="units",
        dtype=np.int64,
    )
    tm.assert_series_equal(daily, expected)


# a duplicated key in the JSON lookup table makes the merge violate
# its many_to_one contract, so merge must refuse rather than duplicate rows.
def test_merge_rejects_duplicate_lookup_keys(sales):
    duplicated = pd.read_json(
        StringIO(
            '[{"store_id": 1, "region": "North"},'
            ' {"store_id": 1, "region": "East"}]'
        ),
        orient="records",
    )

    with pytest.raises(MergeError, match="not a many-to-one merge"):
        sales.merge(duplicated, on="store_id", validate="many_to_one")


# An empty field cannot be stored in the integer dtype requested from
# the parser, so read_csv raises instead of silently producing floats.
def test_read_csv_rejects_missing_value_in_integer_column():
    data = "date,store_id,units\n2024-01-01,1,\n"

    with pytest.raises(ValueError, match="Integer column has NA values"):
        pd.read_csv(StringIO(data), dtype={"units": "int64"})
