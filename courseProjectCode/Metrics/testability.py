"""
This file is used to calculate the testability of the pandas core code. It calculates:
- Number of unit test cases
- Test coverage
"""

import pytest

class TestCounterPlugin:
    def __init__(self):
        self.test_count = 0

    def pytest_collection_modifyitems(self, items):
        # hook that runs automatically during collection
        self.test_count = len(items)


def main():
    counter = TestCounterPlugin()

    pytest.main([
        ".", # path
        "--collect-only", # just finds the tests, doesn't run them
        "-q" # clean output
    ], plugins=[counter])

    print(f"Total test cases found: {counter.test_count}")




if __name__ == "__main__":
    main()