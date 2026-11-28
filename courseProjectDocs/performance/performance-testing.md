# Performance Tests
To run, first complete all steps in HOWTORUN.md

## Stress Test
PANDAS_STRESS_REPORT_DIR=courseProjectDocs/performance/stress-out pytest pandas/tests/test_stress.py -m slow -v

## Spike Test
PANDAS_SPIKE_REPORT_DIR=courseProjectDocs/performance/spike-out pytest pandas/tests/test_spike.py -m slow -v