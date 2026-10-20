import json
import os

from tools.classify_failures import classify, latest_status, summarize


def _status(status, message):
    return {
        "method": "CODAMOSA",
        "model": "auto",
        "dataset": "MT",
        "task": "f001",
        "status": status,
        "message": message,
    }


def test_classifies_success():
    result = classify(_status("OK", "Generation and evaluation completed."))
    assert result["failure_category"] == "success"
    assert result["recommended_retry"] is False


def test_invalid_suite_is_model_failure():
    result = classify(_status(
        "INVALID_GENERATED_TEST",
        "INVALID_GENERATED_TEST: no test functions (empty/comment-only suite)",
    ))
    assert result["failure_category"] == "model_failure"
    assert result["failure_reason"] == "INVALID_SUITE"
    assert result["recommended_retry"] is False


def test_oom_overrides_embedded_rate_limit():
    result = classify(_status(
        "BLOCKED",
        "CODAMOSA_OOM: Docker exit code 137/SIGKILL. account rate limit reached",
    ))
    assert result["failure_category"] == "infrastructure_failure"
    assert result["failure_reason"] == "OUT_OF_MEMORY"
    assert result["recommended_retry"] is True


def test_mount_failure_is_infrastructure_failure():
    result = classify(_status(
        "BLOCKED",
        "Docker exit code 1: ERROR: You need to specify a mount to /input",
    ))
    assert result["failure_category"] == "infrastructure_failure"
    assert result["failure_reason"] == "CONTAINER_MOUNT"


def test_coverup_no_test_is_model_failure():
    result = classify(_status(
        "BLOCKED",
        "CoverUp tidak menghasilkan test setelah generator berhenti. Too many attempts, giving up",
    ))
    assert result["failure_category"] == "model_failure"
    assert result["failure_reason"] == "NO_GENERATED_TEST"
    assert result["recommended_retry"] is False


def test_summary_separates_retry_and_model_failures(tmp_path):
    records = [
        classify(_status("OK", "done")),
        classify(_status("BLOCKED", "Docker exit code 137/SIGKILL")),
        classify(_status("INVALID_GENERATED_TEST", "no assertions")),
    ]
    summary = summarize(records, tmp_path / "status.json", "run-1")
    assert summary["category_counts"] == {
        "infrastructure_failure": 1,
        "model_failure": 1,
        "success": 1,
    }
    assert len(summary["retry_keys"]) == 1
    assert len(summary["model_failure_keys"]) == 1


def test_latest_status_prefers_newest_candidate(tmp_path):
    source = tmp_path / "experiment_results"
    old = source / "runs" / "old"
    new = source / "runs" / "new"
    old.mkdir(parents=True)
    new.mkdir(parents=True)
    (old / "status.json").write_text(json.dumps([]), encoding="utf-8")
    (new / "status.json").write_text(json.dumps([]), encoding="utf-8")
    old_path = old / "status.json"
    new_path = new / "status.json"
    os.utime(old_path, (1, 1))
    os.utime(new_path, (2, 2))
    selected, run_id = latest_status(source)
    assert selected == new_path
    assert run_id == "new"
