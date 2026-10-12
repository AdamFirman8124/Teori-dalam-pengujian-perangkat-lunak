# Matrix: method x model x dataset x task. Each model has isolated outputs.
# Workers use isolated work directories and return data. Only the notebook's
# main thread mutates rows/statuses and writes checkpoints.
def _done(method, model, dataset, task):
    return (method, model, dataset, str(task)) in RESUME_KEYS


_TRANSIENT_ERROR_MARKERS = (
    "429", "rate limit", "too many requests", "502", "503", "504",
    "bad gateway", "service unavailable", "upstream service",
    "connectionerror", "connection error", "connection reset", "connection refused",
    "connection aborted", "network is unreachable", "temporary failure",
    "name resolution", "failed to resolve", "could not resolve", "dns",
    "timed out", "timeout", "docker daemon", "cannot connect to the docker",
    "no such host", "eof",
)


def _retryable_failure(exc, method):
    """Return whether an exception is safe to retry at the task boundary.

    Generated-suite validity is deterministic evidence, not a transient provider
    failure.  A transient HTTP/transport marker anywhere in the message is
    retryable -- including one preserved inside a CoverUp log excerpt, where the
    helper otherwise only sees "tidak menghasilkan test".

    CoverUp's *own* retry budget can still end in "giving up" after a transient
    connection error (e.g. ``InternalServerError: ... Connection error``).
    That is a provider hiccup, not a deterministic property of the task, so it
    stays retryable: the notebook then retries the whole invocation with a fresh
    connection.  Deterministic exhaustion ("Too many attempts") and
    no-coverage-progress outcomes carry no transient marker and fail fast
    instead of repeating a run that still costs another call.
    """
    text = str(exc).lower()
    if "invalid_generated_test" in text:
        return False
    return any(marker in text for marker in _TRANSIENT_ERROR_MARKERS)


def _check_budget(context):
    """Raise TokenBudgetExhausted when the remaining token quota is too low.

    Imported lazily so this file stays importable in the notebook's exec
    namespace (where ``src`` is already on sys.path) and in tests.
    """
    try:
        from token_budget import check_budget
    except ImportError:  # pragma: no cover - src not on path
        try:
            from src.token_budget import check_budget  # type: ignore
        except ImportError:
            return None
    return check_budget(context=context)


def _token_budget_exhausted_type():
    """Return the TokenBudgetExhausted class, or a never-raised placeholder."""
    try:
        from token_budget import TokenBudgetExhausted
    except ImportError:  # pragma: no cover
        try:
            from src.token_budget import TokenBudgetExhausted  # type: ignore
        except ImportError:
            class TokenBudgetExhausted(RuntimeError):  # type: ignore
                pass
    return TokenBudgetExhausted


TokenBudgetExhausted = _token_budget_exhausted_type()


def _run_with_retries(method, model, dataset, task, runner):
    last_exc = None
    for attempt in range(1, GENERATOR_ATTEMPTS + 1):
        # Stop before spending tokens we do not have: a paused run resumes from
        # its checkpoint once the provider quota is topped up again.
        _check_budget(f"{method}:{model} {dataset} {task} attempt {attempt}")
        try:
            return runner()
        except Exception as exc:  # noqa: BLE001 - per-task isolation boundary
            last_exc = exc
            retry = attempt < GENERATOR_ATTEMPTS and _retryable_failure(exc, method)
            if not retry:
                raise
            print(f"{method} {model} {dataset} {task}: attempt {attempt} transient failure; retry.")
            if GENERATOR_RETRY_SECONDS:
                time.sleep(GENERATOR_RETRY_SECONDS * attempt)
    raise last_exc  # pragma: no cover - loop always returns or raises above


def _blocked_record(method, dataset, task, reason):
    _reason = redact(reason)
    _status = "INVALID_GENERATED_TEST" if "INVALID_GENERATED_TEST" in _reason else "BLOCKED"
    _method, _sep, _model = method.partition(":")
    item = {"method": _method, "model": _model if _sep else None,
            "dataset": dataset, "task": str(task),
            "status": _status, "message": _reason}
    print("\n[" + method + " | " + dataset + " " + str(task) + "] " + _status)
    print(item["message"])
    return item


def _run_one_task(dataset, task):
    task_rows, task_statuses = [], []
    if coverup_ok:
        for model in COVERUP_MODELS:
            if _done("CoverUp", model, dataset, task):
                print(f"RESUME skip CoverUp {model} {dataset} {task}")
                continue
            try:
                print("CoverUp mencoba model:", model, "|", dataset, task)
                row = _run_with_retries(
                    "CoverUp", model, dataset, task,
                    lambda: _run_coverup_task_with_model(dataset, task, model),
                )
                task_rows.append(row)
                task_statuses.append({"method": "CoverUp", "model": model,
                    "dataset": dataset, "task": str(task), "status": "OK",
                    "message": "Generation and evaluation completed."})
                print("CoverUp OK", model, dataset, task)
            except Exception as exc:
                task_statuses.append(_blocked_record(
                    "CoverUp:" + model, dataset, task, explain_error(exc)))
    else:
        for model in COVERUP_MODELS:
            if not _done("CoverUp", model, dataset, task):
                task_statuses.append(_blocked_record(
                    "CoverUp:" + model, dataset, task, coverup_reason))

    if codamosa_ok:
        for model in CODAMOSA_MODELS:
            if _done("CODAMOSA", model, dataset, task):
                print(f"RESUME skip CODAMOSA {model} {dataset} {task}")
                continue
            try:
                print("CODAMOSA mencoba model:", model, "|", dataset, task)
                row = _run_with_retries(
                    "CODAMOSA", model, dataset, task,
                    lambda: _run_codamosa_task_with_model(dataset, task, model),
                )
                task_rows.append(row)
                task_statuses.append({"method": "CODAMOSA", "model": model,
                    "dataset": dataset, "task": str(task), "status": "OK",
                    "message": "Generation and evaluation completed."})
                print("CODAMOSA OK", model, dataset, task)
            except Exception as exc:
                task_statuses.append(_blocked_record(
                    "CODAMOSA:" + model, dataset, task, explain_error(exc)))
    else:
        for model in CODAMOSA_MODELS:
            if not _done("CODAMOSA", model, dataset, task):
                task_statuses.append(_blocked_record(
                    "CODAMOSA:" + model, dataset, task, codamosa_reason))
    return task_rows, task_statuses
