"""
This file is used to calculate the testability of the pandas core code. It calculates:
- Number of unit test cases
- Test coverage
"""

import pytest
import coverage

class TestCounterPlugin:
    def __init__(self):
        self.test_count = 0

    def pytest_collection_modifyitems(self, items):
        # hook that runs automatically during collection
        self.test_count = len(items)


def main():
    counter = TestCounterPlugin()
    cov = coverage.Coverage(source=["pandas/core"]) # check the coverage of the core while running the tests
    cov.start()

    # run tests with counter and cov
    pytest.main([
        ".", # path
    ], plugins=[counter])

    cov.stop()
    cov.save()

    print(f"Total test cases found: {counter.test_count}")
    print("Code Coverage Report:")
    cov.report()


if __name__ == "__main__":
    main()