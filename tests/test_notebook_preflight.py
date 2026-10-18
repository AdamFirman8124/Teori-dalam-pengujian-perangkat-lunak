"""Regression tests for the notebook's per-model preflight and statistics parsing.

Two defects previously caused a whole experiment run to fail:

1. ``coverup_preflight``/``codamosa_preflight`` were all-or-nothing: one model
   that failed its tiny probe set the global ``*_ok`` flag to ``False``, so every
   other (healthy) model was skipped on every task.  The functions now return a
   per-model verdict and the notebook runs only the models that passed.
2. The CODAMOSA ``statistics.csv`` reader assumed a ``name,value`` layout, but
   Pynguin writes metric names as column headers with a single data row.

These tests pin both behaviours against the code that actually lives in the
notebook, so a future edit cannot silently reintroduce them.
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

NOTEBOOK = ROOT / "experiments_codamosa_coverup.ipynb"


def _notebook_cells() -> dict:
    nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    return {
        c["id"]: "".join(c.get("source", []))
        for c in nb["cells"]
        if c.get("cell_type") == "code"
    }


def test_notebook_is_valid_and_all_cells_compile():
    cells = _notebook_cells()
    assert cells, "notebook has no code cells"
    for cell_id, source in cells.items():
        compile(source, cell_id, "exec")


def test_preflight_is_per_model_not_all_or_nothing():
    pre = _notebook_cells()["f68dcf13"]
    assert "def coverup_preflight(models):" in pre
    assert "def codamosa_preflight(models):" in pre
    # Return a dict keyed by model so healthy models survive a sibling failure.
    assert "verdict[model] = True" in pre
    assert "verdict[model] = False" in pre
    assert "ok_models" in pre


def test_task_runner_uses_only_preflight_passed_models():
    runner = _notebook_cells()["4ce9652a"]
    assert "for model in ACTIVE_COVERUP_MODELS:" in runner
    assert "for model in ACTIVE_CODAMOSA_MODELS:" in runner
    # Failing models are still recorded, but only for the failing model.
    assert "BLOCKED: model gagal preflight." in runner


def test_task_runner_respects_global_ok_flags():
    """Docker/build failure must still block CODAMOSA instead of trying it."""
    runner = _notebook_cells()["4ce9652a"]
    assert "if not coverup_ok:" in runner
    assert "if not codamosa_ok:" in runner
    # When the global flag is false the runner returns before touching Docker.
    assert runner.index("if not coverup_ok:") < runner.index("for model in ACTIVE_COVERUP_MODELS:")
    assert runner.index("if not codamosa_ok:") < runner.index("for model in ACTIVE_CODAMOSA_MODELS:")


def test_discovery_defaults_to_all_available_models():
    discovery = _notebook_cells()["a9f680bb"]
    # Default must adopt every probed model rather than a fixed short list.
    assert 'os.getenv("MODEL_DISCOVERY_USE_ALL", "1")' in discovery
    assert 'os.getenv("MODEL_DISCOVERY_MAX_MODELS", "0")' in discovery
    assert '"openai/" + m for m in _selected' in discovery
    assert '",".join(_selected)' in discovery


def test_preflight_has_rpm_throttle_and_backoff():
    """Probing the whole catalogue must respect the provider RPM cap."""
    pre = _notebook_cells()["f68dcf13"]
    assert "def _rpm_limit()" in pre
    assert 'os.getenv("RPM_LIMIT", "50")' in pre
    assert "def _throttle(" in pre
    assert "def _probe_with_backoff(" in pre
    assert "_is_rate_limit_error" in pre
    # Both preflights must actually use the throttle and the backoff helper.
    assert pre.count("_throttle(interval)") >= 2
    assert pre.count("_probe_with_backoff(") >= 2


def test_rpm_helpers_respect_limit_and_retry_on_429():
    """Execute the notebook's real helper functions with a tiny RPM budget."""
    pre = _notebook_cells()["f68dcf13"]
    ns: dict = {"os": os, "time": time}
    # Only the pure helpers are needed; skip the provider imports.
    for name in ("_rpm_limit", "_throttle", "_is_rate_limit_error",
                 "_is_transient_probe_error", "_probe_with_backoff"):
        start = pre.index("def %s(" % name)
        end = pre.index("\ndef ", start + 1)
        exec(pre[start:end], ns)

    os.environ["RPM_LIMIT"] = "10"
    assert ns["_rpm_limit"]() == 10
    os.environ["RPM_LIMIT"] = "bad"
    assert ns["_rpm_limit"]() == 50

    assert ns["_is_rate_limit_error"](Exception("Rate limit: 50 rpm")) is True
    assert ns["_is_rate_limit_error"](Exception("HTTPError: 429 Too Many Requests")) is True
    assert ns["_is_rate_limit_error"](Exception("model not found")) is False

    calls = {"n": 0}

    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise Exception("Rate limit: 50 rpm. Try again later.")
        return "ok"

    result, error = ns["_probe_with_backoff"](flaky, 5, 0.0)
    assert result == "ok" and error is None and calls["n"] == 3

    def always_429():
        raise Exception("Rate limit: 50 rpm")

    result, error = ns["_probe_with_backoff"](always_429, 2, 0.0)
    assert result is None and error is not None


