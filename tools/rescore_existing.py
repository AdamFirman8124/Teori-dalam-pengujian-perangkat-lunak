#!/usr/bin/env python3
"""Re-score already-generated suites with the patched harness -- NO LLM calls.

The shipped ``experiment_results/rows.csv`` predates two harness fixes:

  * ``mutation_score_of`` ran import-style suites with the real PUT shadowing
    the mutant, so every mutant "survived" and the score was 0.0;
  * ``pass_rate_of`` let pytest collect foreign files from a shared parent
    directory, inflating ``n_tests``.

This tool takes the suites that are still on disk (``experiment_results/work``)
and re-measures them with the current ``src/eval_metrics.py``.  It never calls a
model, so it is free and deterministic.

Usage
  .venv/bin/python tools/rescore_existing.py \\
      --source experiment_results \\
      --outdir experiment_results/rescore_<tag>
"""
from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
from src import eval_metrics as em  # noqa: E402

METHOD_DIRS = {"CODAMOSA": "codamosa", "CoverUp": "coverup"}


def _suites_for(work_root: Path, method: str, model: str, dataset: str,
                task: str) -> list[Path]:
    """Locate the generated suite files for one (method, model, dataset, task)."""
    slug = model.replace("/", "_")
    if method == "CODAMOSA":
        base = work_root / "codamosa" / slug / dataset / str(task) / "output"
        if not base.is_dir():
            base = work_root / "codamosa" / model / dataset / str(task) / "output"
        if not base.is_dir():
            return []
        return sorted(
            p for p in base.rglob("test_script_*.py")
            if not p.name.endswith("_failing.py")
            and not p.name.endswith("_failing_no_metadata.py")
        )
    base = work_root / "coverup" / slug / dataset / str(task) / "tests"
    if not base.is_dir():
        return []
    return sorted(base.glob("test_coverup_*.py"))


def rescore(source: Path, outdir: Path, datasets: list[str]) -> int:
    rows_path = source / "rows.csv"
    if not rows_path.exists():
        print("no rows.csv under", source, file=sys.stderr)
        return 1
    work_root = source / "work"

    with rows_path.open(encoding="utf-8", newline="") as handle:
        old_rows = list(csv.DictReader(handle))

    outdir.mkdir(parents=True, exist_ok=True)
    rescore_work = outdir / "work"
    rescore_work.mkdir(exist_ok=True)

    new_rows: list[dict] = []
    skipped = 0
    for row in old_rows:
        dataset = row.get("dataset", "")
        task = row.get("task", "")
        method = row.get("method", "")
        model = row.get("model", "") or ""
        if datasets and dataset not in datasets:
            continue
        suite_method = method if method in METHOD_DIRS else "CoverUp"
        suites = _suites_for(work_root, suite_method, model, dataset, task)
        # Baselines have no work dir; keep their existing numbers untouched.
        if not suites:
            if method not in METHOD_DIRS:
                new_rows.append(row)
            else:
                skipped += 1
                print(f"skip {method}/{model}/{dataset}/{task}: no suite on disk")
            continue
        valid = [p for p in suites if em.suite_validity(p)[0]]
        if not valid:
            skipped += 1
            print(f"skip {method}/{model}/{dataset}/{task}: suites now invalid")
            continue
        layout = em.LAYOUTS[dataset](str(task))
        measured = em.evaluate(dataset, str(task), valid, method,
                               wall_time_s=_float(row.get("wall_time_s")),
                               cost_usd=_float(row.get("cost_usd")),
                               workroot=rescore_work)
        measured["model"] = model
        if row.get("generator_ok") is not None:
            measured["generator_ok"] = row["generator_ok"]
        new_rows.append(measured)
        print(f"rescored {method}/{model}/{dataset}/{task}: "
              f"MS={measured.get('mutation_score')} "
              f"n_tests={measured.get('n_tests')} "
              f"pass={measured.get('pass_rate')}")

    shutil.rmtree(rescore_work, ignore_errors=True)

    if not new_rows:
        print("nothing rescored", file=sys.stderr)
        return 1
    cols = sorted({k for r in new_rows for k in r})
    with (outdir / "rows.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=cols, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(new_rows)
    (outdir / "rescore_manifest.json").write_text(
        json.dumps({"source": str(source), "rows": len(new_rows),
                    "skipped": skipped, "datasets": datasets}, indent=2) + "\n",
        encoding="utf-8")
    print(f"wrote {outdir / 'rows.csv'} ({len(new_rows)} rows, {skipped} skipped)")
    return 0


def _float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default="experiment_results")
    parser.add_argument("--outdir", default="experiment_results/rescore")
    parser.add_argument("--datasets", default="",
                        help="comma-separated subset, e.g. HumanEval")
    args = parser.parse_args()
    datasets = [d for d in args.datasets.split(",") if d]
    return rescore(Path(args.source).resolve(), Path(args.outdir).resolve(),
                   datasets)


if __name__ == "__main__":
    raise SystemExit(main())
