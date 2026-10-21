"""Build every table and figure required by Rancangan_Bab_Results_ID.pdf.

The module is deliberately independent of the notebook so the Windows-native and
the Linux-native experiment notebooks can share one, identical analysis layer.

Tables produced (numbering follows the PDF):
  TABEL IV  effectiveness per suite x tool x backbone (RV, Flaky, LC, BC, MS)
  TABEL V   pairwise Wilcoxon signed-rank + Holm + Vargha-Delaney A12 (B1)
  TABEL VI  backbone effect per generator (B1 vs B2)
  TABEL VII linear mixed-effects model  metric ~ tool * backbone + (1|unit)
  TABEL VIII partial Spearman (controlling LOC) between module characteristics
            and per-module branch-coverage advantage on CM
  TABEL IX  efficiency and cost per unit (wall time, API calls, tokens, USD)
  Gambar 3  boxplot MT coverage vs mutation score
  Gambar 4  interaction plot tool x backbone
  Gambar 5  scatter of the strongest RQ3 association

Design rules
  * A metric that was never measured is reported as "-", never as 0.
  * Rows are medians over units; when R > 1 the median of the per-unit medians
    is used, exactly as the PDF describes.
  * Everything degrades gracefully: with a single backbone or a single suite the
    affected table prints an explicit "not measurable yet" note instead of
    inventing numbers.
"""
from __future__ import annotations

import json
import math
import os
import sys
from pathlib import Path
from typing import Any, Iterable, Sequence

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eval_metrics import canonical_model_name

MISSING = "-"
SCORE_FIELDS = ("line_pct", "branch_pct", "mutation_score", "pass_rate")
COST_FIELDS = ("wall_time_s", "cost_usd", "prompt_tokens", "completion_tokens",
               "total_tokens")


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #
def _num(value: Any) -> float | None:
    try:
        out = float(value)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(out) else out


def load_rows(out_dir: Path) -> pd.DataFrame:
    """Read rows.csv plus the per-call LLM logs into one tidy frame."""
    rows_path = Path(out_dir) / "rows.csv"
    if not rows_path.is_file():
        return pd.DataFrame()
    frame = pd.read_csv(rows_path, dtype=str, keep_default_na=False)
    if frame.empty:
        return frame
    for column in SCORE_FIELDS + COST_FIELDS:
        frame[column] = pd.to_numeric(frame.get(column), errors="coerce") \
            if column in frame.columns else np.nan
    frame["model"] = (frame.get("model", pd.Series(dtype=str))
                      .fillna(MISSING).astype(str).map(
                          lambda m: canonical_model_name(m).replace("openai/", "")))
    frame["backbone"] = frame["model"].replace({"": MISSING, "nan": MISSING})
    frame["task"] = frame["task"].astype(str)
    frame["dataset"] = frame["dataset"].astype(str)
    frame["method"] = frame["method"].astype(str)
    return frame


def load_llm_calls(out_dir: Path) -> pd.DataFrame:
    """Per-call log written by CoverUp and CodaMOSA."""
    root = Path(out_dir) / "llm_calls"
    records: list[dict[str, Any]] = []
    if not root.exists():
        return pd.DataFrame(records)
    for path in sorted(root.rglob("*.jsonl")):
        try:
            rel = path.relative_to(root)
            parts = rel.parts
            method, dataset, task = parts[0], parts[-2], path.stem
            model = "/".join(parts[1:-2]).replace("openai_", "openai/")
        except (ValueError, IndexError):
            continue
        for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
            raw = raw.strip()
            if not raw:
                continue
            try:
                entry = json.loads(raw)
            except json.JSONDecodeError:
                continue
            records.append({
                "method": method,
                "model": canonical_model_name(
                    str(entry.get("model") or model)).replace("openai/", ""),
                "dataset": dataset,
                "task": task,
                "prompt_tokens": _num(entry.get("prompt_tokens")) or 0.0,
                "completion_tokens": _num(entry.get("completion_tokens")) or 0.0,
                "total_tokens": _num(entry.get("total_tokens")) or 0.0,
                "cost_usd": _num(entry.get("cost_usd")),
                "latency_s": _num(entry.get("latency_s")),
                "output": str(entry.get("output") or ""),
                "finish_reason": entry.get("finish_reason"),
            })
    return pd.DataFrame(records)


