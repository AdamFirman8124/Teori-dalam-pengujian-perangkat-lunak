import ast, json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
nb = json.loads((ROOT / "experiments_codamosa_coverup.ipynb").read_text())
def get(cid):
    return "".join(next(c for c in nb["cells"] if c.get("id")==cid)["source"])
setup = get("c5d09b00")
exp = get("4ce9652a")
fin = get("dc51281c")
checks = {}
checks["json_valid"] = True
for i,c in enumerate(nb["cells"]):
    if c.get("cell_type")=="code":
        ast.parse("".join(c["source"]))
analysis = get("valid-comparison-chart")
checks["analysis_ok_rows_only"] = 'x.get("status") == "OK"' in analysis
checks["analysis_per_dataset"] = 'groupby(["dataset", "task"]' in analysis
checks["analysis_mutant_identity"] = "mutant_set_id" in analysis
checks["analysis_assertion_evidence"] = "n_assertions_evaluated" in analysis
checks["analysis_chart_saved"] = 'OUT / "comparison.png"' in analysis
checks["setup_task_workers"] = "TASK_WORKERS = max(1, int(os.getenv('TASK_WORKERS', '2')))" in setup
checks["setup_task_limit"] = "os.getenv('TASK_LIMIT', 'all')" in setup
checks["setup_pop5"] = "os.getenv('CODAMOSA_POPULATION', '5')" in setup
checks["setup_analysis_packages"] = all(
    name in setup for name in ("'numpy'", "'pandas'", "'matplotlib'")
)
checks["exp_has_executor"] = "ThreadPoolExecutor" in exp and "_run_one_task" in exp
checks["exp_single_checkpoint"] = exp.count("store.checkpoint(")==1
checks["exp_no_serial_matrix"] = "for dataset, task_ids in TASKS.items():\n    for task in task_ids:" not in exp
checks["exp_helpers_kept"] = "_run_coverup_task_with_model" in exp and "_run_codamosa_task_with_model" in exp
checks["exp_resume_kept"] = "RESUME_KEYS" in exp
checks["fin_no_checkpoint"] = "store.checkpoint(" not in fin
env = (ROOT / "config" / ".env.example").read_text()
checks["env_task_limit"] = "TASK_LIMIT=5" in env
checks["env_task_workers"] = "TASK_WORKERS=1" in env
checks["env_mut_workers"] = "EVAL_MUTANT_WORKERS=1" in env
for k,v in checks.items():
    print(k, v)
assert all(checks.values()), checks
print("ALL CHECKS PASSED")
