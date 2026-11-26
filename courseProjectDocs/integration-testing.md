# How to run

1. Create a venv if you don't have one already
```bash
python -m venv venv
```

2. Activate the venv
```bash
source ./venv/bin/activate
```

3. Build the pandas module
```bash
pip install -e . --no-build-isolation --no-deps
```

4. Install the rest of the dependencies
```bash
pip install -r requirements-dev.txt
```

5. Run the integration tests
```bash
pytest pandas/tests/test_integration.py
```