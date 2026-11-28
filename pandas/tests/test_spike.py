"""
Spike tests for a pandas sales-report workflow.

The tests compare normal, abruptly overloaded, and recovery traffic. They use
the same sales-report flow as the stress tests: derive revenue, pivot revenue
by region and month, and rank the top customers.

Metrics are printed and written as JSON to ``$PANDAS_SPIKE_REPORT_DIR``
(default: a pytest temporary directory). The tests run on Linux and Windows.
Run with::

    pytest pandas/tests/test_spike.py -m slow
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import platform
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

SPIKE_USERS = 32
BASELINE_USERS = 1
RECOVERY_USERS = 1
BASELINE_SECONDS = 2.0
SPIKE_SECONDS = 3.0
RECOVERY_SECONDS = 2.0
SPIKE_ROWS = 100_000
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
    """Sample this process's RSS and CPU utilisation on a background thread."""

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
            sample["rss_mb"]
            for sample in self.samples
            if label is None or sample["label"] == label
        ]
        return max(values, default=_rss_mb())


@pytest.fixture(scope="module")
def spike_report(tmp_path_factory):
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
        os.environ.get("PANDAS_SPIKE_REPORT_DIR")
        or tmp_path_factory.mktemp("spike_report")
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "spike_metrics.json"
    out_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"\nspike metrics written to {out_file}")


def _run_load_phase(orders, n_users, duration, expected):
    """Run a sudden load phase and return request, latency, and error metrics."""
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
            except Exception as err:
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

    ms = np.array(latencies) * 1000
    return {
        "requests": len(latencies),
        "errors": len(errors),
        "error_samples": errors[:5],
        "elapsed_s": round(elapsed, 3),
        "throughput_rps": round(len(latencies) / elapsed, 2),
        "latency_ms": {
            "mean": round(float(ms.mean()), 1) if len(ms) else 0.0,
            "p50": round(float(np.percentile(ms, 50)), 1) if len(ms) else 0.0,
            "p95": round(float(np.percentile(ms, 95)), 1) if len(ms) else 0.0,
            "p99": round(float(np.percentile(ms, 99)), 1) if len(ms) else 0.0,
            "max": round(float(ms.max()), 1) if len(ms) else 0.0,
        },
        "cpu_pct": round(100 * cpu_seconds / elapsed, 1),
    }


def test_sudden_load_spike_and_recovery(spike_report):
    orders = make_orders(SPIKE_ROWS)
    expected = run_report(orders)
    phases = []

    with ResourceSampler() as sampler:
        for name, users, duration in (
            ("baseline", BASELINE_USERS, BASELINE_SECONDS),
            ("spike", SPIKE_USERS, SPIKE_SECONDS),
            ("recovery", RECOVERY_USERS, RECOVERY_SECONDS),
        ):
            sampler.label = name
            result = _run_load_phase(orders, users, duration, expected)
            result["phase"] = name
            result["users"] = users
            result["peak_rss_mb"] = sampler.peak_rss_mb(name)
            phases.append(result)
        sampler.label = "idle"
        time.sleep(3 * SAMPLE_INTERVAL_SECONDS)

    spike_report["sudden_load"] = {
        "rows": SPIKE_ROWS,
        "phases": phases,
        "timeline": sampler.samples,
    }

    print(f"\nsudden load spike ({SPIKE_ROWS:,} rows per request)")
    print(
        f"{'phase':>9} {'users':>5} {'reqs':>5} {'err':>4} {'req/s':>7} "
        f"{'p50 ms':>8} {'p95 ms':>8} {'cpu %':>6} {'rss MB':>7}"
    )
    for phase in phases:
        latency = phase["latency_ms"]
        print(
            f"{phase['phase']:>9} {phase['users']:>5} "
            f"{phase['requests']:>5} {phase['errors']:>4} "
            f"{phase['throughput_rps']:>7} {latency['p50']:>8} "
            f"{latency['p95']:>8} {phase['cpu_pct']:>6} "
            f"{phase['peak_rss_mb']:>7}"
        )

    for phase in phases:
        assert phase["requests"] > 0, phase
        assert phase["errors"] == 0, phase