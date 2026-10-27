#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import eval_metrics as em
from results_schema import FIELDS


def test_files(row: dict[str, str]) -> list[Path]:
    base = ROOT / "results" / "generated" / row["run_id"]
    if row["tool"] == "CoverUp":
        return sorted((base / "tests").glob("test_*.py"))
    return sorted(p for p in (base / "output").glob("test_*.py") if "_failing" not in p.name)


def calls_log(row: dict[str, str]) -> Path:
    if row["tool"] == "CoverUp":
        return ROOT / "results" / "raw" / row["run_id"] / "llm_log.jsonl"
    return ROOT / "results" / "generated" / row["run_id"] / "output" / "llm_calls.jsonl"


def evaluate_row(row: dict[str, str], workroot: Path, raw_timeout: float) -> dict[str, str]:
    tests = [p for p in test_files(row) if em.suite_validity(p)[0]]
    if row.get("status") != "ok" or not tests:
        return row
    workroot.mkdir(parents=True, exist_ok=True)
    workdir = Path(tempfile.mkdtemp(prefix=row["run_id"] + "_", dir=str(workroot)))
    try:
        layout = em.LAYOUTS[row["suite"]](row["unit_id"])
        prepared = em.prepare_suite(layout, tests, workdir)
        coverage = em.coverage_of(prepared, workdir)
        row["lines_total"] = str(coverage.get("lines_total", ""))
        row["lines_exec"] = str(coverage.get("lines_covered", ""))
        row["branches_total"] = str(coverage.get("branches_total", ""))
        row["branches_exec"] = str(coverage.get("branches_covered", ""))
        raw = em.raw_validity_of(calls_log(row), prepared, workdir, timeout=raw_timeout)
        row["n_raw_proposals"] = str(raw["n_raw_proposals"])
        row["n_raw_pass"] = str(raw["n_raw_pass"])
        if row["suite"] == "MT":
            mutants = em.generate_mutants(prepared["put"], workdir / "mutants", workdir)
            mutation = em.mutation_score_of(prepared, mutants, workdir, timeout=8.0)
            row["n_mutants"] = str(mutation.get("n_mutants", 0))
            row["n_killed"] = str(mutation.get("killed", 0))
            row["n_survived"] = str(mutation.get("survived", 0))
            row["n_mutant_timeout"] = str(mutation.get("timeout", 0))
        return row
    finally:
        shutil.rmtree(workdir, ignore_errors=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, nargs="?", default=ROOT / "results" / "results.csv")
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--raw-timeout", type=float, default=15.0)
    args = parser.parse_args()
    rows = list(csv.DictReader(args.input.open(newline="", encoding="utf-8")))
    targets = [i for i, row in enumerate(rows) if row.get("status") == "ok"]
    workroot = ROOT / "results" / "backfill_work"
    workroot.mkdir(parents=True, exist_ok=True)
    import threading
    lock = threading.Lock()
    def write_partial():
        with lock:
            tmp = args.input.with_suffix(args.input.suffix + ".tmp")
            with tmp.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=FIELDS, extrasaction="ignore")
                writer.writeheader()
                writer.writerows(rows)
            tmp.replace(args.input)
    done = 0
    try:
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
            futures = {executor.submit(evaluate_row, rows[i].copy(), workroot, args.raw_timeout): i for i in targets}
            for future in as_completed(futures):
                i = futures[future]
                try:
                    rows[i] = future.result()
                except Exception as exc:
                    print(f"[{done + 1}/{len(targets)}] {rows[i]['run_id']} skipped: {exc}", file=sys.stderr)
                done += 1
                if done % 50 == 0:
                    write_partial()
                    print(f"Backfilled {done}/{len(targets)} OK rows")
    finally:
        write_partial()
        print(f"Backfilled {done} OK rows in {args.input}")


if __name__ == "__main__":
    main()
