import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
notebook_path = ROOT / "experiments_codamosa_coverup.ipynb"
env_example = ROOT / "config" / ".env.example"
nb = json.loads(notebook_path.read_text(encoding="utf-8"))


def cell_by_id(cell_id):
    for cell in nb["cells"]:
        if cell.get("id") == cell_id:
            return cell
    raise KeyError(cell_id)


def text(cell):
    return "".join(cell["source"])


def put(cell, value):
    cell["source"] = value.splitlines(keepends=True)


# Keep setup changes idempotent. Parallelism is configured in the notebook
# and environment files, not inserted by this patch script.
setup = cell_by_id("c5d09b00")
s = text(setup)
s = s.replace(
    "_task_limit_raw = os.getenv('TASK_LIMIT', '1').strip()",
    "_task_limit_raw = os.getenv('TASK_LIMIT', 'all').strip()",
)
s = s.replace(
    "CODAMOSA_POPULATION = int(os.getenv('CODAMOSA_POPULATION', '50'))",
    "CODAMOSA_POPULATION = int(os.getenv('CODAMOSA_POPULATION', '5'))",
    1,
)
put(setup, s)

task_cell = cell_by_id("4ce9652a")
s = text(task_cell)
start_marker = "# Matrix: method x model x dataset x task. Each model has isolated outputs."
start = s.find(start_marker)
if start < 0:
    raise RuntimeError("serial matrix loop start not found")
# The notebook embeds src/parallel_loop_body.py + src/parallel_loop_driver.py
# verbatim after the task-runner head, so syncing is deterministic: keep the
# head, replace everything from the marker onward with the current sources.
head = s[:start]
body = (ROOT / "src" / "parallel_loop_body.py").read_text(encoding="utf-8").rstrip()
driver = (ROOT / "src" / "parallel_loop_driver.py").read_text(encoding="utf-8").rstrip()
put(task_cell, head + body + "\n\n\n" + driver + "\n")
notebook_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print("synced notebook cell 6 from src/parallel_loop_body.py + src/parallel_loop_driver.py")
raise SystemExit(0)

_checkpoint_marker = '        print(f"Checkpoint after {dataset} {task}: rows={len(rows)} statuses={len(statuses)}")'
end = s.find(checkpoint_marker, start)
if end < 0:
    raise RuntimeError("serial matrix loop end not found")
end = s.find("\n", end)
if end < 0:
    end = len(s)

