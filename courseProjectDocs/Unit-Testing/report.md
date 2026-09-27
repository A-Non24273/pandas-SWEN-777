# Unit-testing report

## New test cases and rationale

The new file
[`pandas/tests/core/test_course_project_edge_cases.py`](../../pandas/tests/core/test_course_project_edge_cases.py)
contains 7 deterministic edge-case tests:

| Test area | Cases and rationale |
| --- | --- |
| Truth-value evaluation | DataFrame and multi-value Series objects must raise the documented ambiguity error instead of being treated as booleans. |
| Construction | Empty nullable Series preserve their requested dtype, while a DataFrame rejects an index whose length does not match its values. |
| Boolean indexing | A boolean Series is aligned by labels; an unalignable Series raises `IndexingError`. |
| Duplicate labels | Reindexing a duplicate axis raises rather than silently choosing a value. |
| Missing data | `dropna(thresh=...)` counts non-missing values per row, and `fillna(limit=...)` stops after the configured number of values. |
| Concatenation | Concatenating an empty typed frame with populated data preserves the column dtype. |
| Reshaping | `melt(ignore_index=False)` preserves the source index, while `pivot` rejects duplicate index/column combinations. |

These cases exercise boundary conditions and error paths that are easy to
miss when testing only successful, non-empty, uniquely indexed inputs.

## New test results

The command in the README was run against the local checkout:

```text
7 passed in 5.83s
```

| Tests run | Passed | Failed |
| ---: | ---: | ---: |
| 7 | 7 | 0 |

The existing baseline reports 49,203 passing tests. Including these 7 added
tests, the suite represents 49,210 passing tests when run together with the
baseline suite.

## Coverage improvement analysis

The baseline in `courseProjectDocs/Setup/report.md` reports 93% coverage for
the complete `pandas/core` suite, with 49,203 tests. The focused command for
the new module measured execution from only those 7 tests and reported:

```text
TOTAL: 49,203 statements, 35,837 missed, 20,664 branches,
       1,591 partial/missed branches, 21% line coverage
```

The focused 21% value must not be presented as a replacement for the
baseline 93%: it measures the entire `pandas/core` source while running only
the new test file, whereas the baseline measures the complete test suite.
The new tests add 7 passing cases and specifically execute error-handling
and boundary branches in core indexing, construction, missing-data, and
reshape logic. A full-suite coverage run is required to produce a new
aggregate percentage that is directly comparable with the 93% baseline.
