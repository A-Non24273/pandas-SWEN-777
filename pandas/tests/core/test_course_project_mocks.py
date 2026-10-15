import operator
from io import StringIO
from types import SimpleNamespace

import numpy as np
import pytest

import pandas as pd
import pandas._testing as tm
import pandas.core.computation.expressions as expressions
import pandas.core.frame as frame_module
import pandas.io.json._json as json_module
import pandas.io.parquet as parquet_module


# Verify to_markdown supplies its defaults and the actual frame to its formatter.
def test_to_markdown_formats_frame_with_stubbed_tabulate(monkeypatch):
    calls = []

    def tabulate(data, **kwargs):
        calls.append((data, kwargs))
        return f"{data.iloc[0, 0]}|{kwargs['tablefmt']}|{kwargs['showindex']}"

    monkeypatch.setattr(
        frame_module,
        "import_optional_dependency",
        lambda name: SimpleNamespace(tabulate=tabulate),
    )
    frame = pd.DataFrame({"value": [1]})

    result = frame.to_markdown(index=False)

    assert result == "1|pipe|False"
    assert calls == [
        (
            frame,
            {"headers": "keys", "tablefmt": "pipe", "showindex": False},
        )
    ]


# Verify to_markdown writes formatter output through pandas' handle API.
def test_to_markdown_writes_to_stubbed_handle(monkeypatch):
    output = StringIO()
    get_handle_calls = []

    def tabulate(data, **kwargs):
        return f"{data.iloc[0, 0]} in {kwargs['tablefmt']}"

    def get_handle(path, mode, storage_options):
        get_handle_calls.append((path, mode, storage_options))

        class StubHandle:
            def __enter__(self):
                return SimpleNamespace(handle=output)

            def __exit__(self, *args):
                return None

        return StubHandle()

    monkeypatch.setattr(
        frame_module,
        "import_optional_dependency",
        lambda name: SimpleNamespace(tabulate=tabulate),
    )
    monkeypatch.setattr(frame_module, "get_handle", get_handle)
    frame = pd.DataFrame({"value": [7]})

    result = frame.to_markdown(
        "table.md", storage_options={"token": "test"}, tablefmt="grid"
    )

    assert result is None
    assert output.getvalue() == "7 in grid"
    assert get_handle_calls == [("table.md", "wt", {"token": "test"})]


# Verify pandas builds the NumExpr expression and returns the backend's computed result.
def test_expression_evaluates_with_stubbed_numexpr(monkeypatch):
    calls = []

    def evaluate(expression, *, local_dict, casting):
        calls.append((expression, local_dict, casting))
        return local_dict["left_value"] + local_dict["right_value"]

    monkeypatch.setattr(expressions, "_can_use_numexpr", lambda *args: True)
    monkeypatch.setattr(expressions, "_evaluate", expressions._evaluate_numexpr)
    monkeypatch.setattr(
        expressions, "ne", SimpleNamespace(evaluate=evaluate), raising=False
    )
    left = np.array([1, 2])
    right = np.array([3, 4])

    result = expressions.evaluate(operator.add, left, right)

    tm.assert_numpy_array_equal(result, np.array([4, 6]))
    assert calls == [
        (
            "left_value + right_value",
            {"left_value": left, "right_value": right},
            "safe",
        )
    ]


# Verify to_json prepares split data without the index before encoding.
def test_to_json_uses_pandas_split_payload_with_stubbed_encoder(monkeypatch):
    calls = []

    def dumps(obj, **kwargs):
        calls.append((obj, kwargs))
        return "encoded split data"

    monkeypatch.setattr(json_module, "ujson_dumps", dumps)
    frame = pd.DataFrame({"value": [5]}, index=["row"])

    result = frame.to_json(orient="split", index=False, force_ascii=False, indent=2)

    assert result == "encoded split data"
    assert calls == [
        (
            {"columns": ["value"], "data": [[5]]},
            {
                "orient": "split",
                "double_precision": 10,
                "ensure_ascii": False,
                "date_unit": "ms",
                "iso_dates": False,
                "default_handler": None,
                "indent": 2,
            },
        )
    ]


# Verify pandas normalizes partition columns and returns the engine-written bytes.
def test_to_parquet_normalizes_partition_columns_with_stubbed_engine(monkeypatch):
    calls = []
    frame = pd.DataFrame({"group": ["a"], "value": [1]})

    def write(df, path, compression, **kwargs):
        calls.append((df, compression, kwargs))
        path.write(b"parquet bytes")

    monkeypatch.setattr(
        parquet_module, "get_engine", lambda engine: SimpleNamespace(write=write)
    )

    result = frame.to_parquet(engine="pyarrow", partition_cols="group")

    assert result == b"parquet bytes"
    assert calls == [
        (
            frame,
            "snappy",
            {
                "index": None,
                "partition_cols": ["group"],
                "storage_options": None,
                "filesystem": None,
            },
        )
    ]
