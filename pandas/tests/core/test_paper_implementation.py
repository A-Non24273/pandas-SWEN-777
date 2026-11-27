from unittest import mock

import pandas as pd
import os



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
    frame = pd.DataFrame({"a": [1, 2], "b": [3, 4]})

    with mock.patch("pandas.io.clipboard.clipboard_set") as clipboard_set:
        result = frame.to_clipboard(index=False)

    assert result is None
#os.lineup makes the test platform independant
    expected = (
        f"a\tb{os.linesep}"
        f"1\t3{os.linesep}"
        f"2\t4{os.linesep}"
    )

    clipboard_set.assert_called_once_with(expected)


def test_pipe_calls_mocked_function():
    # Test that pipe forwards the DataFrame and arguments to the function
    frame = pd.DataFrame({"a": [1, 2]})
    func = mock.Mock(return_value="result")

    result = frame.pipe(func, factor=2)

    func.assert_called_once()
    passed_frame = func.call_args.args[0]
    pd.testing.assert_frame_equal(passed_frame, frame)
    assert func.call_args.kwargs == {"factor": 2}
    assert result == "result"


def test_apply_calls_mocked_function_for_each_column():
    # Test that apply calls the function with each column as a Series
    frame = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    func = mock.Mock(return_value=0)

    frame.apply(func)

    assert func.call_count == 2
    pd.testing.assert_series_equal(func.call_args_list[0].args[0], frame["a"])
    pd.testing.assert_series_equal(func.call_args_list[1].args[0], frame["b"])
