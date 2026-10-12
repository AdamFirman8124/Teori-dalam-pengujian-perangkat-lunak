#!/usr/bin/env python3
"""Post-run verification + RQ table + re-score, without any LLM call.

Designed to run at the end of `experiments_codamosa_coverup.ipynb` (a thin
notebook cell calls :func:`post_run`) and as a standalone CLI:

    .venv/bin/python tools/post_run.py --source experiment_results

What it does (steps 3-5 of the runbook):

1. pick the rows/status of the *promoted* run (or the latest candidate when
   promotion was rejected), never silently mixing them;
2. verify data health: status distribution, empty cells, mutation scores that
   are uniformly 0.0, mutant-set conflicts, and per-method/model balance;
3. re-score the on-disk suites with the current harness (free, deterministic);
4. regenerate ``rq1.md`` / ``rq2.md``;
5. print a machine-readable readiness verdict ("siap paper" or not, with reasons).
"""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

METHODS = ("CoverUp", "CODAMOSA")


def _read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def _read_status(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    return data if isinstance(data, list) else []


def resolve_run(source: Path) -> dict:
    """Return the rows/status to report on, plus which run they came from.

    Priority:
      1. ``experiment_results/rows.csv`` when a manifest says it was promoted;
      2. otherwise the newest ``runs/<id>/`` candidate that has rows.csv.
    """
    active_rows = source / "rows.csv"
    active_status = source / "status.json"

    runs_dir = source / "runs"
    candidates = []
    if runs_dir.is_dir():
        candidates = sorted(
            (p for p in runs_dir.iterdir()
             if p.is_dir() and (p / "rows.csv").exists()),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )

    promoted = None
    for cand in candidates:
        manifest_path = cand / "manifest.json"
        if manifest_path.exists():
            try:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            if manifest.get("promoted"):
                promoted = (cand, manifest)
                break

    if promoted is not None:
        run_dir, manifest = promoted
        return {"run_id": run_dir.name, "promoted": True, "manifest": manifest,
                "rows_path": active_rows if active_rows.exists() else run_dir / "rows.csv",
                "status_path": active_status if active_status.exists() else run_dir / "status.json",
                "run_dir": run_dir}

    if candidates:
        run_dir = candidates[0]
        manifest = {}
        mpath = run_dir / "manifest.json"
        if mpath.exists():
            try:
                manifest = json.loads(mpath.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                manifest = {}
        return {"run_id": run_dir.name, "promoted": False, "manifest": manifest,
                "rows_path": run_dir / "rows.csv",
                "status_path": run_dir / "status.json",
                "run_dir": run_dir}

    # Last resort: whatever active files exist.
    return {"run_id": "(active)", "promoted": bool(active_rows.exists()),
            "manifest": {}, "rows_path": active_rows,
            "status_path": active_status, "run_dir": source}


def verify(rows: list[dict], statuses: list[dict]) -> dict:
    """Data-health checks that decide whether the results are paper-ready."""
    reasons: list[str] = []

    counts: dict[str, int] = {}
    for st in statuses:
        counts[st.get("status", "?")] = counts.get(st.get("status", "?"), 0) + 1

    # Empty cells: an OK status with no evaluated row, or vice versa.
    ok_cells = {(st.get("method"), st.get("model"), st.get("dataset"), st.get("task"))
                for st in statuses if st.get("status") == "OK"}
    row_cells = {(r.get("method"), r.get("model") or "", r.get("dataset"), r.get("task"))
                 for r in rows}
    empty = sorted(c for c in ok_cells if c not in row_cells)

    # Mutation scores that are all zero (a harness smell).
    scores = []
    for r in rows:
        val = r.get("mutation_score")
        if val not in ("", None):
            try:
                scores.append(float(val))
            except (TypeError, ValueError):
                pass
    all_zero = bool(scores) and all(s == 0.0 for s in scores)

    # Balance: n per (method, model).
    balance: dict[str, int] = {}
    for r in rows:
        key = "{0}/{1}".format(r.get("method"), r.get("model") or "-")
        balance[key] = balance.get(key, 0) + 1
    nonempty = [v for v in balance.values() if v > 0]
    balanced = bool(nonempty) and max(nonempty) - min(nonempty) <= 1

    conflicts = getattr(verify, "_conflicts", {})

    if counts.get("BLOCKED"):
        reasons.append(f"{counts['BLOCKED']} status BLOCKED")
    if counts.get("INVALID_GENERATED_TEST"):
        reasons.append(f"{counts['INVALID_GENERATED_TEST']} INVALID_GENERATED_TEST")
    if empty:
        reasons.append(f"{len(empty)} sel kosong (OK tanpa baris evaluasi)")
    if all_zero:
        reasons.append("semua mutation_score = 0.0 (harness belum benar / mutan kosong)")
    if not balanced:
        reasons.append(f"n per metode/model tidak seimbang: {balance}")
    if conflicts:
        reasons.append(f"mutant_set_conflicts: {list(conflicts)}")

    return {"status_counts": counts, "empty_cells": empty,
            "all_zero_mutation": all_zero, "balance": balance,
            "balanced": balanced, "mutant_set_conflicts": conflicts,
            "ready": not reasons, "reasons": reasons}


def rescore(source: Path, run_dir: Path) -> dict:
    """Run tools/rescore_existing.py over `source`, write into `run_dir/rescore`."""
    outdir = run_dir / "rescore"
    cmd = [sys.executable, str(ROOT / "tools" / "rescore_existing.py"),
           "--source", str(source), "--outdir", str(outdir)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return {"returncode": proc.returncode,
            "outdir": str(outdir),
            "stdout_tail": "\n".join(proc.stdout.splitlines()[-8:]),
            "stderr_tail": "\n".join(proc.stderr.splitlines()[-4:])}


def _rq_tables(rows_path: Path, run_dir: Path) -> dict:
    """Regenerate rq1.md / rq2.md from a rows.csv using tools/rq_tables.py."""
    cmd = [sys.executable, str(ROOT / "tools" / "rq_tables.py"),
           str(rows_path), str(run_dir)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return {"returncode": proc.returncode,
            "rq1": str(run_dir / "rq1.md"), "rq2": str(run_dir / "rq2.md"),
            "stdout": proc.stdout.strip(), "stderr_tail": "\n".join(proc.stderr.splitlines()[-4:])}


def post_run(source: Path | str = ROOT / "experiment_results",
             *, do_rescore: bool = True, do_tables: bool = True) -> dict:
    """Full steps 3-5 pipeline. Never calls an LLM."""
    source = Path(source)
    run = resolve_run(source)
    rows = _read_rows(run["rows_path"])
    statuses = _read_status(run["status_path"])

    report: dict = {"run": {k: str(v) for k, v in run.items()
                            if k not in {"manifest"}},
                    "n_rows": len(rows), "n_statuses": len(statuses),
                    "promoted": run["promoted"]}

    health = verify(rows, statuses)
    report["health"] = health

    if do_rescore:
        rs = rescore(source, run["run_dir"])
        report["rescore"] = rs
        # Prefer fresh output, but fall back to a previously written rescore
        # rows.csv when the current pass skipped everything (e.g. the generated
        # suites were moved away and nothing could be measured).
        scored_path = Path(rs["outdir"]) / "rows.csv"
        if scored_path.exists() and _read_rows(scored_path):
            report["rescored_rows"] = len(_read_rows(scored_path))
            report["rescore_stale"] = rs["returncode"] != 0
    else:
        report["rescore"] = {"skipped": True}

    if do_tables:
        report["tables"] = _rq_tables(run["rows_path"], run["run_dir"])
    else:
        report["tables"] = {"skipped": True}

    # Final verdict: the re-scored rows are the authoritative measurement when
    # rescoring succeeded, because they were produced by the current harness.
    # Status distribution (BLOCKED/INVALID) still comes from the run itself.
    rs_path = Path(report["rescore"].get("outdir", "")) / "rows.csv" \
        if not report.get("rescore", {}).get("skipped", True) else None
    if rs_path is not None and rs_path.exists():
        rs_rows = _read_rows(rs_path)
        report["health_scored"] = verify(rs_rows, statuses)
        report["verdict_source"] = "rescored"
        report["ready"] = report["health_scored"]["ready"]
    else:
        report["verdict_source"] = "raw"
        report["ready"] = health["ready"]
    return report


def _print_report(report: dict) -> None:
    run = report["run"]
    print("=" * 68)
    print("POST-RUN REPORT")
    print("=" * 68)
    print(f"run_id    : {run.get('run_id')}")
    print(f"promoted  : {report['promoted']}")
    print(f"rows      : {report['n_rows']} | statuses: {report['n_statuses']}")
    h = report["health"]
    print(f"status    : {h['status_counts']}")
    print(f"balanced  : {h['balanced']} | balance={h['balance']}")
    print(f"mut.scores: all_zero={h['all_zero_mutation']}")
    if h["empty_cells"]:
        print(f"empty     : {len(h['empty_cells'])} -> {h['empty_cells'][:6]}")
    rs = report.get("rescore", {})
    if rs.get("skipped"):
        print("rescore   : skipped")
    else:
        print(f"rescore   : rc={rs.get('returncode')} -> {rs.get('outdir')} "
              f"({report.get('rescored_rows', '?')} rows)")
    tb = report.get("tables", {})
    if tb.get("skipped"):
        print("tables    : skipped")
    else:
        print(f"tables    : rc={tb.get('returncode')} -> {tb.get('rq1')}, {tb.get('rq2')}")
    print("-" * 68)
    print(f"verdict on: {report.get('verdict_source', 'raw')} rows")
    if report.get("rescore_stale"):
        print("WARNING   : rescore pass found nothing; using a stale rescore rows.csv")
    verdict_health = report.get("health_scored") or h
    if report["ready"]:
        print("VERDICT   : SIAP PAPER (data yang diukur sudah sehat)")
    else:
        print("VERDICT   : BELUM SIAP PAPER")
        for reason in verdict_health["reasons"]:
            print(f"  - {reason}")
    print("=" * 68)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", default=str(ROOT / "experiment_results"))
    ap.add_argument("--no-rescore", action="store_true")
    ap.add_argument("--no-tables", action="store_true")
    ap.add_argument("--json", action="store_true", help="print report as JSON")
    args = ap.parse_args()

    report = post_run(Path(args.source), do_rescore=not args.no_rescore,
                      do_tables=not args.no_tables)
    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        _print_report(report)
    return 0 if report["ready"] else 2


if __name__ == "__main__":
    raise SystemExit(main())



