from concurrent.futures import ThreadPoolExecutor, as_completed


def _cleanup_codamosa_containers():
    """Remove only containers created by this experiment's CodaMOSA runner.

    ``docker run --rm`` normally cleans up, but interrupted notebook kernels can
    leave Created/Running containers behind.  Labels make the cleanup targeted
    so unrelated Docker workloads are never touched.
    """
    try:
        cp = subprocess.run(
            ["docker", "ps", "-aq", "--filter", "label=teori.experiment=codamosa"],
            capture_output=True, text=True, timeout=30,
        )
        ids = [x for x in cp.stdout.split() if x]
        if ids:
            subprocess.run(["docker", "rm", "-f", *ids], capture_output=True,
                           text=True, timeout=120)
            print(f"Cleaned {len(ids)} CodaMOSA experiment container(s).")
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        print("Container cleanup warning:", exc)


# Remove leftovers from an earlier interrupted run before allocating resources.
_cleanup_codamosa_containers()

_task_jobs = [(dataset, str(task))
              for dataset, task_ids in TASKS.items()
              for task in task_ids]
try:
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
finally:
    _cleanup_codamosa_containers()
