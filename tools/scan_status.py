#!/usr/bin/env python3
"""Status scanner for CoverUp / CodaMOSA experiment runs.

Success is decided per task by looking for the artefacts each method ACTUALLY
produces, because the two methods write to different directories:

  CodaMOSA : <task>/output/test_script_*.py
  CoverUp  : <task>/tests/test_coverup_*.py

A task is never reported as failed merely because ``output/`` is empty; the
scanner checks ``output/`` OR ``tests/``.

It also collects evaluation metrics (coverage, pass rate, mutation score, wall
time, cost) from any evaluation log found inside the results directory, and
writes everything into a NEW directory so legacy artefacts are never mixed in.

Usage
    .venv/bin/python tools/scan_status.py <results_dir> [-o <out_dir>]
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import statistics
import sys
from pathlib import Path

CODAMOSA_GLOB = "output/test_script_*.py"
COVERUP_GLOB = "tests/test_coverup_*.py"

METRIC_KEYS = {
    "line_pct": ("line_pct", "coverage", "line_coverage", "cov_pct"),
    "branch_pct": ("branch_pct", "branch_coverage"),
    "pass_rate": ("pass_rate", "passrate", "pass_pct"),
    "mutation_score": ("mutation_score", "ms", "mutation_pct"),
    "wall_time_s": ("wall_time_s", "wall_time", "duration_s", "elapsed_s"),
    "cost_usd": ("cost_usd", "cost", "total_cost"),
}
TASK_ID_KEYS = ("task", "task_id", "id")
DATASET_KEYS = ("dataset", "suite", "data")
METHOD_KEYS = ("method", "generator")
MODEL_KEYS = ("model", "model_name", "backbone")
EVAL_GLOBS = ("**/rows.csv", "**/eval*.jsonl", "**/eval*.json",
              "**/metrics*.jsonl", "**/metrics*.json")


def _first(d: dict, keys):
    for k in keys:
        v = d.get(k)
        if v is not None and str(v).strip() != "":
            return str(v).strip()
    return None


def _num(value):
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        m = re.search(r"-?\d+(?:\.\d+)?", value)
        if m:
            return float(m.group())
    return None


def discover_task_dirs(results_dir: Path):
    """Return (method, model, dataset, task, path) for each task directory.

    Layout written by the notebook: work/<method>/<model>/<dataset>/<task>/.
    """
    found = []
    if not results_dir.is_dir():
        return found
    for cand in sorted(p for p in results_dir.rglob("*") if p.is_dir()):
        try:
            rel = cand.relative_to(results_dir)
        except ValueError:
            continue
        parts = rel.parts
        if len(parts) < 4:
            continue
        method, model, dataset, task = parts[0], parts[1], parts[-2], parts[-1]
        if not task or task.startswith("."):
            continue
        if not any(cand.glob(CODAMOSA_GLOB)) and not any(cand.glob(COVERUP_GLOB)) \
                and not list(cand.glob("*.log")) and not list(cand.glob("*.json")):
            # Still record it: an empty task dir is itself a signal (BLOCKED).
            pass
        found.append((method, model, dataset, task, cand))
    return found


def scan_task(method_dir: Path) -> dict:
    """Artefact census for one task directory."""
    codamosa = sorted(method_dir.glob(CODAMOSA_GLOB))
    coverup = sorted(method_dir.glob(COVERUP_GLOB))
    rel = lambda p: str(p.relative_to(method_dir))
    if codamosa and coverup:
        source = "both"
    elif codamosa:
        source = "codamosa"
    elif coverup:
        source = "coverup"
    else:
        source = "none"
    return {
        "codamosa_files": [rel(p) for p in codamosa],
        "coverup_files": [rel(p) for p in coverup],
        "n_codamosa_files": len(codamosa),
        "n_coverup_files": len(coverup),
        "n_output_dir_py": len(list(method_dir.glob("output/*.py"))),
        "n_tests_dir_py": len(list(method_dir.glob("tests/*.py"))),
        "has_coverup_log": bool(list(method_dir.glob("coverup*.log"))),
        "ok": bool(codamosa or coverup),
        "source": source,
    }

def discover_task_dirs(results_dir: Path):
    """Find task dirs in new and archived layouts."""
    methods = {"codamosa", "coverup"}
    datasets = {"humaneval", "refactory"}
    found, seen = [], set()
    for cand in sorted(p for p in results_dir.rglob("*") if p.is_dir()):
        try:
            rel = cand.relative_to(results_dir)
        except ValueError:
            continue
        parts = list(rel.parts)
        low = [p.lower() for p in parts]
        mi = next((i for i, p in enumerate(low) if p in methods), None)
        if mi is None or mi + 3 >= len(parts):
            continue
        di = next((i for i in range(mi + 1, len(parts)) if low[i] in datasets), None)
        if di is None or di + 1 != len(parts) - 1:
            continue
        key = (parts[mi], parts[mi + 1], parts[di], parts[di + 1])
        if key not in seen:
            seen.add(key)
            found.append((key[0], key[1], key[2], key[3], cand))
    return found


def _read_records(path: Path):
    """Yield dicts from CSV, JSONL, or common JSON containers."""
    try:
        if path.suffix.lower() == ".csv":
            with path.open(newline="", errors="ignore") as fh:
                yield from csv.DictReader(fh)
        elif path.suffix.lower() == ".jsonl":
            for line in path.read_text(errors="ignore").splitlines():
                if line.strip().startswith("{"):
                    try:
                        obj = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if isinstance(obj, dict):
                        yield obj
        else:
            obj = json.loads(path.read_text(errors="ignore"))
            if isinstance(obj, list):
                for x in obj:
                    if isinstance(x, dict):
                        yield x
            elif isinstance(obj, dict):
                for k in ("rows", "records", "results", "tasks"):
                    if isinstance(obj.get(k), list):
                        for x in obj[k]:
                            if isinstance(x, dict):
                                yield x
                        break
    except (OSError, ValueError, csv.Error) as exc:
        print(f"warning: cannot parse {path}: {exc}", file=sys.stderr)

def evaluation_index(results_dir: Path):
    """Index metrics by (method, model, dataset, task), best effort."""
    idx = {}
    patterns = ("**/rows.csv", "**/eval*.json", "**/eval*.jsonl",
                "**/metric*.json", "**/metric*.jsonl", "**/metrics*.json",
                "**/metrics*.jsonl")
    paths = {p for pattern in patterns for p in results_dir.glob(pattern)}
    for path in sorted(paths):
        for rec in _read_records(path):
            task = _first(rec, TASK_ID_KEYS)
            if not task:
                continue
            method = _first(rec, METHOD_KEYS) or "unknown"
            model = _first(rec, MODEL_KEYS) or "unknown"
            dataset = _first(rec, DATASET_KEYS) or "unknown"
            metrics = {}
            for name, aliases in METRIC_KEYS.items():
                for alias in aliases:
                    if alias in rec:
                        value = _num(rec[alias])
                        if value is not None:
                            metrics[name] = value
                            break
            idx[(method.lower(), model, dataset, str(task))] = metrics
    return idx, len(paths)


def metric_for(index, method, model, dataset, task):
    keys = [(method.lower(), model, dataset, task),
            (method.lower(), "unknown", dataset, task),
            ("unknown", model, dataset, task),
            ("unknown", "unknown", dataset, task)]
    for key in keys:
        if key in index:
            return index[key]
    return {}


def _mean(values):
    return round(statistics.fmean(values), 4) if values else None


def make_summary(records):
    groups = {}
    for rec in records:
        key = (rec["method"], rec["model"], rec["dataset"])
        g = groups.setdefault(key, {"tasks": 0, "tasks_with_tests": 0,
                                    "codamosa_files": 0, "coverup_files": 0,
                                    "eval_logs": 0, "values": {}})
        g["tasks"] += 1
        g["tasks_with_tests"] += int(rec["ok"])
        g["codamosa_files"] += rec["n_codamosa_files"]
        g["coverup_files"] += rec["n_coverup_files"]
        g["eval_logs"] += rec["n_eval_logs"]
        for name, value in rec.get("metrics", {}).items():
            g["values"].setdefault(name, []).append(value)
    result = {}
    for key, g in groups.items():
        row = {k: v for k, v in g.items() if k != "values"}
        row["success_rate"] = round(100 * g["tasks_with_tests"] / g["tasks"], 2)
        for name, values in g["values"].items():
            row[name + "_mean"] = _mean(values)
            row[name + "_n"] = len(values)
        result["|".join(key)] = row
    return result


def summary_markdown(summary):
    cols = ["method", "model", "dataset", "tasks", "tasks_with_tests",
            "success_rate", "codamosa_files", "coverup_files", "eval_logs",
            "line_pct_mean", "pass_rate_mean", "mutation_score_mean",
            "wall_time_s_mean", "cost_usd_mean"]
    lines = ["| " + " | ".join(cols) + " |",
             "|" + "|".join("---" for _ in cols) + "|"]
    for key in sorted(summary):
        method, model, dataset = key.split("|", 2)
        row = [method, model, dataset]
        row += [summary[key].get(c, "-") for c in cols[3:]]
        lines.append("| " + " | ".join(str(x) if x is not None else "-"
                                           for x in row) + " |")
    return "\n".join(lines)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results_dir", type=Path)
    parser.add_argument("-o", "--out", type=Path, required=True,
                        help="new directory for scanner output")
    args = parser.parse_args()
    results = args.results_dir.resolve()
    out = args.out.resolve()
    if not results.is_dir():
        print(f"results directory not found: {results}", file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)
    eval_idx, eval_files = evaluation_index(results)
    records = []
    for method, model, dataset, task, path in discover_task_dirs(results):
        data = scan_task(path)
        data.update({"method": method, "model": model, "dataset": dataset,
                     "task": task, "path": str(path)})
        data["n_eval_logs"] = len(list(path.glob("*eval*.log")))
        data["n_eval_logs"] += len(list(path.glob("*pytest*.log")))
        data["n_eval_logs"] += len(list(path.glob("*docker*.log")))
        data["metrics"] = metric_for(eval_idx, method, model, dataset, task)
        records.append(data)
    records.sort(key=lambda r: (r["method"], r["model"], r["dataset"], r["task"]))
    summary = make_summary(records)
    (out / "status.json").write_text(json.dumps(records, indent=2))
    (out / "summary.json").write_text(json.dumps(summary, indent=2))
    (out / "summary.md").write_text("# Experiment result scan\n\n" +
                                    summary_markdown(summary) + "\n")
    columns = ["method", "model", "dataset", "task", "ok", "source",
               "n_codamosa_files", "n_coverup_files", "n_output_dir_py",
               "n_tests_dir_py", "n_eval_logs", "line_pct", "branch_pct",
               "pass_rate", "mutation_score", "wall_time_s", "cost_usd", "path"]
    with (out / "status.csv").open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            writer.writerow({**record, **record.get("metrics", {})})
    print(f"evaluation files indexed: {eval_files}")
    print(f"tasks scanned: {len(records)}")
    print(f"tasks with generated tests: {sum(bool(r['ok']) for r in records)}")
    print(summary_markdown(summary))
    print(f"wrote: {out / 'status.json'}")
    print(f"wrote: {out / 'status.csv'}")
    print(f"wrote: {out / 'summary.json'}")
    print(f"wrote: {out / 'summary.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


