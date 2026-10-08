# Mock Design

## New test cases and rationale

[`pandas/tests/core/test_course_project_mocks.py`](../../pandas/tests/core/test_course_project_mocks.py)
contains five focused tests. Each uses a stub at a collaborator boundary while
asserting behavior implemented by pandas:

| Test | Rationale |
| --- | --- |
| `test_to_markdown_formats_frame_with_stubbed_tabulate` | Verifies `DataFrame.to_markdown` passes the actual frame and its default options to the formatter, then returns its formatted result. |
| `test_to_markdown_writes_to_stubbed_handle` | Verifies pandas sends the formatted content through its handle API, forwarding the path and storage options and returning `None`. |
| `test_expression_evaluates_with_stubbed_numexpr` | Verifies pandas constructs the NumExpr expression with the correct operands and safe-casting option; the stub performs the addition and the result is checked. |
| `test_to_json_uses_pandas_split_payload_with_stubbed_encoder` | Verifies pandas constructs split-orient JSON data without the index and passes the requested encoding options to the encoder. |
| `test_to_parquet_normalizes_partition_columns_with_stubbed_engine` | Verifies pandas normalizes a string partition column to a list and returns bytes written by the engine to its buffer. |

## Mocking strategy

The tests use pytest's `monkeypatch` fixture and small functional stubs instead
of replacing pandas' public methods or asserting that a mock call happened.
The Markdown tests replace the optional `tabulate` import with a formatter
that consumes the real DataFrame values. The output-routing test also replaces
`get_handle` with a context-manager stub backed by a real `StringIO` buffer.

The expression test directs pandas through its NumExpr implementation and
stubs only `ne.evaluate`; the stub computes from the supplied operands so the
test checks the result as well as expression construction. The JSON test stubs
the low-level `ujson_dumps` encoder, allowing assertions on the structure
prepared by pandas' `FrameWriter`. The Parquet test stubs the selected engine;
its writer writes to the real in-memory buffer created by pandas, exercising
partition normalization and the bytes-return path without an optional parquet
dependency.

## Coverage improvement analysis

Reproduce the focused run with the coverage commands in
[`README.md`](README.md). The measured results were:

```text
5 passed
Name                                     Stmts   Miss   Cover
pandas/core/computation/expressions.py     109     56     49%
pandas/core/frame.py                      2528   2176     14%
pandas/core/generic.py                    1984   1528     23%
pandas/io/json/_json.py                    577    434     25%
pandas/io/parquet.py                       188    143     24%
TOTAL                                     5386   4337     19%
```

These percentages are for entire source modules measured while running only
the five new tests; they are not the full-suite coverage rate. The tests
exercise the relevant pandas behavior in each module (Markdown defaults and
output, expression dispatch, JSON payload preparation, and Parquet buffer and
partition handling). The focused percentages therefore show which modules
receive execution, but should not be interpreted as the coverage of those
individual methods or as a direct comparison with full-suite coverage.
