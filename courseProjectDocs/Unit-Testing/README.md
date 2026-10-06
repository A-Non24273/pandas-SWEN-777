# Added unit tests

The added tests are in
[`pandas/tests/core/test_course_project_edge_cases.py`](../../pandas/tests/core/test_course_project_edge_cases.py).
They cover edge cases for truth-value evaluation, construction, aligned
boolean indexing, duplicate labels, missing values, concatenation, reshaping,
and pivot validation.

## Reproduce the test results

From the repository root, create the environment and install the
local package if this has not already been done:

```bash
python -m venv .venv
.venv/bin/python -m pip install "meson-python>=0.19,<1" "meson>=1.2.3,<2" \
  "Cython>3.1,<4" "numpy>=2.0.2" "pytest>=8.3.4" "pytest-cov>=7.0.0" \
  "versioneer>=0.29" ninja "python-dateutil>=2.9.0"
PATH="$PWD/.venv/bin:$PATH" .venv/bin/python -m pip install -e . \
  --no-build-isolation --no-deps
```

Run the added tests:

```bash
PATH="$PWD/.venv/bin:$PATH" .venv/bin/python -m pytest \
  pandas/tests/core/test_course_project_edge_cases.py
```

To reproduce the focused coverage measurement used in
[`report.md`](report.md):

```bash
PATH="$PWD/.venv/bin:$PATH" .venv/bin/python -m pytest \
  pandas/tests/core/test_course_project_edge_cases.py \
  --cov=pandas/core --cov-report=term-missing
```

## Mock-based pandas core tests

The added core tests are in
[`pandas/tests/core/test_course_project_mocks.py`](../../pandas/tests/core/test_course_project_mocks.py).
They mock the optional `tabulate` formatter, pandas' `get_handle` output
boundary, the NumExpr evaluator, and the JSON and Parquet writer APIs.

Run the tests from the repository root in the configured pandas development
environment:

```bash
PATH="$PWD/.venv/bin:$PATH" .venv/bin/python -m pytest \
  pandas/tests/core/test_course_project_mocks.py
```

To measure coverage only for the core modules exercised by these tests:

```bash
PATH="$PWD/.venv/bin:$PATH" .venv/bin/python -m pytest \
  pandas/tests/core/test_course_project_mocks.py \
  --cov=pandas.core.frame --cov=pandas.core.generic \
  --cov=pandas.core.computation.expressions \
  --cov-report=term-missing
```

The test rationale, mock boundaries, and coverage interpretation are in
[`mocking.md`](mocking.md).

