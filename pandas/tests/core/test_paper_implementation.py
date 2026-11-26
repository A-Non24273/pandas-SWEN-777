from unittest import mock

import pandas as pd


def test_plot_dispatches_to_mocked_backend():
    # Test that DataFrame.plot looks up the correct backend and forwards the correct call
    frame = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    backend = mock.MagicMock(__name__="fake_backend")

    with mock.patch(
        "pandas.plotting._core._get_plot_backend", return_value=backend
    ) as get_backend:
        result = frame.plot(x="a", y="b", kind="bar", backend="fake_backend")

    get_backend.assert_called_once_with("fake_backend")
    backend.plot.assert_called_once_with(frame, x="a", y="b", kind="bar")
    assert result is backend.plot.return_value


def test_to_clipboard_calls_mocked_clipboard_set():
    # Test that to_clipboard sends text to the mocked clipboard
    frame = pd.DataFrame({"a": [1, 2], "b": [3, 4]})

    with mock.patch("pandas.io.clipboard.clipboard_set") as clipboard_set:
        result = frame.to_clipboard(index=False)

    assert result is None
    clipboard_set.assert_called_once_with("a\tb\n1\t3\n2\t4\n")
