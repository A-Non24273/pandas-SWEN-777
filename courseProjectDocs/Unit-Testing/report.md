# Unit-testing report

## New test cases and rationale

The new file
[`pandas/tests/core/test_course_project_edge_cases.py`](../../pandas/tests/core/test_course_project_edge_cases.py)
contains 20 deterministic edge-case tests:

| Test area | Cases and rationale |
| --- | --- |
| Truth-value evaluation | DataFrame and multi-value Series objects must raise the documented ambiguity error instead of being treated as booleans. |
| Construction | Empty nullable Series preserve their requested dtype, while a DataFrame rejects an index whose length does not match its values. |
| Boolean indexing | A boolean Series is aligned by labels; an unalignable Series raises `IndexingError`. |
| Duplicate labels | Reindexing a duplicate axis raises rather than silently choosing a value. |
| Missing data | `dropna(thresh=...)` counts non-missing values per row, and `fillna(limit=...)` stops after the configured number of values. |
| Concatenation | Concatenating an empty typed frame with populated data preserves the column dtype. |
| Reshaping | `melt(ignore_index=False)` preserves the source index, while `pivot` rejects duplicate index/column combinations. |
| Grouping | Grouping with args empty causes error. Grouping with as_index causes error. |
| Inserting | Inserting into a DataFrame with an index that is not an int causes an error. |
| RangeIndex | Calling RangeIndex with a step of 0 causes an error. |
| Sorting MultiIndex | Sorting a MultiIndex using args of different length cause an error. |
| Comparing | Comparing two pd.arrays with different lengths causes an error. Comparing a 1-dimensional array with a 2-dimensional array causes an error. |
| API Extension | Registering int as an api extension causes an error. |


These cases exercise boundary conditions and error paths that are easy to
miss when testing only successful, non-empty, uniquely indexed inputs.

## New test results

The command in the README was run against the local checkout:

```text
20 passed in 1.13s
```

| Tests run | Passed | Failed |
| ---: | ---: | ---: |
| 20 | 20 | 0 |

These tests are included in the full-suite run described below.

## Coverage improvement analysis

The full `pandas/tests` suite was run with coverage scoped to `pandas/core`.
The command excluded network-marked tests, the clipboard tests (which require
the unavailable `qapp` fixture), and the XML test module with URL-dependent
cases:

```text
178876 passed, 29333 skipped, 127 deselected, 666 xfailed
```

The coverage report for `pandas/core` was:

```text
TOTAL: 49,203 statements, 6,516 missed, 20,664 branches,
       1,728 partial branches, 85% branch-aware coverage
```

The 20 new edge-case tests contribute additional coverage for boundary and
error paths in core indexing, construction, grouping, insertion, range and
multi-index handling, comparisons, missing-data, concatenation, reshaping,
and API extension registration. Reproduce the full-suite run with the command
in [`README.md`](README.md).
