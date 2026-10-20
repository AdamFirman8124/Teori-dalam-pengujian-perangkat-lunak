"""Regression tests for generated-suite validity and mutant-set identity."""

from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import eval_metrics as em  # noqa: E402
import experiment_storage as storage  # noqa: E402


@pytest.mark.parametrize(
    ("name", "source", "expected_valid", "expected_assertions", "reason_part"),
    [
        ("valid_assert.py", "def test_value():\n    assert value() == 1\n",
         True, 1, "valid"),
        ("valid_raises.py", "import pytest\ndef test_error():\n"
         "    with pytest.raises(ValueError):\n        value(-1)\n",
         True, 1, "valid"),
        ("valid_unittest.py", "class TestValue:\n"
         "    def test_error(self):\n"
         "        with self.assertRaises(ValueError):\n            value(-1)\n",
         True, 1, "valid"),
        ("comment_only.py", "# generated suite header only\n",
         False, 0, "no test functions"),
        ("assertion_free.py", "def test_value():\n    value()\n",
         False, 0, "no assertions"),
        ("swallowed.py", "def test_value():\n    try:\n"
         "        assert value() == 1\n    except BaseException:\n        pass\n",
         False, 0, "swallowed"),
        ("swallowed_exception.py", "def test_value():\n    try:\n"
         "        assert value() == 1\n    except Exception:\n        pass\n",
         False, 0, "swallowed"),
        ("syntax_error.py", "def test_value(:\n    pass\n",
         False, 0, "SyntaxError"),
    ],
)
def test_suite_validity_fixtures(
    tmp_path: Path,
    name: str,
    source: str,
    expected_valid: bool,
    expected_assertions: int,
    reason_part: str,
) -> None:
    suite = tmp_path / name
    suite.write_text(source, encoding="utf-8")

    valid, reason, assertions = em.suite_validity(suite)

    assert valid is expected_valid
    assert assertions == expected_assertions
    assert reason_part in reason


def test_narrow_exception_does_not_hide_assertion(tmp_path: Path) -> None:
    suite = tmp_path / "test_narrow.py"
    suite.write_text(
        "def test_value():\n"
        "    try:\n"
        "        assert value() == 1\n"
        "    except ValueError:\n"
        "        raise\n",
        encoding="utf-8",
    )

    assert em.suite_validity(suite) == (True, "valid", 1)


def test_mutant_set_metadata_is_stable_and_content_sensitive(tmp_path: Path) -> None:
    first = tmp_path / "mutant_1.py"
    second = tmp_path / "mutant_2.py"
    first.write_text("VALUE = 1\n", encoding="utf-8")
    second.write_text("VALUE = 2\n", encoding="utf-8")

    original = em.mutant_set_metadata([first, second])
    repeated = em.mutant_set_metadata([first, second])
    reversed_order = em.mutant_set_metadata([second, first])
    second.write_text("VALUE = 3\n", encoding="utf-8")
    changed = em.mutant_set_metadata([first, second])

    assert original == repeated
    assert original["mutant_set_total"] == 2
    assert original["mutant_set_id"] != reversed_order["mutant_set_id"]
    assert original["mutant_set_id"] != changed["mutant_set_id"]


def test_paper_benchmark_manifests_are_exact() -> None:
    mt_ids = em.task_ids("MT")
    cm_ids = em.task_ids("CM")

    assert mt_ids == [f"f{i:03d}" for i in range(1, 164)]
    assert len(cm_ids) == len(set(cm_ids)) == 425
    assert len({Path(pkg).parts[1] for pkg, _module, _path in em.cm_modules()}) == 24


def test_cm_layout_resolves_dotted_module() -> None:
    layout = em.cm_layout("flutils.objutils")

    assert layout["put"].is_file()
    assert Path(layout["package_root"]).is_dir()
    assert layout["module_name"] == "flutils.objutils"
    assert layout["mutation_supported"] is False


def test_mt_layout_is_coverup_163_suite_not_legacy_humaneval() -> None:
    layout = em.mt_layout("f001")

    assert Path(layout["put"]).is_file()
    assert "dataset" in Path(layout["put"]).parts
    assert layout["module_name"] == "f001"
    assert layout["mutation_supported"] is True



def test_generate_mutants_writes_reusable_sources(tmp_path: Path) -> None:
    put = tmp_path / "sample.py"
    put.write_text("def increment(value):\n    return value + 1\n", encoding="utf-8")

    mutants = em.generate_mutants(put, tmp_path / "mutants", tmp_path)

    assert mutants
    assert all(path.is_file() and path.read_text(encoding="utf-8").strip()
               for path in mutants)
    assert mutants[0].name == "mutant_0001.py"



