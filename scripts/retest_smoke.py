#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import eval_metrics as em

paths = list((ROOT / "results" / "generated" / "MT-coverup-B1-f003-r01" / "tests").glob("test_*.py"))
workroot = ROOT / "results" / "work_test"
workroot.mkdir(parents=True, exist_ok=True)
row = em.evaluate("MT", "f003", paths, "CoverUp", wall_time_s=1.0, workroot=workroot)
keys = ["line_pct", "branch_pct", "pass_rate", "n_tests", "n_passed", "flaky_count", "mutation_score", "n_mutants"]
print(json.dumps({key: row.get(key) for key in keys}, indent=1))
print("error:", row.get("error"))
