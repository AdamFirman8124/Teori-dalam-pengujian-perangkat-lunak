#!/usr/bin/env python3
"""Generate required figures ONLY from a produced results.csv.

Refuses to plot synthetic-dry-run data; runs after analysis of real outputs.
Figures: 3 boxplot (LC/BC/MS per configuration), 4 tool x backbone interaction
(mean with 95% CI), 5 Pareto cost vs effectiveness (log cost scale).
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def ci95(values: pd.Series) -> float:
    values = values.dropna()
    if len(values) < 2:
        return 0.0
    return float(st.sem(values) * st.t.ppf(0.975, len(values) - 1))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / "results" / "figures")
    args = parser.parse_args()
    df = pd.read_csv(args.input)
    if not (df.status == "ok").any():
        raise SystemExit("No OK runs in results; cannot plot figures yet.")
    args.output.mkdir(parents=True, exist_ok=True)
    df["rv"] = df.n_raw_pass / df.n_raw_proposals.replace(0, np.nan) * 100
    df["lc"] = df.lines_exec / df.lines_total.replace(0, np.nan) * 100
    df["bc"] = df.branches_exec / df.branches_total.replace(0, np.nan) * 100
    df["ms"] = df.n_killed / df.n_mutants.replace(0, np.nan) * 100

    # Figure 3: boxplots LC/BC/MS per configuration.
    for metric, ylabel in (("lc", "Line coverage %"), ("bc", "Branch coverage %"), ("ms", "Mutation score %")):
        fig, ax = plt.subplots(figsize=(7, 4))
        data = [
            grp[metric].dropna().to_numpy()
            for _, grp in df.groupby(["suite", "tool", "backbone"])
        ]
        labels = [f"{s}\n{t}\n{b}" for s, t, b in df.groupby(["suite", "tool", "backbone"]).groups.keys()]
        ax.boxplot(data, showfliers=False)
        ax.set_xticks(range(1, len(labels) + 1))
        ax.set_xticklabels(labels)
        ax.set_ylabel(ylabel)
        ax.set_title(f"Figure 3 — {ylabel} per configuration")
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
        fig.tight_layout()
        fig.savefig(args.output / f"figure3_{metric}.png", dpi=150)
    plt.close("all")

    # Figure 4: interaction plot (mean per tool x backbone) for MS (MT) and BC (CM).
    for suite, metric in (("MT", "ms"), ("CM", "bc")):
        sub = df[(df.suite == suite) & (df.status == "ok")]
        means = sub.groupby(["backbone", "tool"])[metric].mean().unstack()
        cis = sub.groupby(["backbone", "tool"])[metric].apply(ci95).unstack()
        x = range(len(means))
        fig, ax = plt.subplots(figsize=(5, 4))
        for tool in means.columns:
            y = means[tool].to_numpy()
            yerr = cis[tool].to_numpy()
            ax.errorbar(x, y, yerr=yerr, label=tool, marker="o", capsize=4)
        ax.set_xticks(list(x))
        ax.set_xticklabels(means.index)
        ax.set_ylabel("Mean per-unit median (%)")
        ax.set_title(f"Figure 4 — tool × backbone ({suite}, {metric})")
        ax.legend()
        fig.tight_layout()
        fig.savefig(args.output / f"figure4_{suite}_{metric}.png", dpi=150)
    plt.close("all")

    # Figure 5: Pareto (log cost vs median effectiveness).
    pareto = df[df.status == "ok"].groupby(["suite", "tool", "backbone"]).agg(
        cost=("cost_usd", "median"), bc=("bc", "median"), ms=("ms", "median")
    ).reset_index()
    # A logarithmic axis cannot represent free/zero-cost configurations.  Keep
    # paid points on their measured cost and place zero-cost points at one
    # decade below the cheapest paid configuration, preserving them visibly
    # without inventing a positive measured cost.
    positive_costs = pareto.loc[pareto.cost > 0, "cost"]
    effectiveness = pareto[["bc", "ms"]].notna().any(axis=1)
    if positive_costs.empty or not effectiveness.any():
        print("SKIPPED Figure 5: positive cost and effectiveness measurements are both required.")
    else:
        pareto = pareto[effectiveness].copy()
        plot_floor = float(positive_costs.min()) / 10
        pareto["plot_cost"] = pareto.cost.where(pareto.cost > 0, plot_floor)
        fig, ax = plt.subplots(figsize=(6, 5))
        for suite, grp in pareto.groupby("suite"):
            ax.scatter(grp.plot_cost, grp.ms, label=f"{suite} MS", s=60)
            ax.scatter(grp.plot_cost, grp.bc, label=f"{suite} BC", s=40, marker="x")
        ax.set_xscale("log")
        ax.set_xlabel("Median generation cost (USD, log scale)")
        ax.set_ylabel("Median effectiveness (%)")
        ax.set_title("Figure 5 — Pareto: cost vs effectiveness")
        ax.legend()
        fig.tight_layout()
        fig.savefig(args.output / "figure5_pareto.png", dpi=150)
    print(f"Figures written to {args.output}")


if __name__ == "__main__":
    main()
