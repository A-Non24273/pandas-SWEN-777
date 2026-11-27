"""
Stress tests for a pandas sales-report workflow.

The tests push the workflow past a comfortable load and record how it behaves,
rather than checking that it stays fast. Each request runs the same user flow
as ``test_system.py``, at scale: derive revenue, pivot revenue by region and
month, and rank the top customers.

- ``test_concurrent_users_ramp`` ramps the number of concurrent users
  (threads sharing one DataFrame) and records latency, throughput, CPU and
  memory at each level.
- ``test_data_volume_ramp_until_memory_failure`` doubles the data volume
  inside a memory-capped child process until pandas fails. It records where
  and how it fails, and whether the process recovers.
- ``test_profile_report_hotspots`` profiles one large request to find where
  the time goes.

Metrics are printed and written as JSON to ``$PANDAS_STRESS_REPORT_DIR``
(default: a pytest temporary directory). The tests run on Linux and Windows;
the memory-failure test needs ``RLIMIT_AS`` and runs on Linux only. Run with::

    pytest pandas/tests/test_stress.py -m slow
"""

from __future__ import annotations

import cProfile
from concurrent.futures import ThreadPoolExecutor
import gc
import json
import os
from pathlib import Path
import platform
import pstats
import subprocess
import sys
import threading
import time

import numpy as np
import pytest

import pandas as pd

IS_LINUX = sys.platform.startswith("linux")
IS_WINDOWS = sys.platform == "win32"

if not (IS_LINUX or IS_WINDOWS):
    pytest.skip(
        "reads memory usage via /proc or the Win32 API", allow_module_level=True
    )

pytestmark = [pytest.mark.slow, pytest.mark.single_cpu]

# Concurrency ramp: simulated users per level, and how long each level runs.
USER_LEVELS = (1, 2, 4, 8, 16, 32)
STEP_SECONDS = 3.0
CONCURRENCY_ROWS = 100_000

# Volume ramp: address-space budget for the child process, on top of what it
# uses after importing pandas, and the row counts to try.
MEMORY_BUDGET_MB = 1024
VOLUME_START_ROWS = 125_000
VOLUME_MAX_ROWS = 64_000_000
CHILD_TIMEOUT_SECONDS = 600

PROFILE_ROWS = 1_000_000
SAMPLE_INTERVAL_SECONDS = 0.1

REGIONS = np.array(["North", "South", "East", "West"], dtype=object)
CUSTOMERS = np.array([f"C{i:05d}" for i in range(10_000)], dtype=object)


