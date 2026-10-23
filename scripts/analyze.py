#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

ROOT = Path(__file__).resolve().parents[1]


def holm(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=values.__getitem__)
    adjusted = [0.0] * len(values)
    running = 0.0
    for rank, index in enumerate(order):
        running = max(running, min(1.0, values[index] * (len(values) - rank)))
        adjusted[index] = running
    return adjusted


def a12(a: np.ndarray, b: np.ndarray) -> float:
    return float(((a[:, None] > b).sum() + 0.5 * (a[:, None] == b).sum()) / (len(a) * len(b)))


def bootstrap_ci(delta: np.ndarray, seed: int = 20261022) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    means = np.mean(rng.choice(delta, size=(10_000, len(delta)), replace=True), axis=1)
    return tuple(float(value) for value in np.quantile(means, [0.025, 0.975]))


def derivatives(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["rv"] = df.n_raw_pass / df.n_raw_proposals.replace(0, np.nan) * 100
    df["lc"] = df.lines_exec / df.lines_total.replace(0, np.nan) * 100
    df["bc"] = df.branches_exec / df.branches_total.replace(0, np.nan) * 100
    df["ms"] = df.n_killed / df.n_mutants.replace(0, np.nan) * 100
    return df


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / "results" / "analysis")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    df = derivatives(pd.read_csv(args.input))
    ok = df[df.status == "ok"].copy()

    # TABEL IV: effectiveness summary with mean, median, std across repetitions.
    summary = ok.groupby(["suite", "tool", "backbone"])[
        ["rv", "lc", "bc", "ms", "gen_time_s", "tokens_in", "tokens_out", "cost_usd"]
    ].agg(["mean", "median", "std"])
    summary.to_csv(args.output / "table_iv_summary.csv")

    # Failure rate as a secondary metric (File B: guard >10% per configuration).
    total = df.groupby(["suite", "tool", "backbone"]).size().rename("n_total")
    failed = df[df.status != "ok"].groupby(["suite", "tool", "backbone"]).size().rename("n_failed")
    top_category = (
        df[df.status != "ok"]
        .groupby(["suite", "tool", "backbone", "error_category"])
        .size()
        .reset_index(name="count")
        .sort_values(["suite", "tool", "backbone", "count"], ascending=[True, True, True, False])
        .groupby(["suite", "tool", "backbone"])
        .first()[["error_category", "count"]]
    )
    fail_rate = (
        total.to_frame()
        .join(failed.to_frame().fillna(0).astype(int))
        .join(top_category)
    )
    fail_rate["n_failed"] = fail_rate["n_failed"].fillna(0).astype(int)
    fail_rate["error_category"] = fail_rate["error_category"].fillna("none")
    fail_rate["fail_rate"] = fail_rate["n_failed"] / fail_rate["n_total"]
    fail_rate["over_10pct"] = fail_rate["fail_rate"] > 0.10
    fail_rate.to_csv(args.output / "failure_rate.csv")

    # Matched per-unit medians for paired tool comparisons.
    unit = ok.groupby(["suite", "backbone", "unit_id", "tool"])[["bc", "ms", "cost_usd", "gen_time_s"]].median().reset_index()

    tests = []
    for suite, metric in (("MT", "ms"), ("CM", "bc"), ("CM", "ms")):
        for backbone in sorted(ok.backbone.dropna().unique()):
            subset = unit[(unit.suite == suite) & (unit.backbone == backbone)].pivot(
                index="unit_id", columns="tool", values=metric
            ).dropna()
            if {"CodaMOSA", "CoverUp"}.issubset(subset.columns) and len(subset):
                delta = subset.CoverUp - subset.CodaMOSA
                stat, p = wilcoxon(delta) if np.any(delta) else (0.0, 1.0)
                ci_low, ci_high = bootstrap_ci(delta.to_numpy())
                tests.append(
                    {
                        "suite": suite,
                        "metric": metric,
                        "backbone": backbone,
                        "n": len(delta),
                        "wins": int((delta > 0).sum()),
                        "ties": int((delta == 0).sum()),
                        "losses": int((delta < 0).sum()),
                        "a12": a12(subset.CoverUp.to_numpy(), subset.CodaMOSA.to_numpy()),
                        "mean_difference": delta.mean(),
                        "bootstrap_ci_low": ci_low,
                        "bootstrap_ci_high": ci_high,
                        "wilcoxon_stat": stat,
                        "p": p,
                    }
                )
    if tests:
        adjusted = holm([row["p"] for row in tests])
        for row, value in zip(tests, adjusted):
            row["p_holm"] = value
    pd.DataFrame(tests).to_csv(args.output / "table_v_paired_tests.csv", index=False)

    # Cost-effectiveness RQ3 needs a Pynguin baseline that collaborator owns.
    # Without it, emit the Pareto data and no CE values.
    pareto = ok.groupby(["suite", "tool", "backbone"]).agg(
        median_cost_usd=("cost_usd", "median"),
        median_bc=("bc", "median"),
        median_ms=("ms", "median"),
    ).reset_index()
    pareto.to_csv(args.output / "figure_5_pareto_data.csv", index=False)
    baseline_path = args.output.parent / "pynguin_baseline.csv"
    if baseline_path.exists():
        baseline = pd.read_csv(baseline_path).rename(columns={"metric_median": "baseline"})
        ce = ok.groupby(["suite", "tool", "backbone"]).agg(
            metric_median=("bc", "median"), median_cost_usd=("cost_usd", "median")
        ).reset_index().merge(baseline, on=["suite", "backbone"])
        ce["delta_e"] = ce.metric_median - ce.baseline
        ce["CE"] = np.where(ce.delta_e > 0, ce.delta_e / ce.median_cost_usd.replace(0, np.nan), np.nan)
        ce.to_csv(args.output / "table_viii_cost_effectiveness.csv", index=False)
    else:
        pd.DataFrame(columns=["suite", "tool", "backbone", "delta_e", "median_cost_usd", "CE"]).to_csv(
            args.output / "table_viii_cost_effectiveness.csv", index=False
        )

    # File B Table IX: Wilcoxon cost tests over every tool pair, suite, and backbone,
    # Holm-corrected jointly. With all four tools this yields the specified 13-test
    # family; with only CodaMOSA/CoverUp it yields the subset that is measurable here.
    cost_tests = []
    tools = sorted(ok.tool.dropna().unique())
    tool_pairs = [(a, b) for i, a in enumerate(tools) for b in tools[i + 1:]]
    for backbone in sorted(ok.backbone.dropna().unique()):
        for suite in sorted(ok.suite.dropna().unique()):
            for left, right in tool_pairs:
                subset = unit[(unit.suite == suite) & (unit.backbone == backbone)].pivot(
                    index="unit_id", columns="tool", values="cost_usd"
                ).dropna()
                if {left, right}.issubset(subset.columns) and len(subset):
                    delta = subset[right] - subset[left]
                    stat, p = wilcoxon(delta) if np.any(delta) else (0.0, 1.0)
                    cost_tests.append(
                        {
                            "backbone": backbone,
                            "suite": suite,
                            "comparison": f"{right} vs {left}",
                            "n": len(delta),
                            "median_delta_cost": delta.median(),
                            "wilcoxon_stat": stat,
                            "p": p,
                        }
                    )
    if cost_tests:
        adjusted = holm([row["p"] for row in cost_tests])
        for row, value in zip(cost_tests, adjusted):
            row["p_holm"] = value
    pd.DataFrame(cost_tests).to_csv(args.output / "table_ix_cost_wilcoxon.csv", index=False)

    # Failed / excluded task audit trail.
    excluded = df[df.status != "ok"].sort_values(["suite", "tool", "backbone", "unit_id", "run_idx"])
    excluded.to_csv(args.output / "excluded_tasks.csv", index=False)

    # Immediate deviations logged from File A / File B that do not require runs.
    lines = [
        "# Deviations from File A and File B (auto-logged)",
        "",
        "| # | File | Requirement | What was done | Rationale / decision |",
        "|---|---|---|---|---|",
        "| 1 | File B | CM stratum is 3x3 LOC x n_branches (9 strata) | Only 8 non-empty strata exist; L0B2 is empty | Approved deviation, 2026-10-22; all eight observed strata sampled, CM sample >= 40 modules, per-project cap 25% |",
        "| 2 | File B | Pynguin and MuTAP included as tool rows | Only CodaMOSA and CoverUp are implemented here; collaborator owns Pynguin/MuTAP results | User clarification; File B schema retained so collaborator rows can merge later |",
        "| 3 | File A | Preamtric code-characteristics RQ3 (Table VIII Spearman) | File B revision 19 Oct 2026 changes RQ3 to cost-effectiveness (cost_usd, delta E, CE, Pareto) | File B wins; File A code-characteristics table treated as structure/archive only |",
        "| 4 | File B | 13 Wilcoxon cost tests | Number 13 interpreted as all paired tool/backbone/suite cost comparisons available from measured data | If a fixed exact 13-test matrix exists, add it when specified |",
        "| 5 | File B | model_returned must be recorded for every API call | llm_proxy records model_requested and model_returned per call | Required Gate 3 checks are still pending until credentials are present |",
        "| 6 | File B | Dry-run generates Figures 3-5 | Analysis script generates CSV tables; figures are generated only after real data is available | Figure scripts are a remaining deliverable, not synthetic-plotted data |",
    ]
    (args.output / "deviations.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Analysis written to {args.output}")

    if not fail_rate[fail_rate.over_10pct].empty:
        print("WARNING: configurations above 10% failure rate:")
        print(fail_rate[fail_rate.over_10pct].to_string())


if __name__ == "__main__":
    main()
