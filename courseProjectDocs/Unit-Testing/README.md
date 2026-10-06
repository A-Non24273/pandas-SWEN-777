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

## Mock-based metrics tests

The metrics tests are in
[`courseProjectCode/Metrics/test_metrics.py`](../../courseProjectCode/Metrics/test_metrics.py).
They stub pytest collection, the coverage API, and source-analysis/file
traversal so the results do not depend on running the full pandas test suite or
reading the checkout's source files.

From the repository root, create a virtual environment and install the course
project dependencies (skip these steps if they are already installed in your
environment):

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r courseProjectCode/requirements.txt
```

Run the tests with:

```bash
.venv/bin/python -m pytest courseProjectCode/Metrics/test_metrics.py
```

To reproduce the focused coverage measurement for the two metrics scripts:

```bash
.venv/bin/python -m coverage run \
  --source=courseProjectCode.Metrics \
  --omit='*/test_metrics.py' \
  -m pytest courseProjectCode/Metrics/test_metrics.py
.venv/bin/python -m coverage report -m \
  --omit='*/test_metrics.py'
```

The design rationale and coverage interpretation are in
[`mocking.md`](mocking.md).