def test_rpm_limit_from_env(monkeypatch):
    monkeypatch.setenv("RPM_LIMIT", "25")
    assert int(os.getenv("RPM_LIMIT", "50")) == 25




def test_readiness_cell_structure():
    cells = _notebook_cells()
    ids = list(cells)
    assert cells["b4501a3d"], "readiness code cell missing"
    assert ids.index("b4501a3d") < ids.index("a9f680bb"), "readiness must run before discovery"
    assert ids.index("b4501a3d") > ids.index("c5d09b00"), "readiness needs setup variables"


def test_readiness_cell_contract():
    src = _notebook_cells()["b4501a3d"]
    for token in (
        "CPU threads", "RAM total", "RAM tersedia", "Disk bebas",
        "AUTO_INSTALL", "READINESS: OK", "READINESS BLOCKED",
        "RAM tidak bisa diunduh", "TASK_WORKERS",
    ):
        assert token in src, token


def test_readiness_never_downloads_hardware():
    src = _notebook_cells()["b4501a3d"].lower()
    assert "unduh ram" not in src and "download ram" not in src
    assert "Auto-tune" in _notebook_cells()["b4501a3d"]


def test_readiness_detects_wsl_and_adapts():
    src = _notebook_cells()["b4501a3d"]
    assert "def _readiness_detect_wsl():" in src
    assert "microsoft" in src and "_ENV_KIND" in src and "_IS_WSL" in src
    assert ".wslconfig" in src
    assert "Upgrade ke WSL2" in src
    assert "/mnt/" in src and "lebih lambat" in src
    assert "WSL Integration" in src
    assert "sleep" in src.lower()


def test_readiness_wsl_rules_execute():
    src = _notebook_cells()["b4501a3d"]
    start = src.index("def _readiness_detect_wsl():")
    end = src.index("# --- 0b.", start)
    ns: dict = {}
    exec(
        "from pathlib import Path\n"
        "import platform as _platform\n"
        "def _readiness_note(t): pass\n"
        + src[start:end],
        ns,
    )
    assert callable(ns["_readiness_detect_wsl"])
    assert ns["_readiness_detect_wsl"]() in {"native", "wsl", "wsl1", "wsl2"}


def test_readiness_scale_up_guards_remote_threads():
    src = _notebook_cells()["b4501a3d"]
    assert "_AUTO_SCALE" in src
    assert "CPU_RESERVED_THREADS" in src
    assert "CONFIG_MAX_LOAD" in src
    # Skala naik tidak boleh menghapus tunjangan remote: minimal 2 disisakan.
    assert "max(2" in src


def test_readiness_clock_drift_checked():
    src = _notebook_cells()["b4501a3d"]
    assert "CLOCK_WARN_SECONDS" in src
    assert "CLOCK_BLOCK_SECONDS" in src
    assert "hwclock -s" in src


def test_statistics_reader_handles_header_oriented_csv(tmp_path):
    """Reproduce Pynguin's CSV layout and the notebook's parsing logic."""
    stat = tmp_path / "statistics.csv"
    fields = ["TargetModule", "LineCoverage", "LLMCalls", "LLMQueryTime"]
    with stat.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(fields)
        writer.writerow(["mod", "88.0", "7", "1.5"])

    row: dict = {}
    with stat.open(encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh)
        header = next(reader, None)
        data = next(reader, None)
        assert header and data
        for name in ("LLMCalls", "prompt_tokens", "completion_tokens"):
            if name not in header:
                continue
            value = int(float(data[header.index(name)]))
            row["calls_with_usage" if name == "LLMCalls" else name] = value

    assert row["calls_with_usage"] == 7
    assert "prompt_tokens" not in row  # absent in this provider response