def test_run_coverup_uses_top_level_package_dir_for_dotted_cm_module(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source_root = tmp_path / "source"
    target = source_root / "ansible" / "cli" / "adhoc.py"
    target.parent.mkdir(parents=True)
    target.write_text("VALUE = 1\n", encoding="utf-8")
    (source_root / "ansible" / "__init__.py").write_text("", encoding="utf-8")
    (source_root / "ansible" / "cli" / "__init__.py").write_text("", encoding="utf-8")
    captured = {}

    def fake_run(command, **kwargs):
        captured["command"] = command
        captured["env"] = kwargs["env"]
        return type("Result", (), {"returncode": 1, "stdout": "", "stderr": "stop"})()

    monkeypatch.setattr(em.subprocess, "run", fake_run)
    work = tmp_path / "work"
    em.run_coverup(
        target, work / "tests", work, model="dummy",
        module_name="ansible.cli.adhoc", package_root=source_root,
    )

    command = captured["command"]
    package_dir = Path(command[command.index("--package-dir") + 1])
    assert package_dir == work / "project" / "ansible"
    assert captured["env"]["PYTHONPATH"].split(em.os.pathsep)[0] == str(work / "project")


def test_run_coverup_dry_run_accepts_mt_and_cm_package_layouts(tmp_path: Path) -> None:
    for dataset, task in (("MT", "f001"), ("CM", "flutils.objutils")):
        layout = em.LAYOUTS[dataset](task)
        work = tmp_path / dataset
        result = em.run_coverup(
            Path(layout["put"]), work / "tests", work,
            model="dummy", timeout=120, extra=("--dry-run",),
            module_name=layout["module_name"],
            package_root=Path(layout["package_root"]),
        )

        # Dry-run deliberately emits no test; parser/import/coverage must still
        # complete without CLI usage or collection errors.
        assert "usage: CoverUp" not in result.error
        assert "Error measuring coverage" not in result.error
        assert (work / "project").is_dir()



def test_storage_atomic_write_retries_transient_permission_error(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    destination = tmp_path / "rows.csv"
    destination.write_text("old", encoding="utf-8")
    original_replace = storage.os.replace
    calls = {"count": 0}

    def flaky_replace(source, target):
        calls["count"] += 1
        if calls["count"] == 1:
            raise PermissionError(5, "Access is denied", str(target))
        return original_replace(source, target)

    monkeypatch.setattr(storage.os, "replace", flaky_replace)

    storage.ResultStore._atomic_write(destination, "new")

    assert destination.read_text(encoding="utf-8") == "new"
    assert calls["count"] == 2


def test_storage_uses_unique_backup_when_run_id_already_exists(tmp_path: Path) -> None:
    store = storage.ResultStore(tmp_path)
    store.begin("collision_test")

    # Simulate a previous execution of the same notebook finalization cell.
    existing_backup = store.backups / store.run_id
    existing_backup.mkdir()
    (existing_backup / "status.json").write_text("old backup", encoding="utf-8")

    (tmp_path / "rows.csv").write_text("dataset,task\nHumanEval,old\n", encoding="utf-8")
    (tmp_path / "status.json").write_text(
        '[{"dataset": "HumanEval", "task": "old", "status": "BLOCKED"}]',
        encoding="utf-8",
    )
    rows = [{
        "dataset": "HumanEval", "task": "0", "method": "CoverUp",
        "model": "model", "mutation_score": 50.0, "line_pct": 90.0,
        "pass_rate": 100.0,
    }]
    statuses = [{
        "method": "CoverUp", "model": "model", "dataset": "HumanEval",
        "task": "0", "status": "OK",
    }]

    manifest = store.finalize(rows, statuses, expected_statuses=1)

    assert manifest["promoted"]
    assert manifest["backup"] == str(store.backups / f"{store.run_id}_1")
    assert (existing_backup / "status.json").read_text(encoding="utf-8") == "old backup"


def test_storage_blocks_promotion_on_mutant_set_conflict(tmp_path: Path) -> None:
    store = storage.ResultStore(tmp_path)
    store.begin("conflict_test")
    rows = [
        {"dataset": "HumanEval", "task": "0", "method": "CoverUp",
         "model": "openai/claude-sonnet-5", "mutant_set_id": "aaa",
         "mutation_score": 50.0, "line_pct": 90.0, "pass_rate": 100.0},
        {"dataset": "HumanEval", "task": "0", "method": "CODAMOSA",
         "model": "claude-sonnet-5", "mutant_set_id": "bbb",
         "mutation_score": 60.0, "line_pct": 80.0, "pass_rate": 100.0},
        {"dataset": "HumanEval", "task": "1", "method": "CoverUp",
         "model": "openai/claude-sonnet-5", "mutant_set_id": "ccc",
         "mutation_score": 70.0, "line_pct": 95.0, "pass_rate": 90.0},
        {"dataset": "HumanEval", "task": "1", "method": "CODAMOSA",
         "model": "claude-sonnet-5", "mutant_set_id": "ccc",
         "mutation_score": 55.0, "line_pct": 85.0, "pass_rate": 100.0},
    ]
    statuses = [
        {"method": "CoverUp", "model": "openai/claude-sonnet-5",
         "dataset": "HumanEval", "task": "0", "status": "OK"},
        {"method": "CODAMOSA", "model": "claude-sonnet-5",
         "dataset": "HumanEval", "task": "0", "status": "OK"},
        {"method": "CoverUp", "model": "openai/claude-sonnet-5",
         "dataset": "HumanEval", "task": "1", "status": "OK"},
        {"method": "CODAMOSA", "model": "claude-sonnet-5",
         "dataset": "HumanEval", "task": "1", "status": "OK"},
    ]
    manifest = store.finalize(rows, statuses, expected_statuses=4)
    assert not manifest["valid"]
    assert not manifest["promoted"]
    assert "HumanEval:0" in manifest["mutant_set_conflicts"]
    assert "HumanEval:1" not in manifest["mutant_set_conflicts"]



def test_run_coverup_reports_current_log_when_generator_exits_zero_without_tests(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    put = tmp_path / "subject.py"
    put.write_text("def value():\n    return 1\n", encoding="utf-8")
    work = tmp_path / "work"
    tests = work / "tests"

    class Completed:
        returncode = 0
        stdout = ""
        stderr = ""

    def fake_run(*args, **kwargs):
        log_path = work / "coverup.log"
        with log_path.open("a", encoding="utf-8") as handle:
            handle.write("Error: transient upstream service failure\ngiving up\n")
        return Completed()

    monkeypatch.setattr(em, "coverup_cmd", lambda: ["coverup"])
    monkeypatch.setattr(em.subprocess, "run", fake_run)

    result = em.run_coverup(put, tests, work)

    assert not result.ok
    assert result.generated_tests == []
    assert "transient upstream service failure" in result.error
    assert "tidak menghasilkan test" in result.error


# --------------------------------------------------------------------------- #
# pytest_outcome tests  (replaces substring-based mutant kill/survive heuristic)
# --------------------------------------------------------------------------- #
def test_pytest_outcome_passed():
    assert em.pytest_outcome("1 passed in 0.01s") == "passed"
    assert em.pytest_outcome("5 passed, 2 skipped in 1.23s") == "passed"
    assert em.pytest_outcome("no tests ran in 0.00s") == "passed"


def test_pytest_outcome_failed():
    assert em.pytest_outcome("1 failed, 2 passed in 0.05s") == "failed"
    assert em.pytest_outcome("FAILED test_foo.py::test_bar") == "failed"


def test_pytest_outcome_error():
    # Collection/teardown errors (non-assertion) should be "error", not "failed".
    assert em.pytest_outcome("ERROR collecting test_foo.py") == "error"
    assert em.pytest_outcome("1 error in 0.01s") == "error"


def test_pytest_outcome_timeout():
    assert em.pytest_outcome("FAILED ... timed out ... 1 failed") == "timeout"


def test_pytest_outcome_no_summary_falls_back_to_counters():
    assert em.pytest_outcome("collected 3 items\n0 failed, 0 passed, 1 error") == "error"
    assert em.pytest_outcome("collected 2 items\n0 failed, 2 passed") == "passed"


def test_pytest_outcome_no_summary_with_failed():
    assert em.pytest_outcome("collected 1 item\ntest_foo.py::test_bar FAILED") == "failed"


def test_pytest_outcome_ignore_assertionerror_in_pass():
    """A passing test that contains the word AssertionError (e.g. pytest.raises)
    must NOT be misread as a killed mutant."""
    text = (
        "test_foo.py::test_bar PASSED\n"
        "  File \"/path/to/test.py\", line 10, in test_bar\n"
        "    with pytest.raises(AssertionError):\n"
        "E       AssertionError\n"
        "1 passed in 0.03s"
    )
    assert em.pytest_outcome(text) == "passed"


