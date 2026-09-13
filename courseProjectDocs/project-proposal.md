# Project Overview
Pandas (The Python Data Analysis Library) is the main data manipulation engine for data engineering. It provides fast, flexible, and expressive data structures designed to make data cleaning, alignment, reshaping, and statistics easy. 

The pandas repository contains over 150,000 lines of code including Pyton, Cython, and some C extensions. It has a large-scale, constantly evolving software architecture. 

Our project group chose pandas for this project because of our pre-existing usage and comfort for the package. All of us have used pandas either in course work, or in a data engineering project in the real world. 

# Key Quality Metrics
## Maintainability Metrics
To assess the quality of pandas we used the initial metrics outlined in the "Metrics Baseline" assignment. These metrics track how much effort would be required to comprehend or modify the codebase. These metrics include:
- Lines of Code per File
    - Number of lines of code (LOC) in each individual file.
- Comment Density per File
    - The amount of documentation and comment lines relative to the total lines (code plus comments) in each individual file.
- Total Lines of Code
    - The sum of all of the lines of code (LOC) in the entire core system.
- Total Comment Density
    - The ratio of documentation lines to total lines in the entire core system.

## Testability Metrics
In addition to maintainability tests we looked at the testability of the pandas codebase. These tests look at how thoroughly the software can be validated for it's correctness. The metrics we tracked are:
- Number of Unit Test Cases
    - The total quantity of distinct test items collected across the test quite.
- Test Coverage
    - The percentage of executable Python code ran and verified during test execution.

## Additional Semester Quality Metrics
In addition to the baseline measurements our team looks to implement a few more tests for quality metrics. These metrics are:
- Cognitive Complexity
    - A measure of the mental effort and human readability strain required to understand a function's control flow, placing higher penalties on deeply nested logic, recursion, and complex branching structures.
- Mutation Testing Score
    - The ratio of injected faults (like swapping operators or altering boundary conditions) detected and killed by the test suite.