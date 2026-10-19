"""Build paper-aligned RQ tables from experiment rows.

Usage: python tools/rq_tables.py experiment_results/rows.csv [outdir]

MuTAP rows come from another device; merge them first with
``tools/merge_collaborator_results.py``. Missing metrics stay missing and are
never silently converted to zero.
"""
from __future__ import annotations

import itertools
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import rankdata, spearmanr, wilcoxon

ROWS = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else ROWS.parent
OUT.mkdir(parents=True, exist_ok=True)
NUMERIC = ["raw_validity", "flaky_count", "line_pct", "branch_pct",
           "mutation_score", "wall_time_s", "cost_usd", "prompt_tokens",
           "completion_tokens", "total_tokens", "calls_with_usage"]
PRIMARY = {"MT": "mutation_score", "CM": "branch_pct"}


def _backbone(model: object) -> str:
    return str(model or "-").removeprefix("openai/") or "-"


def _markdown(df: pd.DataFrame) -> str:
    if df.empty:
        return "_Belum ada data yang memenuhi syarat._\n"
    headers = [str(c) for c in df.columns]
    body = ["| " + " | ".join(headers) + " |",
            "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in df.itertuples(index=False, name=None):
        body.append("| " + " | ".join("-" if pd.isna(x) else str(x) for x in row) + " |")
    return "\n".join(body) + "\n"


def _write(name: str, frame: pd.DataFrame) -> None:
    frame.to_csv(OUT / f"{name}.csv", index=False)
    (OUT / f"{name}.md").write_text(_markdown(frame), encoding="utf-8")


def _holm(pvals: list[float]) -> list[float]:
    out = [math.nan] * len(pvals)
    finite = sorted(((i, p) for i, p in enumerate(pvals) if not math.isnan(p)), key=lambda x: x[1])
    running, count = 0.0, len(finite)
    for rank, (index, pval) in enumerate(finite):
        running = max(running, min(1.0, (count - rank) * pval))
        out[index] = running
    return out


def _a12(a: np.ndarray, b: np.ndarray) -> float:
    if not len(a) or not len(b):
        return math.nan
    greater = sum(float(x > y) for x in a for y in b)
    equal = sum(float(x == y) for x in a for y in b)
    return (greater + 0.5 * equal) / (len(a) * len(b))


frame = pd.read_csv(ROWS, dtype={"task": str})
for column in NUMERIC:
    if column not in frame:
        frame[column] = np.nan
    frame[column] = pd.to_numeric(frame[column], errors="coerce")
frame["model"] = frame["model"].map(_backbone)
frame["suite"] = frame["dataset"]
per_unit = frame.groupby(["suite", "method", "model", "task"], dropna=False)[NUMERIC].median().reset_index()

# TABEL IV: median per unit, then median across units.
table_iv = per_unit.groupby(["suite", "method", "model"], dropna=False).agg(
    n=("task", "nunique"), RV=("raw_validity", "median"),
    Flaky=("flaky_count", "sum"), LC=("line_pct", "median"),
    BC=("branch_pct", "median"), MS=("mutation_score", "median"),
).reset_index().rename(columns={"suite": "Suite", "method": "Tool", "model": "BB"})
_write("table_iv_effectiveness", table_iv)

# TABEL V: paired Wilcoxon + Holm + A12; BC for CM and MS for MT.
pair_rows = []
for suite in sorted(per_unit["suite"].dropna().unique()):
    metric = PRIMARY.get(suite)
    if not metric:
        continue
    subset = per_unit[per_unit["suite"] == suite]
    for model in sorted(subset["model"].dropna().unique()):
        variants = sorted(subset[subset["model"] == model]["method"].dropna().unique())
        for a_name, b_name in itertools.combinations(variants, 2):
            a = subset[(subset["model"] == model) & (subset["method"] == a_name)].set_index("task")[metric]
            b = subset[(subset["model"] == model) & (subset["method"] == b_name)].set_index("task")[metric]
            paired = pd.concat([a.rename("a"), b.rename("b")], axis=1).dropna()
            if paired.empty:
                continue
            av, bv = paired["a"].to_numpy(), paired["b"].to_numpy()
            diff = av - bv
            pval = 1.0 if np.allclose(diff, 0) else float(wilcoxon(av, bv, zero_method="wilcox").pvalue)
            pair_rows.append({"Suite": suite, "BB": model, "Metric": metric,
                              "A vs B": f"{a_name} vs {b_name}", "n": len(paired),
                              "M/S/K": f"{int((av > bv).sum())}/{int((av == bv).sum())}/{int((av < bv).sum())}",
                              "A12": _a12(av, bv), "p_raw": pval})
table_v = pd.DataFrame(pair_rows)
if not table_v.empty:
    table_v["p_Holm"] = _holm(table_v["p_raw"].tolist())
_write("table_v_pairs", table_v)


# TABEL VI: descriptive B1 -> B2 difference for LLM-backed tools.
backbone_rows = []
for (suite, tool), group in per_unit.groupby(["suite", "method"], dropna=False):
    metric = PRIMARY.get(suite)
    models = sorted(group["model"].dropna().unique())
    if tool not in {"CoverUp", "CODAMOSA", "MuTAP"} or not metric or len(models) != 2:
        continue
    means = group.groupby("model")[metric].mean()
    backbone_rows.append({"Suite": suite, "Metric": metric, "Tool": tool,
                          "B1": models[0], "B1_score": means.get(models[0]),
                          "B2": models[1], "B2_score": means.get(models[1]),
                          "Delta_B1_minus_B2": means.get(models[0]) - means.get(models[1])})
_write("table_vi_backbone", pd.DataFrame(backbone_rows))

# TABEL VIII: partial Spearman (control LOC), only when characteristics exist.
characteristics_path = ROWS.parent / "module_characteristics.csv"
rq3_rows = []
if characteristics_path.is_file():
    chars = pd.read_csv(characteristics_path, dtype={"task": str})
    cm = per_unit[per_unit["suite"] == "CM"]
    llm_models = cm[cm["method"].isin(["CoverUp", "CODAMOSA"])]["model"].dropna()
    model = sorted(llm_models.unique())[0] if not llm_models.empty else None
    # Pynguin has no backbone (usually '-'); pair it with the selected B1 rows.
    cm = cm[(cm["model"] == model) | (cm["method"] == "Pynguin")]
    for a_name, b_name in (("CoverUp", "Pynguin"), ("CODAMOSA", "Pynguin"),
                           ("CoverUp", "CODAMOSA")):
        a = cm[cm["method"] == a_name].set_index("task")["branch_pct"]
        b = cm[cm["method"] == b_name].set_index("task")["branch_pct"]
        data = chars.set_index("task").join((a - b).rename("advantage"))
        data = data.dropna(subset=["advantage", "loc"])
        for characteristic in ("cyclomatic_complexity", "external_dependencies",
                               "type_annotation_density"):
            if characteristic not in data or len(data) < 4:
                continue
            x_rank, y_rank = rankdata(data[characteristic]), rankdata(data["advantage"])
            controls = np.column_stack([np.ones(len(data)), rankdata(data["loc"])])
            x_res = x_rank - controls @ np.linalg.lstsq(controls, x_rank, rcond=None)[0]
            y_res = y_rank - controls @ np.linalg.lstsq(controls, y_rank, rcond=None)[0]
            if data[characteristic].nunique() < 2 or data["advantage"].nunique() < 2:
                continue
            x_rank, y_rank = rankdata(data[characteristic]), rankdata(data["advantage"])
            controls = np.column_stack([np.ones(len(data)), rankdata(data["loc"])])
            x_res = x_rank - controls @ np.linalg.lstsq(controls, x_rank, rcond=None)[0]
            y_res = y_rank - controls @ np.linalg.lstsq(controls, y_rank, rcond=None)[0]
            if np.ptp(x_res) == 0 or np.ptp(y_res) == 0:
                continue
            rho, pval = spearmanr(x_res, y_res)
            rq3_rows.append({"Comparison": f"{a_name} vs {b_name}",
                             "Characteristic": characteristic, "n": len(data),
                             "rho_partial": rho, "p_raw": pval})
table_viii = pd.DataFrame(rq3_rows)
if not table_viii.empty:
    table_viii["p_Holm"] = _holm(table_viii["p_raw"].tolist())
_write("table_viii_spearman", table_viii)


# TABEL VII: mixed-effects metric ~ tool * backbone + (1 | unit).
mixed_rows = []
try:
    import statsmodels.formula.api as smf
except ImportError:
    smf = None
for suite in sorted(per_unit["suite"].dropna().unique()):
    metric = PRIMARY.get(suite)
    if not metric or smf is None:
        continue
    data = per_unit[per_unit["suite"] == suite].dropna(subset=[metric, "model"])
    tools = [t for t in ("CODAMOSA", "CoverUp", "MuTAP")
             if t in set(data["method"])]
    if len(tools) < 2 or data["model"].nunique() < 2:
        continue
    data = data.assign(tool=data["method"], backbone=data["model"])
    formula = f"{metric} ~ C(tool, Treatment('{tools[0]}')) * C(backbone)"
    try:
        fit = smf.mixedlm(formula, data, groups=data["task"]).fit(reml=False)
    except (ValueError, np.linalg.LinAlgError):
        continue
    conf = fit.conf_int()
    for term in fit.params.index:
        if term in {"Intercept", "Group Var"}:
            continue
        mixed_rows.append({"Suite": suite, "Metric": metric, "Factor": term,
                           "Estimate": fit.params[term],
                           "CI_low": conf.loc[term, 0], "CI_high": conf.loc[term, 1],
                           "p": fit.pvalues.get(term, np.nan)})
_write("table_vii_mixed_effects", pd.DataFrame(mixed_rows))
if smf is None:
    print("statsmodels absent: TABEL VII skipped (pip install statsmodels)")


# TABEL IX: generation cost per unit (median).
cost = per_unit.groupby(["suite", "method", "model"], dropna=False).agg(
    Wall_s=("wall_time_s", "median"), Cost_USD=("cost_usd", "median"),
    Tokens=("prompt_tokens", "median"),
).reset_index().rename(columns={"suite": "Suite", "method": "Tool", "model": "BB"})
_write("table_ix_cost", cost)


# Gambar 3/4/5 (only when matplotlib is usable in a headless session).
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    figures = OUT / "figures"
    figures.mkdir(exist_ok=True)
    mt = per_unit[per_unit["suite"] == "MT"]
    if not mt.empty:
        fig, axes = plt.subplots(1, 2, figsize=(11, 4))
        for axis, metric, title in zip(axes, ("line_pct", "mutation_score"),
                                       ("Coverage per fungsi (%)", "Mutation score (%)")):
            groups = [g[metric].dropna().to_numpy() for _, g in mt.groupby(["method", "model"])]
            labels = [f"{m}\n{b}" for (m, b), _ in mt.groupby(["method", "model"])]
            axis.boxplot(groups, tick_labels=labels)
            axis.tick_params(axis="x", labelrotation=90)
            axis.set_title(title)
            axis.grid(alpha=0.3)
        fig.tight_layout()
        fig.savefig(figures / "figure_3_mt_boxplot.png", dpi=200)
        plt.close(fig)
    cm = per_unit[per_unit["suite"] == "CM"]
    if not cm.empty:
        fig, axis = plt.subplots(figsize=(6, 4))
        for (method, model), group in cm.groupby(["method", "model"]):
            axis.scatter([f"{method}\n{model}"] * len(group), group["branch_pct"],
                         s=12, alpha=0.5)
        axis.set_ylabel("Branch coverage (%)")
        axis.grid(alpha=0.3)
        fig.tight_layout()
        fig.savefig(figures / "figure_4_cm_branch.png", dpi=200)
        plt.close(fig)
except Exception as exc:  # pragma: no cover - plotting is best effort
    print("figures skipped:", exc)

print("wrote paper tables to", OUT)
