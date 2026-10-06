import operator
from unittest.mock import MagicMock, Mock

import numpy as np

import pandas as pd
import pandas.core.computation.expressions as expressions
import pandas.core.frame as frame_module
import pandas.io.json as json_module
import pandas.io.parquet as parquet_module


def test_to_markdown_uses_stubbed_formatter(monkeypatch):
    tabulate = Mock(return_value="| value |\n| 1 |")
    monkeypatch.setattr(
        frame_module,
        "import_optional_dependency",
        lambda name: Mock(tabulate=tabulate),
    )
    frame = pd.DataFrame({"value": [1]})

    result = frame.to_markdown(index=False)

    assert result == "| value |\n| 1 |"
    tabulate.assert_called_once_with(
        frame, headers="keys", tablefmt="pipe", showindex=False
    )


def test_to_markdown_writes_through_stubbed_handle(monkeypatch):
    tabulate = Mock(return_value="formatted table")
    monkeypatch.setattr(
        frame_module,
        "import_optional_dependency",
        lambda name: Mock(tabulate=tabulate),
    )
    output = Mock()
    handles = MagicMock()
    handles.__enter__.return_value.handle = output
    get_handle = Mock(return_value=handles)
    monkeypatch.setattr(frame_module, "get_handle", get_handle)
    frame = pd.DataFrame({"value": [1]})

    result = frame.to_markdown("table.md", storage_options={"token": "test"})

    assert result is None
    get_handle.assert_called_once_with(
        "table.md", "wt", storage_options={"token": "test"}
    )
    output.write.assert_called_once_with("formatted table")


def test_expression_dispatches_to_stubbed_numexpr_backend(monkeypatch):
    left = np.array([1, 2])
    right = np.array([3, 4])
    expected = np.array([4, 6])
    evaluate = Mock(return_value=expected)
    monkeypatch.setattr(expressions, "_evaluate", expressions._evaluate_numexpr)
    monkeypatch.setattr(expressions, "_can_use_numexpr", lambda *args: True)
    monkeypatch.setattr(expressions, "ne", Mock(evaluate=evaluate), raising=False)

    result = expressions.evaluate(operator.add, left, right)

    assert result is expected
    evaluate.assert_called_once()
    expression, kwargs = evaluate.call_args.args[0], evaluate.call_args.kwargs
    assert expression == "left_value + right_value"
    assert kwargs["local_dict"]["left_value"] is left
    assert kwargs["local_dict"]["right_value"] is right
    assert kwargs["casting"] == "safe"


def test_to_json_delegates_to_stubbed_json_writer(monkeypatch):
    writer = Mock(return_value='{"value":{"0":1}}')
    monkeypatch.setattr(json_module, "to_json", writer)
    frame = pd.DataFrame({"value": [1]})

    result = frame.to_json(orient="columns", force_ascii=False, indent=2)

    assert result == '{"value":{"0":1}}'
    writer.assert_called_once()
    kwargs = writer.call_args.kwargs
    assert kwargs["obj"] is frame
    assert kwargs["orient"] == "columns"
    assert kwargs["force_ascii"] is False
    assert kwargs["indent"] == 2


def test_to_parquet_delegates_to_stubbed_parquet_writer(monkeypatch):
    writer = Mock(return_value=b"parquet bytes")
    monkeypatch.setattr(parquet_module, "to_parquet", writer)
    frame = pd.DataFrame({"value": [1]})

    result = frame.to_parquet(
        "data.parquet", engine="pyarrow", compression="gzip", index=False
    )

    assert result == b"parquet bytes"
    writer.assert_called_once_with(
        frame,
        "data.parquet",
        "pyarrow",
        compression="gzip",
        index=False,
        partition_cols=None,
        storage_options=None,
        filesystem=None,
    )