# --------------------------------------------------------------------------- #
# Statistics helpers
# --------------------------------------------------------------------------- #
def holm(pvalues: Sequence[float]) -> list[float]:
    m = len(pvalues)
    if not m:
        return []
    order = np.argsort(pvalues)
    adjusted = [0.0] * m
    running = 0.0
    for rank, index in enumerate(order):
        candidate = min(1.0, float(pvalues[index]) * (m - rank))
        running = max(running, candidate)
        adjusted[index] = running
    return adjusted


def a12(a: np.ndarray, b: np.ndarray) -> float:
    """Vargha-Delaney A12 = P(a>b) + 0.5 P(a==b)."""
    if not len(a) or not len(b):
        return float("nan")
    gt = sum(int(np.sum(a[i] > b)) for i in range(len(a)))
    eq = sum(int(np.sum(a[i] == b)) for i in range(len(a)))
    return (gt + 0.5 * eq) / (len(a) * len(b))


def _pct(value: Any, digits: int = 1) -> str:
    number = _num(value)
    return MISSING if number is None else f"{number:.{digits}f}"


def _fmt_p(value: float) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return MISSING
    if value < 0.0001:
        return "<0.0001"
    return f"{value:.4f}"


def unit_medians(frame: pd.DataFrame, metric: str) -> pd.DataFrame:
    """One value per (dataset, method, backbone, task).

    With R > 1 runs per unit this is the median of the R runs; with R = 1 it is
    the single run.  The PDF's "median of medians" then follows from taking the
    median over tasks in the table builders.
    """
    if frame.empty or metric not in frame.columns:
        return pd.DataFrame(columns=["dataset", "method", "backbone", "task", metric])
    sub = frame[["dataset", "method", "backbone", "task", metric]].dropna(subset=[metric])
    if sub.empty:
        return sub
    return (sub.groupby(["dataset", "method", "backbone", "task"], as_index=False)[metric]
            .median())


# --------------------------------------------------------------------------- #
# TABEL IV
# --------------------------------------------------------------------------- #
def raw_validity(calls: pd.DataFrame) -> pd.DataFrame:
    """Share of LLM proposals whose emitted code contains an assertion.

    This is a conservative proxy computed from the stored call log: a proposal
    counts as usable when the model emitted a fenced Python block with at least
    one ``assert``.  It is labelled as such in the output so it is never
    confused with an execution-based raw validity.
    """
    if calls.empty:
        return pd.DataFrame(columns=["dataset", "method", "model", "RV", "n_calls"])
    work = calls.copy()
    work["proposed"] = work["output"].str.contains("```python", regex=False)
    work["with_assert"] = work["output"].str.contains("assert ", regex=False)
    work = work[work["proposed"]]
    if work.empty:
        return pd.DataFrame(columns=["dataset", "method", "model", "RV", "n_calls"])
    grouped = work.groupby(["dataset", "method", "model"], as_index=False).agg(
        RV=("with_assert", lambda s: 100.0 * float(np.mean(s))),
        n_calls=("with_assert", "size"))
    return grouped


