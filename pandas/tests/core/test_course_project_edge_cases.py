import numpy as np
import pytest

import pandas as pd
import pandas._testing as tm


# Verify that a DataFrame cannot be used as a single boolean value.
def test_dataframe_truth_value_is_ambiguous():
    frame = pd.DataFrame({"value": [1, 2]})

    with pytest.raises(
        ValueError, match="The truth value of a DataFrame is ambiguous"
    ): bool(frame)


# Verify that a multi-value Series also rejects ambiguous truth-value checks.
def test_series_truth_value_is_ambiguous_for_multiple_values():
    series = pd.Series([True, False])

    with pytest.raises(ValueError, match="The truth value of a Series is ambiguous"):
        bool(series)


# Verify that an empty Series retains its explicitly requested nullable dtype.
def test_empty_series_preserves_explicit_dtype():
    result = pd.Series([], dtype="Int64")

    assert result.empty
    assert result.dtype == "Int64"


# Verify that construction fails when the index length differs from the data.
def test_dataframe_constructor_rejects_mismatched_index_length():
    with pytest.raises(ValueError, match="Length of values"):
        pd.DataFrame({"value": [1, 2]}, index=["only-one"])


# Verify that a boolean Series mask is aligned to the DataFrame's index labels.
def test_loc_boolean_series_aligns_by_index():
    frame = pd.DataFrame({"value": [10, 20]}, index=["a", "b"])
    mask = pd.Series([True, False], index=["b", "a"])

    result = frame.loc[mask]

    expected = pd.DataFrame({"value": [20]}, index=["b"])
    tm.assert_frame_equal(result, expected)


# Verify that indexing fails when a boolean mask cannot be aligned to the frame.
def test_loc_rejects_boolean_mask_with_unalignable_index():
    frame = pd.DataFrame({"value": [10, 20]}, index=["a", "b"])
    mask = pd.Series([True], index=["missing"])

    with pytest.raises(pd.errors.IndexingError, match="Unalignable boolean Series"):
        frame.loc[mask]


# Verify that reindexing refuses an axis containing duplicate labels.
def test_reindex_duplicate_axis_raises():
    series = pd.Series([1, 2], index=["a", "a"])

    with pytest.raises(ValueError, match="cannot reindex on an axis with duplicate"):
        series.reindex(["a"])


# Verify that groupby() with no arguments returns an error
def test_group_series_empty_error():
    series = pd.Series([1, 2])

    with pytest.raises(TypeError, match="You have to supply one of 'by' and 'level'"):
        series.groupby()


# Verify that as_index=False is rejected when grouping a Series
def test_group_series_no_as_index():
    series = pd.Series([1, 2])

    with pytest.raises(TypeError, match="as_index=False only valid with DataFrame"):
        series.groupby([0, 0], as_index=False)


# Verify location of dataframe insert must be an int
def test_df_insert_loc_must_be_int():
    frame = pd.DataFrame({"a": [1, 2]})

    with pytest.raises(TypeError, match="loc must be int"):
        frame.insert("x", "b", [1, 2])


# Verify that a step of zero cannot be used in range index
def test_rangeindex_step_zero():
    with pytest.raises(ValueError, match="Step must not be zero"):
        pd.RangeIndex(0, 10, 0)


# Multiindex level must have the same length as ascending
def test_multiindex_level_length_bad():
    mi = pd.MultiIndex.from_tuples([(1, "a"), (0, "b")])

    with pytest.raises(ValueError, match="level must have same length as ascending"):
        mi.sortlevel(level=[0, 1], ascending=[True])


# Verify arrays can't be compared with nonmatching lengths
def test_compare_arr_wrong_length():
    arr = pd.array([1, 2], dtype="Int64")

    with pytest.raises(ValueError, match="Lengths must match to compare"):
        arr == [1, 2, 3]


# Verify arrays with 2D structure cannot be compared
def test_compare_arr_2d():
    arr = pd.array([1, 2], dtype="Int64")

    with pytest.raises(
        NotImplementedError, match="can only perform ops with 1-d structures"
    ):
        arr == np.array([[1, 2]])


# Verify int cannot be registered as an api extension
def test_int_as_api_extension():
    with pytest.raises(ValueError, match="can only register pandas extension dtypes"):
        pd.api.extensions.register_extension_dtype(int)
