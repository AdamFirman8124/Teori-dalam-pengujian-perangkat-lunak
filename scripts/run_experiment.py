#!/usr/bin/env python3
"""Run the CoverUp experiment over HumanEval + Refactory and emit RQ1/RQ2 tables.

Usage
  .venv/bin/python run_experiment.py --methods coverup            # RQ1/RQ2, needs LLM
  .venv/bin/python run_experiment.py --methods all --limit 5      # incl. baselines
  .venv/bin/python run_experiment.py --dataset Refactory           # one dataset

Output
  results/rows.csv   one row per (dataset, task, method) with every metric
  results/rq1.md     Coverage / Pass Rate / Mutation Score per method
  results/rq2.md     Coverage / Pass Rate / time / cost per backbone
"""
from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from src import eval_metrics as em  # noqa: E402

METRIC_COLS = ["line_pct", "branch_pct", "pass_rate", "mutation_score",
               "wall_time_s", "cost_usd"]


def backbone_name(model: str | None) -> str | None:
    """Collapse LiteLLM transport prefixes so RQ2 groups by the real backbone.

    e.g. ``openai/gpt-5.5`` -> ``gpt-5.5``.  Returns None when there is no model
    column so callers can fall back to the method name (baselines).
    """
    if not model:
        return None
    return model.replace("openai/", "", 1) if model.startswith("openai/") else model


def load_api_key() -> None:
    """Load .env next to this file so CLI runs see the same config as the notebook."""
    try:
        from dotenv import load_dotenv

        load_dotenv(Path(__file__).resolve().parent.parent / "config" / ".env", override=False)
    except ImportError:
        pass
    # CoverUp/litellm historically honours OPENAI_API_BASE; keep it in sync.
    base = os.environ.get("OPENAI_BASE_URL")
    if base and not os.environ.get("OPENAI_API_BASE"):
        os.environ["OPENAI_API_BASE"] = base
    os.environ.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")


def litellm_model_name(model: str) -> str:
    """Use litellm's OpenAI-compatible provider for custom API-base backends."""
    if os.environ.get("OPENAI_BASE_URL") and "/" not in model:
        return f"openai/{model}"
    return model


def preflight_llm(model: str) -> tuple[bool, str]:
    """One cheap chat call so a quota/key problem fails fast, not after retries."""
    load_api_key()
    if "OPENAI_API_KEY" not in os.environ:
        return False, "OPENAI_API_KEY is not set in the environment"
    try:
        import litellm
    except ImportError:
        return False, "litellm package not installed"
    try:
        litellm.completion(
            model=litellm_model_name(model), max_tokens=1, timeout=60,
            messages=[{"role": "user", "content": "reply with the single letter ok"}])
        return True, "ok"
    except Exception as e:  # noqa: BLE001 - report provider error verbatim
        return False, "{}: {}".format(type(e).__name__, str(e)[:300])


def measure_baseline(job: tuple[str, str, str, str]) -> dict | None:
    """Evaluate one shipped baseline suite; module-level so it can be pickled."""
    ds, tid, suite_name, workroot = job
    tests = em.LAYOUTS[ds](tid)["suites"].get(suite_name) or []
    if not tests:
        return None
    return em.evaluate(ds, tid, tests, suite_name,
                       workroot=Path(workroot) if workroot else None)


def aggregate(rows: list[dict]) -> dict:
    """Mean per metric over the tasks that produced a value (with n)."""
    agg: dict[str, dict] = {}
    for col in METRIC_COLS:
        vals = [r[col] for r in rows
                if isinstance(r.get(col), (int, float)) and r.get(col) is not None]
        agg[col] = {"mean": round(statistics.fmean(vals), 2) if vals else None,
                    "n": len(vals)}
    agg["tasks"] = len({(r["dataset"], r["task"]) for r in rows})
    agg["total_time_s"] = round(sum(r["wall_time_s"] for r in rows
                                    if isinstance(r.get("wall_time_s"), (int, float))), 2)
    agg["total_cost_usd"] = round(sum(r["cost_usd"] for r in rows
                                      if isinstance(r.get("cost_usd"), (int, float))), 4)
    return agg