parallel_loop = r'''# Matrix: method x model x dataset x task. Each model has isolated outputs.
# Workers return data only; the main thread merges and checkpoints serially.
def _done(method, model, dataset, task):
    return (method, model, dataset, str(task)) in RESUME_KEYS


def _blocked_record(method, dataset, task, reason):
    item = {
        "method": method,
        "dataset": dataset,
        "task": str(task),
        "status": "BLOCKED",
        "message": redact(reason),
    }
    print("\n[" + method + " | " + dataset + " " + str(task) + "] BLOCKED")
    print(item["message"])
    return item


def _run_one_task(dataset, task):
    task_rows = []
    task_statuses = []

    if coverup_ok:
        for model in COVERUP_MODELS:
            if _done("CoverUp", model, dataset, task):
                print(f"RESUME skip CoverUp {model} {dataset} {task}")
                continue
            try:
                print("CoverUp mencoba model:", model, "|", dataset, task)
                row = _run_coverup_task_with_model(dataset, task, model)
                task_rows.append(row)
                task_statuses.append({
                    "method": "CoverUp", "model": model,
                    "dataset": dataset, "task": str(task),
                    "status": "OK",
                    "message": "Generation and evaluation completed.",
                })
                print("CoverUp OK", model, dataset, task)
            except Exception as exc:
                task_statuses.append(_blocked_record(
                    "CoverUp:" + model, dataset, task, explain_error(exc)
                ))
    else:
        for model in COVERUP_MODELS:
            if not _done("CoverUp", model, dataset, task):
                task_statuses.append(_blocked_record(
                    "CoverUp:" + model, dataset, task, coverup_reason
                ))

    if codamosa_ok:
        for model in CODAMOSA_MODELS:
            if _done("CODAMOSA", model, dataset, task):
                print(f"RESUME skip CODAMOSA {model} {dataset} {task}")
                continue
            try:
                print("CODAMOSA mencoba model:", model, "|", dataset, task)
                row = _run_codamosa_task_with_model(dataset, task, model)
                task_rows.append(row)
                task_statuses.append({
                    "method": "CODAMOSA", "model": model,
                    "dataset": dataset, "task": str(task),
                    "status": "OK",
                    "message": "Generation and evaluation completed.",
                })
                print("CODAMOSA OK", model, dataset, task)
            except Exception as exc:
                task_statuses.append(_blocked_record(
                    "CODAMOSA:" + model, dataset, task, explain_error(exc)
                ))
    else:
        for model in CODAMOSA_MODELS:
            if not _done("CODAMOSA", model, dataset, task):
                task_statuses.append(_blocked_record(
                    "CODAMOSA:" + model, dataset, task, codamosa_reason
                ))

    return task_rows, task_statuses
'''
parallel_driver = r'''

# Run independent tasks concurrently, but keep all shared result writes in the main thread.\nfrom concurrent.futures import ThreadPoolExecutor, as_completed\n\n_task_jobs = [\n    (dataset, str(task))\n    for dataset, task_ids in TASKS.items()\n    for task in task_ids\n]\nif _task_jobs:\n    _worker_count = min(TASK_WORKERS, len(_task_jobs))\n    print(f"Starting {_worker_count} parallel task workers for {len(_task_jobs)} tasks.")\n    with ThreadPoolExecutor(max_workers=_worker_count, thread_name_prefix="experiment-task") as _executor:\n        _future_to_task = {\n            _executor.submit(_run_one_task, dataset, task): (dataset, task)\n            for dataset, task in _task_jobs\n        }\n        for _future in as_completed(_future_to_task):\n            dataset, task = _future_to_task[_future]\n            try:\n                _task_rows, _task_statuses = _future.result()\n            except Exception as exc:\n                _task_rows, _task_statuses = [], []\n                for model in COVERUP_MODELS:\n                    if not _done("CoverUp", model, dataset, task):\n                        _task_statuses.append(_blocked_record(\n                            "CoverUp:" + model, dataset, task,\n                            "Unexpected task worker error: " + explain_error(exc),\n                        ))\n                for model in CODAMOSA_MODELS:\n                    if not _done("CODAMOSA", model, dataset, task):\n                        _task_statuses.append(_blocked_record(\n                            "CODAMOSA:" + model, dataset, task,\n                            "Unexpected task worker error: " + explain_error(exc),\n                        ))\n            rows.extend(_task_rows)\n            statuses.extend(_task_statuses)\n            store.checkpoint(rows, statuses)\n            print(f"Checkpoint after {dataset} {task}: rows={len(rows)} statuses={len(statuses)}")\nelse:\n    print("No tasks selected; nothing to run.")
'''
s = s[:start] + parallel_loop + parallel_driver + s[end:]
put(task_cell, s)

# Persist the patched notebook and configuration template.
env = env_example.read_text(encoding="utf-8")
env = env.replace("CODAMOSA_SEARCH_SECONDS=15", "CODAMOSA_SEARCH_SECONDS=60")
env = env.replace("EVAL_MUTANT_WORKERS=6", "EVAL_MUTANT_WORKERS=3")
env = env.replace(
    "# Gunakan 1 untuk pilot, lalu None/all untuk full run.\nTASK_LIMIT=1",
    "# Jalankan seluruh HumanEval + Refactory secara default. Untuk pilot, ubah menjadi 1.\nTASK_LIMIT=all",
)
if "TASK_WORKERS=" not in env:
    env = env.replace(
        "EVAL_MUTANT_WORKERS=3\n",
        "EVAL_MUTANT_WORKERS=3\n# Parallel task workers; 2 is tuned for a 6-core CPU.\nTASK_WORKERS=2\n",
    )
env_example.write_text(env, encoding="utf-8")
notebook_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print("patched parallel notebook and .env.example")
