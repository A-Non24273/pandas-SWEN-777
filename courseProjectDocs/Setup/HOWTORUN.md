To run the unit test coverage code, first create a python virtual environment

```bash
python -m venv venv
```

Then install dependencies:

```bash
./venv/bin/pip install -r ./requirements.txt
./venv/bin/pip install -r ./courseProjectCode/requirements.txt
```

For some reason, there is an issue sometimes when compiling due to missing git tags, this can be resolved with:

```bash
git remote add upstream https://github.com/pandas-dev/pandas.git 2>/dev/null || true
git fetch upstream --tags
```

After fetching the tags, run this:

```bash
./venv/bin/pip install -e . --no-build-isolation --no-deps
```

Then, you can run and view the reports with:

```bash
./venv/bin/python ./courseProjectCode/Metrics/testability.py
./venv/bin/python ./courseProjectCode/Metrics/maintainability.py
```