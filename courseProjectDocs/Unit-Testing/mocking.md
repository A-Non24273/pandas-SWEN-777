# Mock Design

## New test cases and rationale

[`courseProjectCode/Metrics/test_metrics.py`](../../courseProjectCode/Metrics/test_metrics.py)
contains three tests for the custom metrics scripts:

| Test | Rationale |
| --- | --- |
| Collection hook counts collected items | Checks the test-count plugin's state update without asking pytest to collect the pandas suite. |
| Testability main coordinates pytest and coverage | Verifies source selection, execution order, and printed test count while avoiding a nested full-suite run and real coverage-data writes. |
| Maintainability main aggregates source analysis | Checks per-file and total LOC/comment-density output, plus the unreadable-file skip path, without reading real source files. |

## Mocking strategy

Use pytest's `monkeypatch` fixture to replace boundaries at the point each
script consumes them. `pytest.main` is a stub that invokes the supplied
collection plugin with two fake items. `coverage.Coverage` is replaced by a
small recording fake so the test can assert that coverage starts before the
runner and stops, saves, and reports afterward. For maintainability,
`os.walk` yields a fixed set of paths and `SourceAnalysis.from_file` returns
fixed code/documentation counts or raises `OSError` for one path.

These are stubs rather than behaviorally complete substitutes: they return
only the values needed to exercise the scripts' own decisions. This keeps the
tests deterministic, fast, independent of pandas' test suite, and independent
of the checkout's filesystem contents.

## Coverage improvement analysis

The new tests directly execute the metrics scripts' orchestration, report
aggregation, percentage calculations, and exception-skip behavior. The
coverage command in [`README.md`](README.md) measures only
`testability.py` and `maintainability.py`; its result must not be compared to
the separate pandas-core coverage numbers, which measure a different source
tree and test scope.

Focused result: **3 tests passed**. Coverage measured 38 statements with 0
missed, 4 branches with 0 partial branches, for **100% coverage** across the
two metrics scripts. This confirms the relevant script lines and branches are
exercised by the mocked tests. No previous focused baseline exists for these
scripts, so a percentage-point increase cannot be claimed; the result is also
not comparable with pandas-core coverage. The measured result is repeated in
[`report.md`](report.md).