def table(by_method: dict[str, list[dict]], title: str, cols: list[str],
          first_col: str = "method") -> str:
    head = [first_col, "n_tasks"] + [c for c in cols]
    lines = [f"## {title}", "", "| " + " | ".join(head) + " |",
             "|" + "|".join(["---"] * len(head)) + "|"]
    for method, rows in by_method.items():
        agg = aggregate(rows)
        cells = [method, str(agg["tasks"])]
        for c in cols:
            if c == "wall_time_s":
                cells.append(f"{agg['total_time_s']} s total / "
                             f"{agg[c]['mean']} s avg" if agg[c]["mean"] is not None else "-")
            elif c == "cost_usd":
                cells.append(f"${agg['total_cost_usd']} total" if agg[c]["mean"] is not None else "-")
            else:
                v = agg[c]["mean"]
                cells.append(f"{v}%" if v is not None else "-")
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", choices=["HumanEval", "Refactory", "both"], default="both")
    ap.add_argument("--limit", type=int, help="only the first N tasks (pilot runs)")
    ap.add_argument("--tasks", help="explicit comma-separated task ids")
    ap.add_argument("--methods", default="coverup",
                    help="coverup, or baselines, or all (comma list allowed)")
    ap.add_argument(
        "--model", default=None,
        help="model accepted by CoverUp/litellm; defaults to first COVERUP_MODELS entry")
    ap.add_argument("--timeout", type=int, default=900, help="per-task CoverUp timeout (s)")
    ap.add_argument("--dry-run", action="store_true",
                    help="pass --dry-run through to CoverUp (no LLM calls)")
    ap.add_argument("--outdir", default="results")
    ap.add_argument("--jobs", type=int, default=1,
                    help="tasks to evaluate in parallel (baselines only; keep 1 for CoverUp)")
    args = ap.parse_args()
    load_api_key()
    if args.model is None:
        configured = [m.strip() for m in os.environ.get("COVERUP_MODELS", "").split(",") if m.strip()]
        args.model = configured[0] if configured else "gpt-4o"

    methods = [m.strip() for m in args.methods.split(",") if m.strip()]
    if "all" in methods:
        methods = [m for m in methods if m != "all"] + ["coverup", "baselines"]
    if "coverup" in methods and not args.dry_run:
        ok, why = preflight_llm(args.model)
        if not ok:
            print("LLM preflight FAILED - CoverUp cannot run: " + why, file=sys.stderr)
            print("Fix the API access, or run the baselines only: "
                  "--methods baselines", file=sys.stderr)
            return 3
        print("LLM preflight ok ({})".format(args.model))
    datasets = ["HumanEval", "Refactory"] if args.dataset == "both" else [args.dataset]
    outdir = Path(args.outdir)
    outdir.mkdir(exist_ok=True)
    workroot = outdir / "work"
    workroot.mkdir(exist_ok=True)

    def do_coverup(ds: str, tid: str) -> dict:
        layout = em.LAYOUTS[ds](tid)
        task_work = workroot / ds / str(tid)
        task_work.mkdir(parents=True, exist_ok=True)
        rr = em.run_coverup(Path(layout["put"]), task_work / "tests",
                            task_work, model=args.model, timeout=args.timeout,
                            extra=("--dry-run",) if args.dry_run else ())
        row = em.evaluate(ds, tid, [Path(p) for p in rr.generated_tests],
                          "CoverUp", wall_time_s=rr.wall_time_s, cost_usd=rr.cost_usd,
                          workroot=workroot)
        row["coverup_ok"] = rr.ok
        row["coverup_GFU_R"] = f"{rr.good}/{rr.failed}/{rr.useless}/{rr.retries}"
        row["prompt_tokens"] = rr.prompt_tokens
        row["completion_tokens"] = rr.completion_tokens
        row["total_tokens"] = rr.total_tokens
        row["calls_with_usage"] = rr.calls_with_usage
        row["n_tests_files"] = len(rr.generated_tests)
        if rr.error:
            row["error"] = rr.error[:300].replace("\n", " ")
        return row

    rows: list[dict] = []
    rows_path = outdir / "rows.csv"
    jobs: list[tuple[str, str, str, str]] = []
    for ds in datasets:
        ids = args.tasks.split(",") if args.tasks else em.task_ids(ds, args.limit)
        for tid in ids:
            if "coverup" in methods:
                row = do_coverup(ds, tid)
                rows.append(row)
                print(json.dumps(row), flush=True)
            if "baselines" in methods:
                for suite_name in em.LAYOUTS[ds](tid)["suites"]:
                    jobs.append((ds, tid, suite_name, str(workroot)))

    if jobs:
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor(max_workers=max(1, args.jobs)) as ex:
            for row in ex.map(measure_baseline, jobs):
                if row:
                    rows.append(row)
                    print(json.dumps(row), flush=True)

    if not rows:
        print("no rows produced", file=sys.stderr)
        return 1

    import csv
    cols = ["dataset", "task", "method", "put", "line_pct", "branch_pct", "pass_rate",
            "mutation_score", "killed", "survived", "problematic", "n_mutants",
            "n_tests", "n_passed", "n_tests_files", "wall_time_s", "cost_usd",
            "prompt_tokens", "completion_tokens", "total_tokens", "calls_with_usage",
            "coverup_ok", "coverup_GFU_R", "error"]
    with rows_path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    # RQ1 groups by METHOD (CoverUp vs baselines); RQ2 groups by BACKBONE/model
    # (which LLM/backbone yields the best coverage/pass-rate per unit time & cost).
    by_method: dict[str, list[dict]] = {}
    for r in rows:
        by_method.setdefault(r["method"], []).append(r)
    by_backbone: dict[str, list[dict]] = {}
    for r in rows:
        backbone = backbone_name(r.get("model")) or r.get("method") or "unknown"
        by_backbone.setdefault(backbone, []).append(r)
    rq1 = table(by_method, "RQ1 - Main performance (Coverage / Pass Rate / Mutation Score)",
                ["line_pct", "pass_rate", "mutation_score"])
    rq2 = table(by_backbone, "RQ2 - Backbone (Coverage / Pass Rate / Time / Cost)",
                ["line_pct", "pass_rate", "wall_time_s", "cost_usd"],
                first_col="backbone")
    (outdir / "rq1.md").write_text(rq1)
    (outdir / "rq2.md").write_text(rq2)
    print("\n" + rq1 + "\n" + rq2)
    print(f"wrote {rows_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
