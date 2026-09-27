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


