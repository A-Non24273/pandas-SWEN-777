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

