#!/usr/bin/env python3
"""Fase 4 pedoman: module characteristics + stratified CM sample.

Menghitung ``loc``, ``sloc``, ``n_branches`` untuk seluruh 425 modul CM,
memilih 3 modul pilot, lalu mengambil sampel acak bertingkat 3x3
(tertil LOC x tertil n_branches) minimal 40 modul dengan seed tetap dan
batas maksimum 25% modul dari satu proyek.

Keluaran:
  experiment_results_linux/module_characteristics.csv
  experiment_results_linux/cm_sample.csv

Jalankan:
  .venv/bin/python tools/build_cm_sample.py [--out DIR] [--seed 20261021]
"""
from __future__ import annotations

import argparse
import ast
import csv
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import eval_metrics as em  # noqa: E402

BRANCH_NODES = (ast.If, ast.For, ast.While, ast.Try, ast.IfExp,
                ast.With, ast.AsyncFor, ast.AsyncWith, ast.Assert)


def count_branches(path: Path) -> int:
    """Jumlah titik percabangan AST sesuai definisi Bagian 13 pedoman."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return 0
    total = 0
    for node in ast.walk(tree):
        if isinstance(node, BRANCH_NODES):
            total += 1
        if isinstance(node, ast.BoolOp):
            total += len(node.values) - 1
        if hasattr(ast, "Match") and isinstance(node, ast.Match):
            total += len(node.cases)
    return total


def raw_metrics(path: Path) -> tuple[int, int]:
    """(loc, sloc) via radon, fallback to manual counting."""
    try:
        from radon.raw import analyze
        result = analyze(path.read_text(encoding="utf-8", errors="replace"))
        return int(result.loc), int(result.sloc)
    except Exception:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        sloc = sum(1 for line in lines
                   if line.strip() and not line.strip().startswith("#"))
        return len(lines), sloc


def tertile(values: list[float]) -> tuple[float, float]:
    ordered = sorted(values)
    if not ordered:
        return 0.0, 0.0
    n = len(ordered)
    return ordered[n // 3], ordered[(2 * n) // 3]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="experiment_results_linux")
    parser.add_argument("--seed", type=int, default=20261021)
    parser.add_argument("--min-sample", type=int, default=40)
    parser.add_argument("--max-project-share", type=float, default=0.25)
    args = parser.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    modules = em.cm_modules()
    if not modules:
        print("ERROR: cm_modules.csv tidak terbaca", file=sys.stderr)
        return 1

    records = []
    for pkg_col, dotted, path in modules:
        loc, sloc = raw_metrics(path)
        records.append({
            "unit_id": dotted,
            "project": Path(pkg_col).name,
            "loc": loc,
            "sloc": sloc,
            "n_branches": count_branches(path),
            "stratum": "",
            "is_pilot": 0,
            "in_sample": 0,
        })
    print(f"modules: {len(records)}")

    loc_low, loc_high = tertile([r["loc"] for r in records])
    br_low, br_high = tertile([r["n_branches"] for r in records])

    def loc_band(v: int) -> int:
        return 0 if v <= loc_low else (1 if v <= loc_high else 2)

    def br_band(v: int) -> int:
        return 0 if v <= br_low else (1 if v <= br_high else 2)

    for r in records:
        r["stratum"] = f"L{loc_band(r['loc'])}B{br_band(r['n_branches'])}"

    rng = random.Random(args.seed)

    # Pilot: 3 modul kecil dari proyek berbeda, dikeluarkan dari sampel.
    by_project_smallest = {}
    for r in sorted(records, key=lambda x: (x["loc"], x["n_branches"])):
        by_project_smallest.setdefault(r["project"], r)
    pilots = list(by_project_smallest.values())[:3]
    for r in pilots:
        r["is_pilot"] = 1
    pilot_ids = {r["unit_id"] for r in pilots}
    print("pilot:", sorted(pilot_ids))

    candidates = [r for r in records if r["unit_id"] not in pilot_ids]

    # Stratified sampling: round-robin across strata, respecting project cap.
    strata: dict[str, list[dict]] = defaultdict(list)
    for r in candidates:
        strata[r["stratum"]].append(r)
    for group in strata.values():
        rng.shuffle(group)

    cap = max(1, int(args.min_sample * args.max_project_share))
    chosen: list[dict] = []
    project_count: Counter[str] = Counter()
    strata_keys = sorted(strata)
    progress = True
    while progress and len(chosen) < args.min_sample:
        progress = False
        for key in strata_keys:
            if len(chosen) >= args.min_sample:
                break
            while strata[key]:
                candidate = strata[key].pop()
                if project_count[candidate["project"]] >= cap:
                    continue
                candidate["in_sample"] = 1
                chosen.append(candidate)
                project_count[candidate["project"]] += 1
                progress = True
                break

    if len(chosen) < args.min_sample:
        print(f"WARNING: hanya {len(chosen)} modul memenuhi batas proyek; "
              f"target {args.min_sample}", file=sys.stderr)

    columns = ["unit_id", "project", "loc", "sloc", "n_branches",
               "stratum", "is_pilot", "in_sample"]
    with (out / "module_characteristics.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns)
        writer.writeheader()
        writer.writerows(records)

    sample = [r for r in records if r["in_sample"]]
    with (out / "cm_sample.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns)
        writer.writeheader()
        writer.writerows(sample)

    print(f"sample: {len(sample)} modules from {len({r['project'] for r in sample})} projects")
    print("strata:", dict(Counter(r["stratum"] for r in sample)))
    print("per project:", dict(Counter(r["project"] for r in sample).most_common()))
    print(f"wrote {out/'module_characteristics.csv'} and {out/'cm_sample.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
