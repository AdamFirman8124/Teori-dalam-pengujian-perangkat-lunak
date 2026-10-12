"""Unit tests for task-level generator retry policy used by the notebook."""

from pathlib import Path


BODY = Path(__file__).resolve().parents[1] / "src" / "parallel_loop_body.py"


def _load_retry_helpers(monkeypatch, attempts=3, delay=0):
    source = BODY.read_text(encoding="utf-8")
    prefix = source.split("def _blocked_record", 1)[0]
    namespace = {
        "RESUME_KEYS": set(),
        "GENERATOR_ATTEMPTS": attempts,
        "GENERATOR_RETRY_SECONDS": delay,
        "time": __import__("time"),
    }
    exec(compile(prefix, str(BODY), "exec"), namespace)
    sleeps = []
    monkeypatch.setattr(namespace["time"], "sleep", sleeps.append)
    return namespace, sleeps


def test_transient_provider_error_is_retried(monkeypatch):
    helpers, sleeps = _load_retry_helpers(monkeypatch, attempts=3, delay=2)
    calls = []

    def runner():
        calls.append(1)
        if len(calls) < 3:
            raise RuntimeError("503 Service Unavailable from upstream service")
        return "ok"

    result = helpers["_run_with_retries"](
        "CODAMOSA", "model", "HumanEval", "1", runner
    )

    assert result == "ok"
    assert len(calls) == 3
    assert sleeps == [2, 4]


def test_coverup_zero_exit_with_transient_log_is_retried(monkeypatch):
    helpers, _ = _load_retry_helpers(monkeypatch, attempts=2)
    calls = []

    def runner():
        calls.append(1)
        if len(calls) == 1:
            raise RuntimeError(
                "CoverUp tidak menghasilkan test setelah generator berhenti. "
                "Log run terbaru:\n503 Service Unavailable from upstream service"
            )
        return "ok"

    assert helpers["_run_with_retries"](
        "CoverUp", "model", "Refactory", "q5", runner
    ) == "ok"
    assert len(calls) == 2


def test_coverup_exhausted_generation_is_not_retried(monkeypatch):
    helpers, sleeps = _load_retry_helpers(monkeypatch, attempts=3, delay=2)
    calls = []

    def runner():
        calls.append(1)
        raise RuntimeError(
            "CoverUp tidak menghasilkan test setelah generator berhenti. "
            "Log run terbaru:\nToo many attempts, giving up"
        )

    try:
        helpers["_run_with_retries"](
            "CoverUp", "model", "HumanEval", "0", runner
        )
    except RuntimeError as exc:
        assert "Too many attempts" in str(exc)
    else:
        raise AssertionError("exhausted generation must be raised immediately")

    assert len(calls) == 1
    assert sleeps == []


def test_coverup_no_coverage_progress_is_not_retried(monkeypatch):
    helpers, sleeps = _load_retry_helpers(monkeypatch, attempts=3, delay=2)
    calls = []

    def runner():
        calls.append(1)
        raise RuntimeError(
            "CoverUp tidak menghasilkan test setelah generator berhenti. "
            "Log run terbaru:\nTest doesn't improve coverage"
        )

    try:
        helpers["_run_with_retries"](
            "CoverUp", "model", "HumanEval", "1", runner
        )
    except RuntimeError as exc:
        assert "improve coverage" in str(exc)
    else:
        raise AssertionError("no-progress generation must be raised immediately")

    assert len(calls) == 1
    assert sleeps == []


def test_invalid_generated_suite_is_not_retried(monkeypatch):
    helpers, sleeps = _load_retry_helpers(monkeypatch, attempts=3, delay=2)
    calls = []

    def runner():
        calls.append(1)
        raise RuntimeError("INVALID_GENERATED_TEST: no test functions")

    try:
        helpers["_run_with_retries"](
            "CODAMOSA", "model", "Refactory", "q3", runner
        )
    except RuntimeError as exc:
        assert "INVALID_GENERATED_TEST" in str(exc)
    else:
        raise AssertionError("invalid suite must be raised immediately")

    assert len(calls) == 1
    assert sleeps == []


def test_non_transient_program_error_is_not_retried(monkeypatch):
    helpers, _ = _load_retry_helpers(monkeypatch, attempts=3)
    calls = []

    def runner():
        calls.append(1)
        raise IndexError("list index out of range")

    try:
        helpers["_run_with_retries"](
            "CODAMOSA", "model", "HumanEval", "1", runner
        )
    except IndexError:
        pass
    else:
        raise AssertionError("non-transient errors must not be retried")



def test_coverup_connection_error_then_giving_up_is_retried(monkeypatch):
    """When CoverUp's internal retry budget exhausts after a transient connection
    error it ends with 'giving up'.  Since a real transient marker is present,
    the notebook must still retry the whole task (not fail fast)."""
    helpers, sleeps = _load_retry_helpers(monkeypatch, attempts=3, delay=2)
    calls = []

    def runner():
        calls.append(1)
        # Simulate CoverUp retrying internally, hitting a transient connection
        # error 3 times, then giving up with that error still visible in the log.
        if len(calls) < 3:
            raise RuntimeError(
                "CoverUp tidak menghasilkan test setelah generator berhenti. "
                "Log run terbaru:\n"
                "Error: <class 'litellm.exceptions.InternalServerError'>\n"
                "InternalServerError: OpenAIException - Connection error\n"
                "giving up"
            )
        return "ok"

    assert helpers["_run_with_retries"](
        "CoverUp", "model", "HumanEval", "0", runner
    ) == "ok"
    assert len(calls) == 3
    assert sleeps == [2, 4]   # exponential back-off: delay * attempt


def test_coverup_deterministic_exhaustion_not_retried(monkeypatch):
    """Deterministic exhaustion ('Too many attempts') contains no transient marker
    and must not be retried."""
    helpers, sleeps = _load_retry_helpers(monkeypatch, attempts=3, delay=2)
    calls = []

    def runner():
        calls.append(1)
        raise RuntimeError(
            "CoverUp tidak menghasilkan test setelah generator berhenti. "
            "Log run terbaru:\nToo many attempts, giving up"
        )

    try:
        helpers["_run_with_retries"](
            "CoverUp", "model", "HumanEval", "1", runner
        )
    except RuntimeError as exc:
        assert "Too many attempts" in str(exc)
    else:
        raise AssertionError("deterministic exhaustion must be raised immediately")

    assert len(calls) == 1
    assert sleeps == []

    assert len(calls) == 1
