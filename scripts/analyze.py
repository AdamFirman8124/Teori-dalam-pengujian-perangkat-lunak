#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon
import statsmodels.formula.api as smf

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


def load_all_data(input_path: Path) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    base_dir = input_path.parent
    existing_tools = set(df.tool.dropna().unique())

    to_merge = []
    pynguin_file = base_dir / "pynguin_results.csv"
    if "Pynguin" not in existing_tools and pynguin_file.exists():
        to_merge.append(pd.read_csv(pynguin_file))

    mutap_file = base_dir / "mutap_results.csv"
    if "MuTAP" not in existing_tools and mutap_file.exists():
        to_merge.append(pd.read_csv(mutap_file))

    if to_merge:
        df = pd.concat([df, *to_merge], ignore_index=True)
        # Save canonical merged file
        combined_path = base_dir / "results_combined.csv"
        df.to_csv(combined_path, index=False)

    return derivatives(df)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / "results" / "analysis")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    df = load_all_data(args.input)
    ok = df[df.status == "ok"].copy()

    # Fill NaN backbones (e.g. Pynguin) as "-" for consistent grouping
    df_clean = df.copy()
    df_clean["backbone"] = df_clean["backbone"].fillna("-")
    ok_clean = ok.copy()
    ok_clean["backbone"] = ok_clean["backbone"].fillna("-")

    # TABEL IV: effectiveness summary with mean, median, std across repetitions
    summary = ok_clean.groupby(["suite", "tool", "backbone"])[
        ["rv", "lc", "bc", "ms", "gen_time_s", "tokens_in", "tokens_out", "cost_usd"]
    ].agg(["mean", "median", "std"])
    summary.to_csv(args.output / "table_iv_summary.csv")

    # Failure rate
    total = df_clean.groupby(["suite", "tool", "backbone"]).size().rename("n_total")
    failed = df_clean[df_clean.status != "ok"].groupby(["suite", "tool", "backbone"]).size().rename("n_failed")
    top_category = (
        df_clean[df_clean.status != "ok"]
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

    # Matched per-unit medians for paired tool comparisons
    unit = ok_clean.groupby(["suite", "backbone", "unit_id", "tool"])[["bc", "ms", "cost_usd", "gen_time_s"]].median().reset_index()

    # TABEL V: Paired comparisons specified in research design (B1 & B2 backbones)
    paired_spec = [
        # B1 Backbone (RQ1)
        ("MT", "ms", "B1", "MuTAP", "Pynguin"),
        ("MT", "ms", "B1", "MuTAP", "CodaMOSA"),
        ("MT", "ms", "B1", "MuTAP", "CoverUp"),
        ("MT", "ms", "B1", "CoverUp", "Pynguin"),
        ("MT", "ms", "B1", "CoverUp", "CodaMOSA"),
        ("MT", "ms", "B1", "CodaMOSA", "Pynguin"),
        ("CM", "bc", "B1", "CoverUp", "Pynguin"),
        ("CM", "bc", "B1", "CoverUp", "CodaMOSA"),
        ("CM", "bc", "B1", "CodaMOSA", "Pynguin"),
        ("CM", "ms", "B1", "CoverUp", "Pynguin"),
        ("CM", "ms", "B1", "CoverUp", "CodaMOSA"),
        ("CM", "ms", "B1", "CodaMOSA", "Pynguin"),
        # B2 Backbone (RQ1)
        ("MT", "ms", "B2", "CoverUp", "Pynguin"),
        ("MT", "ms", "B2", "CoverUp", "CodaMOSA"),
        ("MT", "ms", "B2", "CodaMOSA", "Pynguin"),
        ("CM", "bc", "B2", "CoverUp", "Pynguin"),
        ("CM", "bc", "B2", "CoverUp", "CodaMOSA"),
        ("CM", "bc", "B2", "CodaMOSA", "Pynguin"),
        ("CM", "ms", "B2", "CoverUp", "Pynguin"),
        ("CM", "ms", "B2", "CoverUp", "CodaMOSA"),
        ("CM", "ms", "B2", "CodaMOSA", "Pynguin"),
    ]

    tests = []
    for suite, metric, bb, a, b in paired_spec:
        sub_a = unit[(unit.suite == suite) & ((unit.backbone == bb) | (unit.tool == "Pynguin")) & (unit.tool == a)][["unit_id", metric]].rename(columns={metric: a})
        sub_b = unit[(unit.suite == suite) & ((unit.backbone == bb) | (unit.tool == "Pynguin")) & (unit.tool == b)][["unit_id", metric]].rename(columns={metric: b})
        merged = pd.merge(sub_a, sub_b, on="unit_id").dropna()
        if len(merged):
            delta = merged[a] - merged[b]
            stat, p = wilcoxon(delta) if np.any(delta) else (0.0, 1.0)
            ci_low, ci_high = bootstrap_ci(delta.to_numpy())
            tests.append(
                {
                    "suite": suite,
                    "metric": metric,
                    "backbone": bb,
                    "comparison": f"{a} vs {b}",
                    "tool_a": a,
                    "tool_b": b,
                    "n": len(delta),
                    "wins": int((delta > 0).sum()),
                    "ties": int((delta == 0).sum()),
                    "losses": int((delta < 0).sum()),
                    "a12": a12(merged[a].to_numpy(), merged[b].to_numpy()),
                    "mean_difference": float(delta.mean()),
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

    # TABEL VI: backbone effect per LLM generator (mean over units)
    adaptasi = {"CodaMOSA": "interface-only", "CoverUp": "none", "MuTAP": "none (B1 only)"}
    backbone_rows = []
    for suite, metric in (("MT", "ms"), ("CM", "bc")):
        for tool in ("CodaMOSA", "CoverUp"):
            means = unit[(unit.suite == suite) & (unit.tool == tool)].groupby("backbone")[metric].mean()
            if {"B1", "B2"}.issubset(means.index):
                backbone_rows.append(
                    {
                        "suite": suite,
                        "metric": metric,
                        "tool": tool,
                        "adaptasi": adaptasi[tool],
                        "b1": round(float(means["B1"]), 2),
                        "b2": round(float(means["B2"]), 2),
                        "delta_b1_minus_b2": round(float(means["B1"] - means["B2"]), 2),
                        "n_units": int(unit[(unit.suite == suite) & (unit.tool == tool)].unit_id.nunique()),
                    }
                )
    pd.DataFrame(backbone_rows).to_csv(args.output / "table_vi_backbone_effect.csv", index=False)

    # TABEL VII: Linear Mixed-Effects Models (RQ2)
    # metric ~ tool * backbone + (1 | unit)
    vii_rows = []
    for suite, metric, dep_name in [("MT", "ms", "Mutation score"), ("CM", "bc", "Branch coverage")]:
        sub = ok_clean[(ok_clean.suite == suite) & (ok_clean.tool.isin(["CodaMOSA", "CoverUp"]))].dropna(subset=[metric]).copy()
        if not sub.empty:
            formula = f'{metric} ~ C(tool, Treatment(reference="CodaMOSA")) * C(backbone, Treatment(reference="B1"))'
            md = smf.mixedlm(formula, sub, groups=sub["unit_id"])
            mdf = md.fit()

            # Variance decomposition via Sum of Squares
            # Total sum of squares of unit-level residuals
            y = sub[metric].to_numpy()
            ss_tot = float(np.sum((y - np.mean(y)) ** 2))

            # Sum of squares attributed to Tool, Backbone, Interaction
            mean_tool = sub.groupby("tool")[metric].transform("mean").to_numpy()
            ss_tool = float(np.sum((mean_tool - np.mean(y)) ** 2))

            mean_bb = sub.groupby("backbone")[metric].transform("mean").to_numpy()
            ss_bb = float(np.sum((mean_bb - np.mean(y)) ** 2))

            mean_tb = sub.groupby(["tool", "backbone"])[metric].transform("mean").to_numpy()
            ss_tb = float(np.sum((mean_tb - np.mean(y)) ** 2))
            ss_inter = max(0.0, ss_tb - ss_tool - ss_bb)

            pct_tool = (ss_tool / ss_tot) * 100 if ss_tot > 0 else 0.0
            pct_bb = (ss_bb / ss_tot) * 100 if ss_tot > 0 else 0.0
            pct_inter = (ss_inter / ss_tot) * 100 if ss_tot > 0 else 0.0

            conf = mdf.conf_int()
            for param_name in mdf.params.index:
                if param_name == "Group Var":
                    continue
                # Human-friendly label
                if "CoverUp" in param_name and "B2" in param_name:
                    factor_label = "CoverUp × B2"
                    var_pct = pct_inter
                elif "CoverUp" in param_name:
                    factor_label = "Tool: CoverUp"
                    var_pct = pct_tool
                elif "B2" in param_name:
                    factor_label = "Backbone: B2"
                    var_pct = pct_bb
                else:
                    factor_label = "Intercept (CodaMOSA, B1)"
                    var_pct = np.nan

                vii_rows.append(
                    {
                        "suite": suite,
                        "metric": metric,
                        "factor": factor_label,
                        "estimate": round(float(mdf.params[param_name]), 3),
                        "ci_95_low": round(float(conf.loc[param_name, 0]), 3),
                        "ci_95_high": round(float(conf.loc[param_name, 1]), 3),
                        "p_value": float(mdf.pvalues[param_name]),
                        "var_pct": round(var_pct, 2) if not np.isnan(var_pct) else "-",
                    }
                )
    pd.DataFrame(vii_rows).to_csv(args.output / "table_vii_mixed_effects.csv", index=False)

    # TABEL VIII: Cost summary and Cost-Effectiveness (RQ3)
    cost_summary = ok_clean.groupby(["suite", "tool", "backbone"])[
        ["tokens_in", "tokens_out", "cost_usd", "gen_time_s", "hit_budget"]
    ].agg(["mean", "median", "std"])
    cost_summary.to_csv(args.output / "table_viii_cost.csv")

    # Cost-effectiveness with Pynguin baseline
    # MT baseline is Pynguin MS; CM baseline is Pynguin BC
    pynguin_baselines = {}
    for s, m in [("MT", "ms"), ("CM", "bc")]:
        py_unit = unit[(unit.suite == s) & (unit.tool == "Pynguin")][m]
        pynguin_baselines[s] = float(py_unit.median()) if not py_unit.empty else 0.0

    ce_rows = []
    for (s, t, b), grp in ok_clean.groupby(["suite", "tool", "backbone"]):
        if t == "Pynguin":
            continue
        eval_metric = "ms" if s == "MT" else "bc"
        base_val = pynguin_baselines.get(s, 0.0)
        tool_med = float(unit[(unit.suite == s) & (unit.tool == t) & (unit.backbone == b)][eval_metric].median())
        med_cost = float(grp["cost_usd"].median())
        delta_e = tool_med - base_val
        ce_ratio = (delta_e / med_cost) if med_cost > 0 else np.nan
        ce_rows.append(
            {
                "suite": s,
                "tool": t,
                "backbone": b,
                "metric": eval_metric,
                "tool_median": round(tool_med, 2),
                "baseline_pynguin": round(base_val, 2),
                "delta_e": round(delta_e, 2),
                "median_cost_usd": round(med_cost, 6),
                "CE": round(ce_ratio, 2) if not np.isnan(ce_ratio) else np.nan,
            }
        )
    pd.DataFrame(ce_rows).to_csv(args.output / "table_viii_cost_effectiveness.csv", index=False)

    # Pareto data (Figure 5)
    pareto = ok_clean.groupby(["suite", "tool", "backbone"]).agg(
        median_cost_usd=("cost_usd", "median"),
        median_bc=("bc", "median"),
        median_ms=("ms", "median"),
    ).reset_index()
    pareto.to_csv(args.output / "figure_5_pareto_data.csv", index=False)

    # File B Table IX: Wilcoxon cost tests
    cost_tests = []
    tools = [t for t in sorted(ok_clean.tool.dropna().unique()) if t != "Pynguin"]
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
                            "median_delta_cost": float(delta.median()),
                            "wilcoxon_stat": stat,
                            "p": p,
                        }
                    )
    if cost_tests:
        adjusted = holm([row["p"] for row in cost_tests])
        for row, value in zip(cost_tests, adjusted):
            row["p_holm"] = value
    pd.DataFrame(cost_tests).to_csv(args.output / "table_ix_cost_wilcoxon.csv", index=False)

    # Excluded tasks audit
    excluded = df[df.status != "ok"].sort_values(["suite", "tool", "backbone", "unit_id", "run_idx"])
    excluded.to_csv(args.output / "excluded_tasks.csv", index=False)

    print(f"Analysis successfully written to {args.output}")


if __name__ == "__main__":
    main()