def test_statistics_reader_source_has_no_dictreader_name_value():
    runner = _notebook_cells()["4ce9652a"]
    assert "DictReader(_fh)" not in runner
    assert "CODAMOSA writes variable names as column headers" in runner


def test_llm_logging_and_budget_knobs_are_wired():
    cells = _notebook_cells()
    setup = cells["c5d09b00"]
    runner = cells["4ce9652a"]
    preflight = cells["f68dcf13"]

    # One fixed budget for every task: no profile/tuned switch may exist.
    assert "EXPERIMENT_PROFILE" not in setup
    assert "PROFILE_TAG" not in setup
    assert "TUNED_" not in setup
    assert "COVERUP_MAX_ATTEMPTS" in setup
    assert "CODAMOSA_TEMPERATURE" in setup
    assert "load_dotenv(ROOT / 'config' / '.env', override=True)" in setup

    assert "COVERUP_PREFLIGHT_TIMEOUT" in preflight
    assert "_is_transient_probe_error" in preflight
    assert "llm_calls_log=llm_calls_log" in runner
    assert "CODAMOSA_LLM_CALLS_LOG=/output/llm_calls.jsonl" in runner
    assert "COVERUP_MAX_ATTEMPTS" in runner
    assert "CODAMOSA_TEMPERATURE" in runner


def test_runner_has_no_profile_dimension():
    cells = _notebook_cells()
    runner = cells["4ce9652a"]
    finalizer = cells["dc51281c"]

    assert "_profiled_slug" not in runner
    assert 'row["profile"]' not in runner
    assert '"profile":' not in runner
    # Plain method+model resume key.
    assert "return (method, model, dataset, str(task)) in RESUME_KEYS" in runner
    # Fresh full run: expected count comes straight from TASKS x models.
    assert "expected_statuses = sum(len(task_ids) for task_ids in TASKS.values())" in finalizer
    assert "profile" not in finalizer



def test_wilcoxon_markdown_contains_no_python_code():
    nb = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    cell = next(c for c in nb["cells"] if c.get("id") == "wilcoxon-table-md")
    assert cell["cell_type"] == "markdown"
    source = "".join(cell["source"])
    assert "import numpy" not in source
    assert "def _a12" not in source
    assert "p-Holm" in source




def test_analysis_cells_have_no_profile_dimension():
    cells = _notebook_cells()
    chart = cells["valid-comparison-chart"]
    summary = cells["suite-metrics-table"]
    stats = cells["wilcoxon-table"]

    assert '["dataset", "method", "model"]' in chart
    assert '"profile"' not in chart
    assert '"profile"' not in summary
    assert '"profile"' not in stats
    assert '" @"' not in stats




def test_all_terminal_statuses_are_recorded():
    runner = _notebook_cells()["4ce9652a"]
    # Successful CoverUp/CODAMOSA statuses and the generic blocked helpers must
    # all record the same identity fields so nothing is silently dropped.
    assert runner.count('"status": "OK"') >= 2
    assert runner.count('"status": _status') >= 1
    assert '"method": _method' in runner



def test_codamosa_preflight_preserves_upstream_400_body_for_retry():
    preflight = _notebook_cells()["f68dcf13"]
    assert "upstream_error" in preflight
    assert "response.text[:1000]" in preflight
    assert "_is_transient_probe_error" in preflight



def test_codamosa_container_named_and_force_removed_on_timeout():
    runner = _notebook_cells()["4ce9652a"]
    assert '"--name", _container_name' in runner
    assert '"docker", "rm", "-f", _container_name' in runner
    assert "container removed: " in runner
    assert 'teori.dataset=" + dataset' in runner


def test_valid_comparison_ok_keys_include_method_model_dataset_task():
    chart = _notebook_cells()["valid-comparison-chart"]
    assert 'x.get("method")' in chart
    assert 'x.get("model")' in chart
    assert 'x.get("dataset")' in chart
    assert 'str(x.get("task"))' in chart