def make_orders(n_rows: int, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    days = pd.to_timedelta(rng.integers(0, 366, n_rows), unit="D")
    return pd.DataFrame(
        {
            "order_id": np.arange(n_rows, dtype=np.int64),
            "order_date": pd.Timestamp("2024-01-01") + days,
            "customer": CUSTOMERS[rng.integers(0, len(CUSTOMERS), n_rows)],
            "region": REGIONS[rng.integers(0, len(REGIONS), n_rows)],
            "quantity": rng.integers(1, 10, n_rows),
            "unit_price": rng.uniform(1, 100, n_rows).round(2),
        }
    )


def run_report(orders: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Handle one request: the sales-report user flow."""
    enriched = orders.assign(
        revenue=orders["quantity"] * orders["unit_price"],
        month=orders["order_date"].dt.month,
    )
    by_region = enriched.pivot_table(
        index="region", columns="month", values="revenue", aggfunc="sum"
    )
    top_customers = enriched.groupby("customer")["revenue"].sum().nlargest(10)
    return by_region, top_customers


def _proc_status_mb(key: str) -> float:
    with open("/proc/self/status", encoding="ascii") as fh:
        for line in fh:
            if line.startswith(key):
                return int(line.split()[1]) / 1024
    return float("nan")


if IS_WINDOWS:
    import ctypes
    from ctypes import wintypes

    class _ProcessMemoryCounters(ctypes.Structure):
        _fields_ = [
            ("cb", wintypes.DWORD),
            ("PageFaultCount", wintypes.DWORD),
            ("PeakWorkingSetSize", ctypes.c_size_t),
            ("WorkingSetSize", ctypes.c_size_t),
            ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
            ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
            ("PagefileUsage", ctypes.c_size_t),
            ("PeakPagefileUsage", ctypes.c_size_t),
        ]

    _kernel32 = ctypes.WinDLL("kernel32")
    _kernel32.GetCurrentProcess.restype = wintypes.HANDLE
    _psapi = ctypes.WinDLL("psapi")
    _psapi.GetProcessMemoryInfo.argtypes = [
        wintypes.HANDLE,
        ctypes.POINTER(_ProcessMemoryCounters),
        wintypes.DWORD,
    ]
    _psapi.GetProcessMemoryInfo.restype = wintypes.BOOL

    def _rss_mb() -> float:
        # The working set is Windows' equivalent of RSS.
        counters = _ProcessMemoryCounters()
        counters.cb = ctypes.sizeof(counters)
        ok = _psapi.GetProcessMemoryInfo(
            _kernel32.GetCurrentProcess(), ctypes.byref(counters), counters.cb
        )
        return counters.WorkingSetSize / 2**20 if ok else float("nan")

else:

    def _rss_mb() -> float:
        return _proc_status_mb("VmRSS:")


class ResourceSampler:
    """Sample this process's RSS and CPU utilisation on a background thread.

    ``cpu_pct`` is CPU time over wall time across all threads, so 100 means
    one fully busy core.
    """

    def __init__(self, interval: float = SAMPLE_INTERVAL_SECONDS) -> None:
        self.interval = interval
        self.samples: list[dict] = []
        self.label = ""
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._t0 = 0.0

    def __enter__(self) -> ResourceSampler:
        self._t0 = time.perf_counter()
        self._thread.start()
        return self

    def __exit__(self, *exc_info) -> None:
        self._stop.set()
        self._thread.join()

    def _run(self) -> None:
        last_wall, last_cpu = time.perf_counter(), time.process_time()
        while not self._stop.wait(self.interval):
            wall, cpu = time.perf_counter(), time.process_time()
            self.samples.append(
                {
                    "t": round(wall - self._t0, 3),
                    "rss_mb": round(_rss_mb(), 1),
                    "cpu_pct": round(100 * (cpu - last_cpu) / (wall - last_wall), 1),
                    "label": self.label,
                }
            )
            last_wall, last_cpu = wall, cpu

    def peak_rss_mb(self, label: str | None = None) -> float:
        values = [
            s["rss_mb"] for s in self.samples if label is None or s["label"] == label
        ]
        return max(values, default=_rss_mb())


@pytest.fixture(scope="module")
def stress_report(tmp_path_factory):
    report = {
        "environment": {
            "python": platform.python_version(),
            "gil_enabled": getattr(sys, "_is_gil_enabled", lambda: True)(),
            "pandas": pd.__version__,
            "numpy": np.__version__,
            "cpu_count": os.cpu_count(),
            "platform": platform.platform(),
        }
    }
    yield report
    out_dir = Path(
        os.environ.get("PANDAS_STRESS_REPORT_DIR")
        or tmp_path_factory.mktemp("stress_report")
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "stress_metrics.json"
    out_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nstress metrics written to {out_file}")


def _run_user_level(orders, n_users, duration, expected):
    """Run ``n_users`` concurrent users, each sending requests until the
    deadline. Returns per-request latencies, errors and elapsed wall time."""
    expected_pivot = expected[0].to_numpy()
    expected_top = expected[1].index.tolist()
    latencies: list[float] = []
    errors: list[str] = []
    lock = threading.Lock()
    barrier = threading.Barrier(n_users + 1)

    def user(deadline_holder):
        barrier.wait()
        deadline = deadline_holder[0]
        while time.perf_counter() < deadline:
            start = time.perf_counter()
            try:
                by_region, top_customers = run_report(orders)
            except Exception as err:  # record, keep the other users running
                with lock:
                    errors.append(repr(err))
                continue
            latency = time.perf_counter() - start
            correct = (
                np.allclose(by_region.to_numpy(), expected_pivot)
                and top_customers.index.tolist() == expected_top
            )
            with lock:
                latencies.append(latency)
                if not correct:
                    errors.append("wrong result")

    deadline_holder = [0.0]
    with ThreadPoolExecutor(max_workers=n_users) as pool:
        futures = [pool.submit(user, deadline_holder) for _ in range(n_users)]
        deadline_holder[0] = time.perf_counter() + duration
        start_wall, start_cpu = time.perf_counter(), time.process_time()
        barrier.wait()
        for future in futures:
            future.result()
        elapsed = time.perf_counter() - start_wall
        cpu_seconds = time.process_time() - start_cpu
    return latencies, errors, elapsed, cpu_seconds


def test_concurrent_users_ramp(stress_report):
    orders = make_orders(CONCURRENCY_ROWS)
    expected = run_report(orders)  # reference result, also warms up caches
    levels = []

    with ResourceSampler() as sampler:
        for n_users in USER_LEVELS:
            label = f"{n_users} users"
            sampler.label = label
            latencies, errors, elapsed, cpu_seconds = _run_user_level(
                orders, n_users, STEP_SECONDS, expected
            )
            ms = np.array(latencies) * 1000
            levels.append(
                {
                    "users": n_users,
                    "requests": len(latencies),
                    "errors": len(errors),
                    "error_samples": errors[:5],
                    "elapsed_s": round(elapsed, 3),
                    "throughput_rps": round(len(latencies) / elapsed, 2),
                    "latency_ms": {
                        "mean": round(float(ms.mean()), 1),
                        "p50": round(float(np.percentile(ms, 50)), 1),
                        "p95": round(float(np.percentile(ms, 95)), 1),
                        "p99": round(float(np.percentile(ms, 99)), 1),
                        "max": round(float(ms.max()), 1),
                    },
                    "cpu_pct": round(100 * cpu_seconds / elapsed, 1),
                    "peak_rss_mb": sampler.peak_rss_mb(label),
                }
            )
        sampler.label = "idle"
        time.sleep(3 * SAMPLE_INTERVAL_SECONDS)

    stress_report["concurrency"] = {
        "rows": CONCURRENCY_ROWS,
        "step_seconds": STEP_SECONDS,
        "levels": levels,
        "timeline": sampler.samples,
    }

    print(f"\nconcurrent users ramp ({CONCURRENCY_ROWS:,} rows per request)")
    print(f"{'users':>5} {'reqs':>5} {'err':>4} {'req/s':>7} {'p50 ms':>8} "
          f"{'p95 ms':>8} {'max ms':>8} {'cpu %':>6} {'rss MB':>7}")
    for lv in levels:
        lat = lv["latency_ms"]
        print(f"{lv['users']:>5} {lv['requests']:>5} {lv['errors']:>4} "
              f"{lv['throughput_rps']:>7} {lat['p50']:>8} {lat['p95']:>8} "
              f"{lat['max']:>8} {lv['cpu_pct']:>6} {lv['peak_rss_mb']:>7}")

    # Overload may make the system slow, but every request must still finish
    # with the right answer: no exceptions, no corrupted shared state.
    for lv in levels:
        assert lv["requests"] > 0, lv
        assert lv["errors"] == 0, lv


def _volume_ramp_child(budget_mb: int) -> None:
    """Child process entry point: cap the address space, then double the data
    volume until pandas runs out of memory. Prints one JSON line."""
    import resource

    baseline_vm_mb = _proc_status_mb("VmSize:")
    cap_mb = int(baseline_vm_mb + budget_mb)
    resource.setrlimit(resource.RLIMIT_AS, (cap_mb * 2**20, resource.RLIM_INFINITY))

    steps: list[dict] = []
    failure = None
    with ResourceSampler() as sampler:
        n_rows = VOLUME_START_ROWS
        while n_rows <= VOLUME_MAX_ROWS:
            sampler.label = f"{n_rows} rows"
            stage = "build"
            try:
                t0 = time.perf_counter()
                orders = make_orders(n_rows)
                t1 = time.perf_counter()
                stage = "report"
                run_report(orders)
                t2 = time.perf_counter()
            except MemoryError as err:
                failure = {"rows": n_rows, "stage": stage, "error": type(err).__name__,
                           "message": str(err)[:300]}
                break
            steps.append(
                {
                    "rows": n_rows,
                    "build_s": round(t1 - t0, 3),
                    "report_s": round(t2 - t1, 3),
                    "rows_per_s": round(n_rows / (t2 - t1)),
                    "frame_mb": round(orders.memory_usage(deep=True).sum() / 2**20, 1),
                    "peak_rss_mb": sampler.peak_rss_mb(sampler.label),
                }
            )
            del orders
            n_rows *= 2

        orders = None
        gc.collect()
        rss_after_failure = _rss_mb()

        def attempt(label, n):
            sampler.label = label
            try:
                by_region, top = run_report(make_orders(n, seed=1))
            except MemoryError as err:
                return {"rows": n, "ok": False, "error": str(err)[:300]}
            return {"rows": n, "ok": by_region.shape == (4, 12) and len(top) == 10}

        recovery = attempt("recovery", 10_000)
        retry_last_ok = attempt("retry", steps[-1]["rows"]) if steps else None

    print(
        json.dumps(
            {
                "budget_mb": budget_mb,
                "baseline_vm_mb": round(baseline_vm_mb, 1),
                "cap_mb": cap_mb,
                "steps": steps,
                "failure": failure,
                "rss_after_failure_mb": round(rss_after_failure, 1),
                "recovery": recovery,
                "retry_last_ok": retry_last_ok,
                "timeline": sampler.samples,
            }
        )
    )


@pytest.mark.skipif(not IS_LINUX, reason="memory cap uses RLIMIT_AS (Linux only)")
def test_data_volume_ramp_until_memory_failure(stress_report):
    child = (
        "import runpy, sys; "
        "runpy.run_path(sys.argv[1])['_volume_ramp_child'](int(sys.argv[2]))"
    )
    start = time.perf_counter()
    proc = subprocess.run(
        [sys.executable, "-W", "ignore", "-c", child, __file__, str(MEMORY_BUDGET_MB)],
        capture_output=True,
        text=True,
        timeout=CHILD_TIMEOUT_SECONDS,
        check=False,
    )
    wall = time.perf_counter() - start

    # A crash (e.g. -11 for SIGSEGV, -9 for the OOM killer) is a failure of
    # the test: running out of memory must surface as a Python exception.
    assert proc.returncode == 0, f"child exited {proc.returncode}\n{proc.stderr}"
    result = json.loads(proc.stdout.strip().splitlines()[-1])
    result["wall_s"] = round(wall, 2)
    stress_report["volume"] = result

    print(f"\ndata volume ramp (address space capped at +{MEMORY_BUDGET_MB} MB)")
    print(f"{'rows':>11} {'build s':>8} {'report s':>9} {'rows/s':>11} "
          f"{'frame MB':>9} {'rss MB':>7}")
    for step in result["steps"]:
        print(f"{step['rows']:>11,} {step['build_s']:>8} {step['report_s']:>9} "
              f"{step['rows_per_s']:>11,} {step['frame_mb']:>9} "
              f"{step['peak_rss_mb']:>7}")
    print(f"failure:   {result['failure']}")
    print(f"recovery:  {result['recovery']}")
    print(f"retry:     {result['retry_last_ok']}")

    failure = result["failure"]
    assert failure is not None, "never reached the memory limit"
    assert failure["error"] == "MemoryError"
    # After the failure the process keeps working: small requests succeed,
    # and so does the largest size that succeeded before the failure.
    assert result["recovery"]["ok"], result["recovery"]
    assert result["retry_last_ok"]["ok"], result["retry_last_ok"]


def test_profile_report_hotspots(stress_report):
    orders = make_orders(PROFILE_ROWS)
    run_report(orders)  # warm up

    profiler = cProfile.Profile()
    profiler.enable()
    by_region, top_customers = run_report(orders)
    profiler.disable()

    stats = pstats.Stats(profiler)
    total = stats.total_tt
    hotspots = sorted(
        (
            {
                "function": f"{Path(file).name}:{line}({name})",
                "calls": calls,
                "tottime_s": round(tottime, 4),
                "share_pct": round(100 * tottime / total, 1),
            }
            for (file, line, name), (_, calls, tottime, _, _) in stats.stats.items()
        ),
        key=lambda h: h["tottime_s"],
        reverse=True,
    )[:10]

    # Same aggregation with the string key converted to a categorical, to
    # check whether the string key is the cost.
    enriched = orders.assign(revenue=orders["quantity"] * orders["unit_price"])
    customer_cat = enriched["customer"].astype("category")

    def best_of(func, repeat=5):
        times = []
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = func()
            times.append(time.perf_counter() - t0)
        return min(times), result

    str_s, by_str = best_of(lambda: enriched.groupby("customer")["revenue"].sum())
    cat_s, by_cat = best_of(
        lambda: enriched["revenue"].groupby(customer_cat, observed=True).sum()
    )
    by_cat.index = by_cat.index.astype(by_str.index.dtype)
    pd.testing.assert_series_equal(by_str, by_cat, check_names=False)

    stress_report["profile"] = {
        "rows": PROFILE_ROWS,
        "total_s": round(total, 4),
        "hotspots": hotspots,
        "groupby_key_dtype": str(enriched["customer"].dtype),
        "groupby_str_key_s": round(str_s, 4),
        "groupby_category_key_s": round(cat_s, 4),
        "speedup": round(str_s / cat_s, 2),
    }

    print(f"\nprofile of one request ({PROFILE_ROWS:,} rows, {total:.3f}s)")
    for h in hotspots:
        print(f"{h['share_pct']:>5}%  {h['tottime_s']:>7}s  {h['function']}")
    print(f"groupby on {enriched['customer'].dtype} key: {str_s:.4f}s; "
          f"on category key: {cat_s:.4f}s ({str_s / cat_s:.1f}x)")

    assert by_region.shape == (4, 12)
    assert len(top_customers) == 10
