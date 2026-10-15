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

## Full-suite core coverage

To run the full pandas test suite and measure coverage for `pandas/core`, use:

```bash
PATH="$PWD/.venv/bin:$PATH" .venv/bin/python -m pytest pandas/tests -q \
  --cov=pandas/core --cov-report=term
```

## Mock-based pandas core tests

The added core tests are in
[`pandas/tests/core/test_course_project_mocks.py`](../../pandas/tests/core/test_course_project_mocks.py).
They stub the optional Markdown formatter, pandas' handle API, NumExpr
evaluation, the low-level JSON encoder, and the Parquet engine. The assertions
check pandas' inputs and transformations at each boundary, along with returned
or written output.

Run the tests from the repository root in the configured pandas development
environment (the local build prerequisites are listed above):

```bash
PATH="$PWD/.venv/bin:$PATH" .venv/bin/python -m pytest \
  -q pandas/tests/core/test_course_project_mocks.py
```

The expected result is `5 passed`. To reproduce the focused coverage report,
run coverage and report only the pandas implementation modules used by the
tests:

```bash
COVERAGE_RCFILE=/dev/null PATH="$PWD/.venv/bin:$PATH" \
  .venv/bin/python -m coverage run \
  --include='*/pandas/core/frame.py,*/pandas/core/generic.py,*/pandas/core/computation/expressions.py,*/pandas/io/json/_json.py,*/pandas/io/parquet.py' \
  -m pytest -q pandas/tests/core/test_course_project_mocks.py
COVERAGE_RCFILE=/dev/null PATH="$PWD/.venv/bin:$PATH" \
  .venv/bin/python -m coverage report \
  --include='*/pandas/core/frame.py,*/pandas/core/generic.py,*/pandas/core/computation/expressions.py,*/pandas/io/json/_json.py,*/pandas/io/parquet.py' \
  --show-missing
```

For the test rationale, mock boundaries, and coverage interpretation, see
[`mocking.md`](mocking.md).
