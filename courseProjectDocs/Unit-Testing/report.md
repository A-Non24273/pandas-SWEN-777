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

The existing baseline reports 49,203 passing tests. Including these 20 added
tests, the suite represents 49,223 passing tests when run together with the
baseline suite.

## Coverage improvement analysis

The baseline in `courseProjectDocs/Setup/report.md` reports 93% coverage for
the complete `pandas/core` suite, with 49,203 tests. The focused command for
the new module measured execution from only those 20 tests and reported:

```text
TOTAL: 49,203 statements, 35,796 missed, 20,664 branches,
       1,601 partial branches, 21% line coverage
```

The focused 21% value must not be presented as a replacement for the
baseline 93%: it measures the entire `pandas/core` source while running only
the new test file, whereas the baseline measures the complete test suite.
The new tests add 20 passing cases and specifically execute error-handling
and boundary branches in core indexing, construction, grouping, insertion,
range and multi-index handling, comparisons, missing-data, concatenation,
reshaping, and API extension registration. A full-suite coverage run is
required to produce a new aggregate percentage that is directly comparable
with the 93% baseline.

## Mock-based metrics tests

[`courseProjectCode/Metrics/test_metrics.py`](../../courseProjectCode/Metrics/test_metrics.py)
adds three tests covering the test-count hook, testability/coverage
orchestration, and maintainability aggregation. The tests replace pytest,
coverage, filesystem traversal, and source analysis with deterministic stubs.

The focused test command, dependency setup, and mock rationale are documented
in [`README.md`](README.md) and [`mocking.md`](mocking.md).

The coverage command reports only `testability.py` and `maintainability.py`.
This focused metric for the custom course scripts is not directly comparable
with either the 93% full-suite pandas-core baseline or the 21% pandas-core
edge-case run. Test execution and the measured focused percentage are recorded
below.

### Mock-test results and coverage

The documented focused test command completed successfully:

```text
3 passed in 0.18s
```

The documented coverage command reported:

```text
TOTAL  38 statements, 0 missed, 4 branches, 0 partial branches, 100% coverage
```

Both metrics scripts were fully covered by this focused run. There is no
previous coverage baseline for these two scripts, so 100% is the resulting
focused coverage, not a quantified percentage-point increase. The pandas-core
figures above use a different codebase scope and are not comparable.
