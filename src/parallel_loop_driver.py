from concurrent.futures import ThreadPoolExecutor, as_completed

_task_jobs = [(dataset, str(task))
              for dataset, task_ids in TASKS.items()
              for task in task_ids]
if _task_jobs:
    _worker_count = min(TASK_WORKERS, len(_task_jobs))
    print(f"Starting {_worker_count} parallel task workers for {len(_task_jobs)} tasks.")
    with ThreadPoolExecutor(max_workers=_worker_count,
                            thread_name_prefix="experiment-task") as _executor:
        _future_to_task = {
            _executor.submit(_run_one_task, dataset, task): (dataset, task)
            for dataset, task in _task_jobs
        }
        for _future in as_completed(_future_to_task):
            dataset, task = _future_to_task[_future]
            try:
                _task_rows, _task_statuses = _future.result()
            except Exception as exc:
                _task_rows, _task_statuses = [], []
                _reason = "Unexpected task worker error: " + explain_error(exc)
                for model in COVERUP_MODELS:
                    if not _done("CoverUp", model, dataset, task):
                        _task_statuses.append(_blocked_record(
                            "CoverUp:" + model, dataset, task, _reason))
                for model in CODAMOSA_MODELS:
                    if not _done("CODAMOSA", model, dataset, task):
                        _task_statuses.append(_blocked_record(
                            "CODAMOSA:" + model, dataset, task, _reason))
            rows.extend(_task_rows)
            statuses.extend(_task_statuses)
            store.checkpoint(rows, statuses)
            print(f"Checkpoint after {dataset} {task}: rows={len(rows)} statuses={len(statuses)}")
else:
    print("No tasks selected; nothing to run.")
