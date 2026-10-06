# Mock Design

## New test cases and rationale

[`pandas/tests/core/test_course_project_mocks.py`](../../pandas/tests/core/test_course_project_mocks.py)
contains five tests that isolate external collaborators used by pandas core:

| Test | Rationale |
| --- | --- |
| `DataFrame.to_markdown` delegates formatting | Replaces optional `tabulate` import and verifies pandas supplies its documented defaults and returns the formatter result. |
| `DataFrame.to_markdown` writes through its handle | Replaces `get_handle` and the output handle, checking path/mode/storage options and ensuring formatted text is written without touching disk. |
| Expression evaluation dispatches to NumExpr | Replaces the NumExpr evaluator and verifies the expression, operands, and safe-casting option forwarded by pandas. |
| `NDFrame.to_json` delegates serialization | Replaces the JSON writer and checks that the object and selected serialization options are forwarded and its result returned. |
| `DataFrame.to_parquet` delegates storage | Replaces the Parquet writer and checks engine, compression, index, and other storage options without requiring an installed Parquet engine or writing a file. |

## Mocking strategy

Use pytest's `monkeypatch` fixture at the point each dependency is consumed.
The formatter test replaces `pandas.core.frame.import_optional_dependency`
with a lightweight object exposing a mock `tabulate` method. The output test
also replaces `pandas.core.frame.get_handle` with a mock context manager whose
handle records writes. The expression test directs `evaluate` through
`_evaluate_numexpr`, forces its eligibility check to pass, and supplies a mock
`ne.evaluate`; this isolates dispatch from NumExpr's implementation and
avoids depending on array-size thresholds or compiled backend behavior.
The JSON and Parquet tests replace `pandas.io.json.to_json` and
`pandas.io.parquet.to_parquet` respectively, validating the wrapper arguments
without invoking their serialization backends.

Each mock preserves the relevant collaborator contract while controlling its
result. Assertions focus on pandas' responsibility: defaults and return
values, output routing, and backend call arguments.

## Coverage improvement analysis

The tests exercise the pandas-core caller paths for Markdown formatting,
output handling, expression backend dispatch, JSON serialization delegation,
and Parquet serialization delegation. The focused coverage command in
[`README.md`](README.md) scopes measurement to `pandas.core.frame`,
`pandas.core.generic`, and `pandas.core.computation.expressions`, rather than
measuring every module under `pandas/core`. The resulting percentages are
test-file-specific and should not be compared directly with the full-suite
93% baseline or the edge-case-only 21% measurement above. Coverage could not yet be measured
because pytest fails during pandas import when the local compiled extensions
are unavailable, and editable installation stalls during metadata preparation
in this untagged checkout. The build and test status are tracked in
[`report.md`](report.md); no numeric coverage increase is claimed before that
focused run succeeds.