#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import os
import signal
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed, Future
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from notebook_control import load_local_env
from protocol import load_config, require_environment
from resource_guard import physical_cpus, plan_workers, read_mem_available_mb
from results_schema import FIELDS
from tool_adapters import run_task

WRITE_LOCK = threading.Lock()
PAUSE_FILE = ROOT / "results" / "pause.requested"


def read_results(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_results(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    by_id = {str(row["run_id"]): row for row in rows}
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(by_id.values())
    temporary.replace(path)


def completed_ids(rows: list[dict[str, str]]) -> set[str]:
    return {row["run_id"] for row in rows if row.get("status") == "ok"}


def total_cost(rows: list[dict[str, str]]) -> float:
    return sum(float(row.get("cost_usd") or 0) for row in rows)


def cleanup_containers() -> None:
    found = subprocess.run(
        ["docker", "ps", "-aq", "--filter", "label=teori.experiment=codamosa"],
        capture_output=True, text=True,
    ).stdout.split()
    if found:
        subprocess.run(["docker", "rm", "-f", *found], capture_output=True, text=True)


def pause_requested() -> bool:
    return PAUSE_FILE.exists()


def request_pause() -> None:
    PAUSE_FILE.parent.mkdir(parents=True, exist_ok=True)
    PAUSE_FILE.write_text(datetime.now(timezone.utc).isoformat(), encoding="utf-8")


def clear_pause() -> None:
    PAUSE_FILE.unlink(missing_ok=True)


class GracefulInterrupt:
    """Set a flag on SIGINT/SIGTERM so the current in-flight run can finish,
    then the loop exits cleanly. Results are already checkpointed after each
    run, so re-running with --retry-failed resumes from where it left off."""

    def __init__(self) -> None:
        self.interrupted = False
        self._old_sigint = None
        self._old_sigterm = None

    def __enter__(self) -> "GracefulInterrupt":
        self._old_sigint = signal.getsignal(signal.SIGINT)
        self._old_sigterm = signal.getsignal(signal.SIGTERM)

        def handler(signum, frame):
            self.interrupted = True
            print(f"\nReceived signal {signum}; finishing current run(s), then pausing.")

        signal.signal(signal.SIGINT, handler)
        signal.signal(signal.SIGTERM, handler)
        return self

    def __exit__(self, *args) -> None:
        signal.signal(signal.SIGINT, self._old_sigint)
        signal.signal(signal.SIGTERM, self._old_sigterm)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pilot", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-runs", type=int)
    parser.add_argument("--workers", type=int)
    parser.add_argument("--retry-failed", action="store_true")
    parser.add_argument("--pause", action="store_true", help="Create pause.requested and exit without launching runs")
    parser.add_argument("--resume", action="store_true", help="Remove pause.requested before launching")
    args = parser.parse_args()
    load_local_env()
    config = load_config()
    if not args.dry_run:
        require_environment(config)
    matrix = ROOT / "results" / ("pilot_matrix.csv" if args.pilot else "run_matrix.csv")
    results_path = ROOT / "results" / ("pilot_results.csv" if args.pilot else "results.csv")
    if not matrix.exists():
        subprocess.run([sys.executable, str(ROOT / "scripts" / "build_matrix.py"), *(["--pilot"] if args.pilot else [])], check=True)
    matrix_rows = list(csv.DictReader(matrix.open(newline="", encoding="utf-8")))
    results = read_results(results_path)
    done = completed_ids(results)
    pending = [row for row in matrix_rows if row["run_id"] not in done]
    recorded = {row["run_id"] for row in results}
    if not args.retry_failed:
        pending = [row for row in pending if row["run_id"] not in recorded]
    if args.max_runs is not None:
        pending = pending[: args.max_runs]
    state = {
        "matrix": str(matrix), "results": str(results_path), "total": len(matrix_rows),
        "completed_ok": len(done), "recorded": len(results), "pending": len(pending),
        "cost_usd": total_cost(results),
    }
    if args.dry_run:
        print(json.dumps(state, indent=2))
        return 0

    if args.pause:
        request_pause()
        print(f"Pause requested: {PAUSE_FILE}. No runs launched.")
        return 0

    clear_pause()

    experiment = config["experiment"]
    rpm = int(experiment.get("rate_limit_rpm", 0) or 0)
    if rpm > 0:
        os.environ["RPM_LIMIT"] = str(rpm)
    probe_path = ROOT / "results" / "endpoint_probe.json"
    probes = json.loads(probe_path.read_text(encoding="utf-8")) if probe_path.exists() else []
    probed_models = {
        (str(entry.get("backbone")), str(entry.get("model_requested")))
        for entry in probes if entry.get("passed")
    }
    unprobed = [row for row in pending if (row["backbone"], row["model_requested"]) not in probed_models]
    if unprobed:
        totals: dict[str, int] = {}
        for row in unprobed:
            key = f"{row['backbone']}/{row['model_requested']}"
            totals[key] = totals.get(key, 0) + 1
        print("Runner probe gate blocks the following rows until scripts/probe_endpoints.py passes for them:")
        for key, count in sorted(totals.items(), key=lambda item: -item[1]):
            print(f"  {key}: {count}")
        pending = [row for row in pending if row not in unprobed]
    if not pending:
        print(json.dumps({**state, "pending": 0, "blocked_all": True}, indent=2))
        return 0

    cap = float(experiment["cost_cap_usd"])
    launch_cap = cap * float(experiment["stop_launch_fraction"])
    if total_cost(results) >= launch_cap:
        raise RuntimeError("Cost reached the 80% launch-stop threshold")
    pilot_started = ROOT / "results" / "pilot_started_at.txt"
    if args.pilot and not pilot_started.exists():
        pilot_started.write_text(datetime.now(timezone.utc).isoformat(), encoding="utf-8")
    if pilot_started.exists():
        start = datetime.fromisoformat(pilot_started.read_text(encoding="utf-8").strip())
        elapsed_days = (datetime.now(timezone.utc) - start).total_seconds() / 86400
        if elapsed_days >= float(experiment["elapsed_cap_days"]) * float(experiment["stop_launch_fraction"]):
            raise RuntimeError("Elapsed time reached the 80% launch-stop threshold")

    workers = args.workers or plan_workers(int(experiment["parallel_workers"]), experiment["worker_memory"])
    print(json.dumps(state, indent=2))
    print(
        f"Starting {len(pending)} runs with {workers} workers "
        f"(configured={experiment['parallel_workers']}, physical_cpus={physical_cpus()}, "
        f"mem_available_mb={read_mem_available_mb()})"
    )
    print("Pause at any time: touch results/pause.requested  (or run: python scripts/run_experiment.py --pause)")
    print("Resume after pause: python scripts/run_experiment.py --resume [--retry-failed]")
    cleanup_containers()
    started = time.monotonic()
    interrupt = GracefulInterrupt()
    try:
        with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="experiment") as pool:
            future_rows: dict[Future, dict] = {pool.submit(run_task, row, ROOT / "results"): row for row in pending}
            for index, future in enumerate(as_completed(future_rows), 1):
                matrix_row = future_rows[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {field: "" for field in FIELDS}
                    result.update(matrix_row)
                    result.update(status="failed", error_category="crash", end_time=datetime.now(timezone.utc).isoformat())
                    print(f"{matrix_row['run_id']}: unexpected worker error: {exc}")
                with WRITE_LOCK:
                    results = [row for row in results if row.get("run_id") != result["run_id"]]
                    results.append(result)
                    write_results(results_path, results)
                status = result.get("status")
                print(
                    f"[{index}/{len(pending)}] {result['run_id']} {status} "
                    f"cost=${float(result.get('cost_usd') or 0):.6f} "
                    f"elapsed={time.monotonic() - started:.1f}s"
                )
                if total_cost(results) >= launch_cap:
                    print("STOP: reached 80% cost threshold; no further runs should launch")
                    break
                if interrupt.interrupted or pause_requested():
                    print("Interrupt/pause detected; not launching additional runs.")
                    break
    finally:
        cleanup_containers()
    print(f"Checkpoint: {results_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
