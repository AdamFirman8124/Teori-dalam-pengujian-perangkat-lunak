#!/usr/bin/env python3
from __future__ import annotations

import csv
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from matrix import generate_matrix
from protocol import load_config
from results_schema import FIELDS

rng = random.Random(20261022)
config = load_config()
matrix_path = ROOT / "results" / "run_matrix.csv"
generate_matrix(matrix_path, pilot=False)
rows = list(csv.DictReader(matrix_path.open(newline="", encoding="utf-8")))
out = []
for row in rows:
    tool = row["tool"]
    suite = row["suite"]
    backbone = row["backbone"]
    quality = (7 if tool == "CoverUp" else 3) + (-3 if backbone == "B2" else 0) + rng.gauss(0, 8)
    branches_total = rng.randint(2, 50)
    lines_total = rng.randint(15, 500)
    bc = max(0, min(100, (82 if suite == "MT" else 55) + quality))
    lc = max(0, min(100, bc + rng.uniform(5, 15)))
    mutants = rng.randint(1, 35)
    ms = max(0, min(100, (62 if suite == "MT" else 48) + quality + rng.gauss(0, 5)))
    tokens_in = rng.randint(1000, 12000)
    tokens_out = rng.randint(500, 5000)
    price = config["backbones"][backbone]
    cost = tokens_in * price["input_usd_per_million"] / 1_000_000 + tokens_out * price["output_usd_per_million"] / 1_000_000
    failed = rng.random() < 0.02
    now = datetime.now(timezone.utc).isoformat()
    record = {field: "" for field in FIELDS}
    record.update(row)
    record.update({
        "tool_version": "simulated",
        "model_returned": price["model_requested"],
        "start_time": now,
        "end_time": now,
        "budget_s": 600,
        "gen_time_s": round(rng.uniform(15, 600), 3),
        "ratelimit_wait_s": round(rng.uniform(0, 20), 3),
        "hit_budget": int(rng.random() < 0.08),
        "wait_flag": 0,
        "attempt": 1,
        "status": "failed" if failed else "ok",
        "error_category": "timeout" if failed else "",
        "n_api_calls": rng.randint(1, 80),
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
        "cost_usd": round(cost, 8),
        "n_raw_proposals": rng.randint(2, 20),
        "n_raw_pass": rng.randint(1, 2),
        "n_tests_final": rng.randint(1, 20),
        "n_pass_first": rng.randint(1, 20),
        "n_fail": int(failed),
        "n_error": 0,
        "n_timeout": 0,
        "k_reruns": 5,
        "n_flaky": int(rng.random() < 0.01),
        "n_valid": rng.randint(1, 20),
        "lines_total": lines_total,
        "lines_exec": round(lines_total * lc / 100),
        "branches_total": branches_total,
        "branches_exec": round(branches_total * bc / 100),
        "mutation_tool": "cosmic-ray",
        "n_mutants": mutants,
        "n_killed": round(mutants * ms / 100),
        "n_survived": mutants - round(mutants * ms / 100),
        "n_mutant_timeout": rng.randint(0, 1),
        "sim_max_median": round(rng.random(), 4),
    })
    if failed:
        for field in ("lines_exec", "branches_exec", "n_killed", "n_survived"):
            record[field] = ""
    out.append(record)
with (ROOT / "results" / "results_sim.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(out)
print(f"Wrote {len(out)} simulated rows")