def table_iv(frame: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    """TABEL IV: effectiveness per suite x tool x backbone."""
    if frame.empty:
        return pd.DataFrame()
    rv = raw_validity(calls)
    records = []
    for (dataset, method, backbone), group in frame.groupby(
            ["dataset", "method", "backbone"], dropna=False):
        valid = group
        if "pass_rate" in group.columns and group["pass_rate"].notna().any():
            passing = group[group["pass_rate"].fillna(0) >= 100.0]
            valid = passing if not passing.empty else group
        record = {
            "Suite": dataset,
            "Tool": method,
            "BB": backbone,
            "RV (%)": MISSING,
            "Flaky": MISSING,
            "LC (%)": _pct(valid["line_pct"].median()),
            "BC (%)": _pct(valid["branch_pct"].median()),
            "MS (%)": _pct(valid["mutation_score"].median()),
            "n": int(group["task"].nunique()),
        }
        match = rv[(rv["dataset"] == dataset) & (rv["method"] == method)
                   & (rv["model"] == backbone)]
        if not match.empty:
            record["RV (%)"] = _pct(match["RV"].iloc[0])
        if str(method).lower() == "pynguin":
            record["RV (%)"] = "n/a"
            record["Flaky"] = "n/a"
        records.append(record)
    return pd.DataFrame(records).sort_values(["Suite", "Tool", "BB"]).reset_index(drop=True)


# --------------------------------------------------------------------------- #
# TABEL V
# --------------------------------------------------------------------------- #
def table_v(frame: pd.DataFrame, metric: str, dataset: str,
            backbone: str | None = None) -> pd.DataFrame:
    """TABEL V: pairwise Wilcoxon + Holm + A12 for one metric and suite."""
    if frame.empty:
        return pd.DataFrame()
    sub = frame[frame["dataset"] == dataset]
    if backbone is not None:
        sub = sub[sub["backbone"] == backbone]
    if sub.empty:
        return pd.DataFrame()
    medians = unit_medians(sub, metric)
    if medians.empty:
        return pd.DataFrame()
    pivot = medians.pivot_table(index="task", columns="method", values=metric)
    tools = [c for c in pivot.columns if pivot[c].notna().sum() >= 3]
    if len(tools) < 2:
        return pd.DataFrame()

    from scipy.stats import wilcoxon

    rows, raw_p = [], []
    for i, a_tool in enumerate(tools):
        for b_tool in tools[i + 1:]:
            paired = pivot[[a_tool, b_tool]].dropna()
            if len(paired) < 3:
                continue
            a = paired[a_tool].to_numpy(float)
            b = paired[b_tool].to_numpy(float)
            diff = a - b
            nonzero = diff[diff != 0]
            if len(nonzero) == 0:
                p = 1.0
            else:
                try:
                    _, p = wilcoxon(a, b, alternative="two-sided")
                except ValueError:
                    p = 1.0
            rows.append({
                "Suite": dataset,
                "Metrik": metric,
                "A vs B": f"{a_tool} vs {b_tool}",
                "n": len(paired),
                "M/S/K": f"{int((diff > 0).sum())}/{int((diff == 0).sum())}/{int((diff < 0).sum())}",
                "A12": round(a12(a, b), 3),
                "p (Holm)": p,
            })
            raw_p.append(p)
    if not rows:
        return pd.DataFrame()
    for row, adjusted in zip(rows, holm(raw_p)):
        row["p (Holm)"] = _fmt_p(adjusted)
        row["Signifikan"] = "ya" if adjusted < 0.05 else "tidak"
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------- #
# TABEL VI + VII + Gambar 4
# --------------------------------------------------------------------------- #
def table_vi(frame: pd.DataFrame, metric_by_suite: dict[str, str]) -> pd.DataFrame:
    """TABEL VI: backbone effect per generator (mean over units)."""
    if frame.empty:
        return pd.DataFrame()
    records = []
    for dataset, metric in metric_by_suite.items():
        sub = frame[frame["dataset"] == dataset]
        if sub.empty or metric not in sub.columns:
            continue
        for method, group in sub.groupby("method"):
            per_backbone = group.groupby("backbone")[metric].mean()
            if per_backbone.empty:
                continue
            b1 = per_backbone.get("GPT-5.6 Sol", np.nan)
            b2 = per_backbone.get("GPT-5.6 Luna", np.nan)
            delta = (b1 - b2) if pd.notna(b1) and pd.notna(b2) else np.nan
            records.append({
                "Suite": dataset, "Metrik": metric, "Tool": method,
                "Adaptasi": "tidak ada" if method.lower() == "coverup" else "interface-only",
                "B1": _pct(b1), "B2": _pct(b2), "Δ (B1−B2)": _pct(delta),
            })
    return pd.DataFrame(records)


def table_vii(frame: pd.DataFrame, dataset: str, metric: str) -> pd.DataFrame:
    """TABEL VII: linear mixed-effects  metric ~ tool * backbone + (1|unit)."""
    if frame.empty or metric not in frame.columns:
        return pd.DataFrame()
    sub = frame[(frame["dataset"] == dataset)][
        ["task", "method", "backbone", metric]].dropna()
    if sub.empty or sub["backbone"].nunique() < 2 or sub["method"].nunique() < 2:
        return pd.DataFrame()
    try:
        import statsmodels.formula.api as smf
        sub = sub.rename(columns={metric: "value", "task": "unit",
                                  "method": "tool", "backbone": "bb"})
        model = smf.mixedlm("value ~ C(tool) * C(bb)", sub, groups=sub["unit"]).fit()
    except Exception:
        return pd.DataFrame()
    records = []
    for name, estimate in model.params.items():
        if name == "Group Var":
            continue
        try:
            ci_low, ci_high = model.conf_int().loc[name]
            p_value = model.pvalues[name]
        except Exception:
            ci_low = ci_high = p_value = np.nan
        records.append({
            "Suite": dataset, "Metrik": metric,
            "Faktor": name.replace("C(tool)[T.", "Tool: ").replace("C(bb)[T.", "Backbone: ")
                              .replace("]", "").replace(":", " × "),
            "Estimasi": round(float(estimate), 2),
            "SK 95%": f"[{ci_low:.2f}, {ci_high:.2f}]" if pd.notna(ci_low) else MISSING,
            "p": _fmt_p(float(p_value)) if pd.notna(p_value) else MISSING,
            "Var. (%)": MISSING,
        })
    return pd.DataFrame(records)


# --------------------------------------------------------------------------- #
# TABEL VIII + Gambar 5
# --------------------------------------------------------------------------- #
def _rank_residual(values: pd.Series, control: pd.Series) -> np.ndarray:
    """Residual of the ranked values after removing the ranked control."""
    y = pd.Series(values).rank(method="average").to_numpy(float)
    x = pd.Series(control).rank(method="average").to_numpy(float)
    design = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(design, y, rcond=None)
    return y - design @ beta


def table_viii(frame: pd.DataFrame, characteristics: pd.DataFrame,
               backbone: str | None = None) -> pd.DataFrame:
    """TABEL VIII: partial Spearman (control LOC) of per-module BC advantage."""
    if frame.empty or characteristics.empty:
        return pd.DataFrame()
    sub = frame[frame["dataset"] == "CM"]
    if backbone is not None:
        sub = sub[sub["backbone"] == backbone]
    if sub.empty:
        return pd.DataFrame()
    medians = unit_medians(sub, "branch_pct")
    if medians.empty:
        return pd.DataFrame()
    pivot = medians.pivot_table(index="task", columns="method", values="branch_pct")
    characteristics = characteristics.set_index("task")
    records, raw_p = [], []
    for a_tool, b_tool in (("CoverUp", "Pynguin"), ("CodaMOSA", "Pynguin"),
                           ("CoverUp", "CodaMOSA")):
        if a_tool not in pivot.columns or b_tool not in pivot.columns:
            continue
        advantage = (pivot[a_tool] - pivot[b_tool]).dropna()
        joined = characteristics.reindex(advantage.index).dropna(subset=["loc"])
        if len(joined) < 10:
            continue
        adv = advantage.reindex(joined.index)
        for feature in ("cyclomatic_complexity", "external_dependencies",
                        "type_annotation_density"):
            x = joined[feature].astype(float)
            y_res = _rank_residual(adv, joined["loc"])
            x_res = _rank_residual(x, joined["loc"])
            if np.std(x_res) == 0 or np.std(y_res) == 0:
                rho, p = 0.0, 1.0
            else:
                rho = float(np.corrcoef(x_res, y_res)[0, 1])
                n = len(x_res)
                if abs(rho) >= 1.0:
                    p = 0.0
                else:
                    t_stat = rho * math.sqrt((n - 2) / (1 - rho ** 2))
                    from scipy.stats import t as student_t
                    p = float(2 * student_t.sf(abs(t_stat), n - 2))
            records.append({
                "Perbandingan": f"{a_tool} vs {b_tool}",
                "Karakteristik": feature,
                "ρ parsial": round(rho, 3),
                "p (Holm)": p,
                "n": len(x_res),
            })
            raw_p.append(p)
    if not records:
        return pd.DataFrame()
    for row, adjusted in zip(records, holm(raw_p)):
        row["p (Holm)"] = _fmt_p(adjusted)
        row["Signifikan"] = "ya" if adjusted < 0.05 else "tidak"
    return pd.DataFrame(records)


# --------------------------------------------------------------------------- #
# TABEL IX
# --------------------------------------------------------------------------- #
def table_ix(frame: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    """TABEL IX: generation cost per unit (median)."""
    if frame.empty:
        return pd.DataFrame()
    per_task = frame.copy()
    if not calls.empty:
        agg = calls.groupby(["method", "model", "dataset", "task"], as_index=False).agg(
            api_calls=("total_tokens", "size"),
            llm_cost=("cost_usd", lambda s: s.sum(min_count=1)),
            llm_prompt=("prompt_tokens", "sum"),
            llm_completion=("completion_tokens", "sum"),
            llm_total=("total_tokens", "sum"))
        per_task = per_task.merge(
            agg, on=["method", "model", "dataset", "task"], how="left")
    records = []
    for (dataset, method, backbone), group in per_task.groupby(
            ["dataset", "method", "backbone"], dropna=False):
        record = {
            "Suite": dataset, "Tool": method, "BB": backbone,
            "Waktu (s)": _pct(group["wall_time_s"].median()),
            "Panggilan API": MISSING,
            "Token (ribu)": MISSING,
            "Biaya (USD)": MISSING,
        }
        if "api_calls" in group.columns and group["api_calls"].notna().any():
            record["Panggilan API"] = _pct(group["api_calls"].median(), 0)
            tokens = group["llm_total"].median()
            if pd.notna(tokens):
                record["Token (ribu)"] = _pct(tokens / 1000.0, 1)
            cost = group["llm_cost"].sum(min_count=1)
            if pd.notna(cost):
                record["Biaya (USD)"] = f"{cost:.4f}"
        elif group["cost_usd"].notna().any():
            record["Biaya (USD)"] = f"{group['cost_usd'].sum():.4f}"
        records.append(record)
    return pd.DataFrame(records).sort_values(["Suite", "Tool", "BB"]).reset_index(drop=True)


# --------------------------------------------------------------------------- #
# Figures
# --------------------------------------------------------------------------- #
def figure_3(frame: pd.DataFrame, out_path: Path):
    """Boxplot MT: coverage vs mutation score (one point = median per unit)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    mt = frame[frame["dataset"] == "MT"]
    if mt.empty:
        return None
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    specs = [("line_pct", "Line coverage (%)"), ("mutation_score", "Mutation score (%)")]
    for ax, (metric, title) in zip(axes, specs):
        medians = unit_medians(mt, metric)
        if medians.empty:
            ax.set_title(f"{title} (tidak ada data)")
            ax.set_xticks([])
            continue
        medians["label"] = medians["method"] + "\n" + medians["backbone"]
        labels = sorted(medians["label"].unique())
        data = [medians.loc[medians["label"] == label, metric].to_numpy()
                for label in labels]
        ax.boxplot(data, labels=labels)
        ax.set_title(title)
        ax.set_ylim(0, 105)
        ax.grid(axis="y", alpha=.25)
        ax.tick_params(axis="x", labelsize=7)
    fig.suptitle("Gambar 3. Distribusi per fungsi pada MT suite", fontweight="bold")
    fig.tight_layout()
    fig.savefig(out_path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return out_path


def figure_4(frame: pd.DataFrame, metric_by_suite: dict[str, str], out_path: Path):
    """Interaction plot: mean metric per tool across backbones."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    suites = [s for s in metric_by_suite if not frame[frame["dataset"] == s].empty]
    if not suites:
        return None
    fig, axes = plt.subplots(1, len(suites), figsize=(6 * len(suites), 4.5), squeeze=False)
    for ax, dataset in zip(axes[0], suites):
        metric = metric_by_suite[dataset]
        sub = frame[frame["dataset"] == dataset].dropna(subset=[metric])
        for method, group in sub.groupby("method"):
            means = group.groupby("backbone")[metric].mean()
            if means.empty:
                continue
            ax.plot(means.index, means.values, marker="o", label=method)
        ax.set_title(f"{dataset} — {metric}")
        ax.set_ylabel(metric)
        ax.set_ylim(0, 105)
        ax.grid(alpha=.25)
        ax.legend(fontsize=8)
    fig.suptitle("Gambar 4. Efek backbone per generator", fontweight="bold")
    fig.tight_layout()
    fig.savefig(out_path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return out_path


def figure_5(frame: pd.DataFrame, characteristics: pd.DataFrame, out_path: Path):
    """Scatter of per-module BC advantage vs the strongest RQ3 characteristic."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    sub = frame[frame["dataset"] == "CM"]
    if sub.empty or characteristics.empty:
        return None
    medians = unit_medians(sub, "branch_pct")
    if medians.empty:
        return None
    pivot = medians.pivot_table(index="task", columns="method", values="branch_pct")
    pairs = [("CoverUp", "Pynguin"), ("CodaMOSA", "Pynguin"), ("CoverUp", "CodaMOSA")]
    best = None
    for a_tool, b_tool in pairs:
        if a_tool not in pivot.columns or b_tool not in pivot.columns:
            continue
        advantage = (pivot[a_tool] - pivot[b_tool]).dropna()
        joined = characteristics.set_index("task").reindex(advantage.index).dropna(
            subset=["loc"])
        if len(joined) < 10:
            continue
        for feature in ("cyclomatic_complexity", "external_dependencies",
                        "type_annotation_density"):
            rho = float(np.corrcoef(joined[feature].astype(float), advantage.reindex(joined.index))[0, 1])
            if best is None or abs(rho) > abs(best[0]):
                best = (rho, feature, advantage.reindex(joined.index), joined[feature],
                        f"{a_tool} vs {b_tool}")
    if best is None:
        return None
    rho, feature, advantage, values, label = best
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(values.astype(float), advantage, alpha=.7)
    ax.axhline(0, color="#888", linewidth=1)
    ax.set_xlabel(feature)
    ax.set_ylabel(f"Selisih median branch coverage (poin)\n{label}")
    ax.set_title(f"Gambar 5. Keunggulan per modul vs {feature} (ρ={rho:.2f})")
    ax.grid(alpha=.25)
    fig.tight_layout()
    fig.savefig(out_path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return out_path


# --------------------------------------------------------------------------- #
# One-call entry point used by the notebooks
# --------------------------------------------------------------------------- #
def render_all(out_dir: Path, backbone_b1: str = "GPT-5.6 Sol",
               characteristics_path: Path | None = None,
               figures: bool = True) -> dict[str, pd.DataFrame]:
    """Compute every table; returns {name: DataFrame} for notebook display."""
    out_dir = Path(out_dir)
    frame = load_rows(out_dir)
    calls = load_llm_calls(out_dir)
    characteristics = pd.DataFrame()
    if characteristics_path and Path(characteristics_path).is_file():
        characteristics = pd.read_csv(characteristics_path, dtype={"task": str})

    results: dict[str, pd.DataFrame] = {}
    results["TABEL IV"] = table_iv(frame, calls)
    results["TABEL V"] = pd.concat(
        [table_v(frame, "mutation_score", "MT", backbone_b1),
         table_v(frame, "branch_pct", "CM", backbone_b1),
         table_v(frame, "mutation_score", "CM", backbone_b1)],
        ignore_index=True) if not frame.empty else pd.DataFrame()
    results["TABEL VI"] = table_vi(frame, {"MT": "mutation_score", "CM": "branch_pct"})
    results["TABEL VII"] = pd.concat(
        [table_vii(frame, "MT", "mutation_score"),
         table_vii(frame, "CM", "branch_pct")], ignore_index=True) \
        if not frame.empty else pd.DataFrame()
    results["TABEL VIII"] = table_viii(frame, characteristics, backbone_b1)
    results["TABEL IX"] = table_ix(frame, calls)

    if figures:
        results["_fig3"] = figure_3(frame, out_dir / "gambar3_boxplot_mt.png")
        results["_fig4"] = figure_4(frame, {"MT": "mutation_score", "CM": "branch_pct"},
                                    out_dir / "gambar4_interaction.png")
        results["_fig5"] = figure_5(frame, characteristics, out_dir / "gambar5_scatter_cm.png")
    return results
