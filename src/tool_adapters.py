from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

import eval_metrics as em
from protocol import ROOT, load_config
from results_schema import FIELDS
from rate_gate import acquire

RATE_STATE = ROOT / "results" / "rate_gate.jsonl"


def _rate_limited() -> float:
    # Rate gating is handled per LLM call inside CoverUp (llm.py)
    # and CodaMOSA (model.py). Calling acquire() here at the task level
    # creates an exclusive lock deadlock against child processes.
    return 0.0


def _secret_env(backbone: str) -> tuple[str, str, dict[str, Any]]:
    config = load_config()["backbones"][backbone]
    base = os.environ[config["base_url_env"]].rstrip("/")
    key = os.environ[config["api_key_env"]]
    return base, key, config


def _cost(backbone: str, tokens_in: int, tokens_out: int) -> float:
    model = load_config()["backbones"][backbone]
    return (
        tokens_in * float(model["input_usd_per_million"])
        + tokens_out * float(model["output_usd_per_million"])
    ) / 1_000_000


def _layout(suite: str, unit_id: str) -> dict[str, Any]:
    return em.LAYOUTS[suite](unit_id)


def _model_slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value)


def _read_calls(path: Path) -> dict[str, Any]:
    calls = []
    if path.is_file():
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                calls.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    returned = [call.get("model_returned") or call.get("returned_model") for call in calls]
    returned = [value for value in returned if value]
    return {
        "n_api_calls": len(calls),
        "tokens_in": sum(int(call.get("tokens_in") or call.get("prompt_tokens") or 0) for call in calls),
        "tokens_out": sum(int(call.get("tokens_out") or call.get("completion_tokens") or 0) for call in calls),
        "ratelimit_wait_s": sum(float(call.get("ratelimit_wait_s") or 0) for call in calls),
        "model_returned": returned[-1] if returned else None,
        "returned_values": sorted(set(returned)),
    }


def _base_result(row: dict[str, str], started: dt.datetime) -> dict[str, Any]:
    result = {field: "" for field in FIELDS}
    result.update(
        {
            "run_id": row["run_id"],
            "suite": row["suite"],
            "unit_id": row["unit_id"],
            "project": row.get("project", ""),
            "tool": row["tool"],
            "backbone": row["backbone"],
            "model_requested": row["model_requested"],
            "run_idx": int(row["run_idx"]),
            "seed": int(row["seed"]),
            "start_time": started.isoformat(),
            "budget_s": int(load_config()["experiment"]["budget_seconds"]),
            "attempt": 1,
            "mutation_tool": load_config()["experiment"]["mutation_tool"],
            "k_reruns": int(load_config()["experiment"]["flaky_repetitions"]),
            "status": "failed",
        }
    )
    return result


def _evaluation_fields(evaluated: dict[str, Any]) -> dict[str, Any]:
    return {
        "n_tests_final": evaluated.get("n_tests", evaluated.get("n_tests_files", 0)),
        "n_pass_first": evaluated.get("n_passed", 0),
        "n_fail": max(0, int(evaluated.get("n_tests", 0) or 0) - int(evaluated.get("n_passed", 0) or 0)),
        "n_error": 0,
        "n_timeout": 0,
        "n_flaky": evaluated.get("flaky_count", 0),
        "n_valid": evaluated.get("n_passed", 0),
        "lines_total": evaluated.get("lines_total", evaluated.get("num_statements", "")),
        "lines_exec": evaluated.get("lines_covered", ""),
        "branches_total": evaluated.get("branches_total", ""),
        "branches_exec": evaluated.get("branches_covered", ""),
        "n_mutants": evaluated.get("n_mutants", 0),
        "n_killed": evaluated.get("killed", 0),
        "n_survived": evaluated.get("survived", 0),
        "n_mutant_timeout": evaluated.get("timeout", 0),
    }


def run_mutap(row: dict[str, str], output_root: Path) -> dict[str, Any]:
    """Generate a MuTAP suite in Docker and evaluate it with the shared S3-S4 pipeline.

    MuTAP (fork plasma-umass/MuTAP @888ab58a, prpl-test/) is assertion-focused:
    the LLM proposes assertions against the PUT, invalid ones are filtered
    (raw validity), and surviving mutants drive an augmented prompt.  The
    collaborator image embeds the PUT inline in its test file; the adapter
    swaps that block for an import of our dataset package so coverage and
    mutation are measured on the same PUT and mutant set as every other tool
    (pedoman rule 14-4).  Internal MutPy mutants are MuTAP's algorithm input,
    not the evaluation engine; final metrics come from our pipeline.
    """
    started = dt.datetime.now(dt.timezone.utc)
    result = _base_result(row, started)
    result["tool_version"] = "fork@888ab58a"
    base, key, model = _secret_env(row["backbone"])
    work = output_root / "generated" / row["run_id"]
    if work.exists():
        shutil.rmtree(work, ignore_errors=True)
    output = work / "output"
    output.mkdir(parents=True, exist_ok=True)
    layout = _layout(row["suite"], row["unit_id"])
    task_id = int(row["unit_id"][1:])  # f001 -> collaborator task 1
    container = f"exp-{_model_slug(row['run_id']).lower()}-{int(time.time()*1000)%1000000}"
    subprocess.run(["docker", "rm", "-f", container], capture_output=True)
    budget = int(load_config()["experiment"]["budget_seconds"])
    grace = int(load_config()["experiment"]["kill_grace_seconds"])
    command = [
        "docker", "run", "--rm", "--name", container,
        "--label", "teori.experiment=mutap",
        "--cpus", str(load_config()["experiment"]["worker_cpus"]),
        "--memory", str(load_config()["experiment"]["worker_memory"]),
        "--memory-swap", str(load_config()["experiment"]["worker_memory"]),
        "-v", f"{output.resolve()}:/workspace/output/mutap",
        "-e", f"API_KEY={key}",
        "-e", f"BASE_URL_API_KEY={base}",
        "-e", f"MODEL_AI_1={model['model_requested']}",
        "mutap-runner:latest",
        "python", "run_mutap_experiment.py", str(task_id),
        "--model", model["model_requested"],
    ]
    t0 = time.monotonic()
    try:
        completed = subprocess.run(command, capture_output=True, text=True,
                                   encoding="utf-8", errors="replace",
                                   timeout=budget + grace)
        (work / "docker.stdout.log").write_text(completed.stdout or "", encoding="utf-8")
        (work / "docker.stderr.log").write_text(completed.stderr or "", encoding="utf-8")
        if completed.returncode:
            raise RuntimeError(f"MuTAP exit {completed.returncode}: {(completed.stdout + completed.stderr)[-1500:]}")
        summary = _read_mutap_summary(output)
        test_path = output / f"test_mutap_task_{task_id}.py"
        if not test_path.is_file():
            raise RuntimeError("MuTAP produced no test file")
        put_code = Path(layout["put"]).read_text(encoding="utf-8")
        func_name = summary.get("function_name") or re.search(r"def\s+(\w+)\s*\(", put_code).group(1)
        test_code = test_path.read_text(encoding="utf-8")
        # The collaborator file embeds its own PUT copy (script_N.py), which
        # does not byte-match our dataset module; cut everything before the
        # test function and import the PUT from our package instead, so
        # coverage and mutation are measured on the shared dataset PUT.
        test_start = test_code.find(f"def test_{func_name}")
        if test_start < 0:
            raise RuntimeError("MuTAP test file has no test function to transform")
        transformed_code = (
            f"from {layout['module_name']} import {func_name}\n\n"
            + test_code[test_start:]
        )
        transformed = output / "test_mutap.py"
        transformed.write_text(transformed_code, encoding="utf-8")
        valid = [transformed] if em.suite_validity(transformed)[0] else []
        if not valid:
            raise RuntimeError("MuTAP test suite not importable after PUT swap; refusing to score empty coverage")
        evaluated = em.evaluate(
            row["suite"], row["unit_id"], valid, "MuTAP",
            wall_time_s=time.monotonic() - t0, cost_usd=0.0,
            workroot=output_root / "work",
            timeout=int(load_config()["experiment"]["evaluation_timeout_seconds"]),
        )
        result.update(_evaluation_fields(evaluated))
        result["gen_time_s"] = max(0.0, time.monotonic() - t0)
        result["hit_budget"] = int(result["gen_time_s"] >= budget - 5)
        result["wait_flag"] = 0
        tokens_in = int(summary.get("prompt_tokens") or 0)
        tokens_out = int(summary.get("completion_tokens") or 0)
        result["n_api_calls"] = int(summary.get("api_calls") or 0)
        result["tokens_in"] = tokens_in
        result["tokens_out"] = tokens_out
        result["cost_usd"] = round(_cost(row["backbone"], tokens_in, tokens_out), 8)
        result["model_returned"] = model["model_requested"]
        result["n_raw_proposals"] = int(summary.get("raw_total_assertions") or 0)
        result["n_raw_pass"] = int(summary.get("raw_valid_assertions") or 0)
        result["status"] = "ok"
        result["error_category"] = ""
    except subprocess.TimeoutExpired:
        subprocess.run(["docker", "rm", "-f", container], capture_output=True, text=True)
        result.update({"hit_budget": 1, "error_category": "timeout", "gen_time_s": budget})
    except Exception as exc:
        result["error_category"] = _error_category(exc)
        result["error_message"] = str(exc)[-2000:]
    result["end_time"] = dt.datetime.now(dt.timezone.utc).isoformat()
    return result


def _read_mutap_summary(output: Path) -> dict[str, Any]:
    for candidate in output.glob("model_*_results.json"):
        entries = json.loads(candidate.read_text(encoding="utf-8"))
        if entries:
            return entries[-1]
    return {}


def _raw_validity_for(calls_log: Path, row: dict[str, str], valid: list[Path]) -> dict[str, int]:
    """Raw-validity fields with a zero-valued fallback that never fails a run.

    Uses the run's own valid tests to build the package context; when the log
    or context is unusable the run keeps zero proposals instead of crashing.
    """
    work = calls_log.parent.parent
    raw_work = work / "rawwork"
    raw_work.mkdir(parents=True, exist_ok=True)
    try:
        prepared = em.prepare_suite(_layout(row["suite"], row["unit_id"]), valid, raw_work)
        return em.raw_validity_of(calls_log, prepared, raw_work)
    except Exception:
        return {"n_raw_proposals": 0, "n_raw_pass": 0}


def run_pynguin(row: dict[str, str], output_root: Path) -> dict[str, Any]:
    """Generate a Pynguin suite in Docker and evaluate it with the shared S3-S4 pipeline.

    Pynguin uses no LLM: cost is zero, no backbone, no API calls.  Runs in the
    pynguin-runner image (python:3.10 + pynguin==0.47.0, per docs/sources.md)
    with DYNAMOSA and the same 600 s budget as every other tool (W1/W4).
    """
    started = dt.datetime.now(dt.timezone.utc)
    result = _base_result(row, started)
    result["tool_version"] = "0.47.0"
    result["model_requested"] = ""
    result["model_returned"] = ""
    result["backbone"] = ""
    result["n_api_calls"] = 0
    result["tokens_in"] = ""
    result["tokens_out"] = ""
    result["cost_usd"] = 0.0
    result["ratelimit_wait_s"] = 0.0
    work = output_root / "generated" / row["run_id"]
    if work.exists():
        shutil.rmtree(work, ignore_errors=True)
    output = work / "output"
    output.mkdir(parents=True, exist_ok=True)
    layout = _layout(row["suite"], row["unit_id"])
    project = Path(layout["package_root"]).resolve()
    package = _filtered_requirements(layout, work)
    container = f"exp-{_model_slug(row['run_id']).lower()}-{int(time.time()*1000)%1000000}"
    subprocess.run(["docker", "rm", "-f", container], capture_output=True)
    budget = int(load_config()["experiment"]["budget_seconds"])
    grace = int(load_config()["experiment"]["kill_grace_seconds"])
    command = [
        "docker", "run", "--rm", "--name", container,
        "--label", "teori.experiment=pynguin",
        "--oom-score-adj", "1000",
        "--cpus", str(load_config()["experiment"]["worker_cpus"]),
        "--memory", str(load_config()["experiment"]["worker_memory"]),
        "--memory-swap", str(load_config()["experiment"]["worker_memory"]),
        "-v", f"{project}:/input:ro",
        "-v", f"{output.resolve()}:/output",
        "-v", f"{work.resolve()}:/package:ro",
        "-e", "PYNGUIN_DANGER_AWARE=1",
        "img-pynguin:latest",
        "--project-path", "/input",
        "--module-name", layout["module_name"],
        "--output-path", "/output",
        "--algorithm", "DYNAMOSA",
        "--maximum-search-time", str(budget),
        "--seed", row["seed"],
        "--coverage-metrics", "BRANCH", "LINE",
        "--output-variables", "TargetModule,LineCoverage,BranchCoverage",
    ]
    t0 = time.monotonic()
    try:
        completed = subprocess.run(command, capture_output=True, text=True,
                                   encoding="utf-8", errors="replace",
                                   timeout=budget + grace)
        (work / "docker.stdout.log").write_text(completed.stdout or "", encoding="utf-8")
        (work / "docker.stderr.log").write_text(completed.stderr or "", encoding="utf-8")
        if completed.returncode:
            raise RuntimeError(
                f"Pynguin exit {completed.returncode}: {(completed.stdout + completed.stderr)[-2000:]}")
        tests = sorted(output.rglob("test_*.py"))
        if not tests:
            raise RuntimeError("Pynguin produced no test suite")
        valid = [path for path in tests if em.suite_validity(path)[0]]
        if not valid:
            raise RuntimeError("Pynguin produced no importable test file; refusing to score empty coverage")
        evaluated = em.evaluate(
            row["suite"], row["unit_id"], valid, "Pynguin",
            wall_time_s=time.monotonic() - t0, cost_usd=0.0,
            workroot=output_root / "work",
            timeout=int(load_config()["experiment"]["evaluation_timeout_seconds"]),
        )
        result.update(_evaluation_fields(evaluated))
        result["gen_time_s"] = max(0.0, time.monotonic() - t0)
        result["hit_budget"] = int(result["gen_time_s"] >= budget - 5)
        result["wait_flag"] = 0
        result["status"] = "ok"
        result["error_category"] = ""
    except subprocess.TimeoutExpired:
        subprocess.run(["docker", "rm", "-f", container], capture_output=True, text=True)
        result.update({"hit_budget": 1, "error_category": "timeout", "gen_time_s": budget})
    except Exception as exc:
        result["error_category"] = _error_category(exc)
        result["error_message"] = str(exc)[-2000:]
    result["end_time"] = dt.datetime.now(dt.timezone.utc).isoformat()
    return result


class UnsupportedBackbone(RuntimeError):
    """Raised when a model's transport alias no longer belongs to a probed backbone."""


def require_backbone_probed(backbone: str, expected_requested: str) -> dict[str, Any]:
    probe_path = ROOT / "results" / "endpoint_probe.json"
    results = json.loads(probe_path.read_text(encoding="utf-8")) if probe_path.exists() else []
    probed = next(
        (
            entry
            for entry in results
            if entry.get("backbone") == backbone
            and entry.get("passed")
            and entry.get("model_requested") == expected_requested
        ),
        None,
    )
    if probed is None:
        raise UnsupportedBackbone(
            f"Backbone {backbone} has no passing probe for {expected_requested} in results/endpoint_probe.json."
        )
    return probed


def run_coverup(row: dict[str, str], output_root: Path) -> dict[str, Any]:
    started = dt.datetime.now(dt.timezone.utc)
    result = _base_result(row, started)
    result["tool_version"] = "0.6.3+experiment-patches"
    require_backbone_probed(row["backbone"], row["model_requested"])
    work = output_root / "generated" / row["run_id"]
    if work.exists():
        shutil.rmtree(work, ignore_errors=True)
    tests_dir = work / "tests"
    calls = output_root / "raw" / row["run_id"] / "llm_log.jsonl"
    calls.parent.mkdir(parents=True, exist_ok=True)
    layout = _layout(row["suite"], row["unit_id"])
    base, key, model = _secret_env(row["backbone"])
    transport_model = "openai/" + row["model_requested"]
    old = os.environ.copy()
    try:
        os.environ.update({
            "OPENAI_API_KEY": key,
            "OPENAI_BASE_URL": base,
            "LLM_PROXY_BACKBONE": row["backbone"],
            "LLM_PROXY_RUN_ID": row["run_id"],
            "FLAKY_REPEATS": str(load_config()["experiment"]["flaky_repetitions"]),
            "RPM_GATE_STATE": str((ROOT / "results" / "rate_gate.jsonl").resolve()),
            "RPM_LIMIT": str(load_config()["experiment"].get("rate_limit_rpm", 50)),
        })
        wait_s = _rate_limited()
        print(f"[{row['run_id']}] CoverUp prompting {row['model_requested']}...", flush=True)
        run = em.run_coverup(
            Path(layout["put"]), tests_dir, work,
            model=transport_model,
            timeout=int(load_config()["experiment"]["budget_seconds"]),
            llm_calls_log=calls,
            module_name=layout.get("module_name"),
            package_root=Path(layout["package_root"]) if layout.get("package_root") else None,
            extra=("--max-concurrency", "1", "--model-temperature", "0"),
        )
        info = _read_calls(calls)
        elapsed = (dt.datetime.now(dt.timezone.utc) - started).total_seconds()
        result.update(info)
        result["cost_usd"] = _cost(row["backbone"], info["tokens_in"], info["tokens_out"])
        result["ratelimit_wait_s"] = float(info.get("ratelimit_wait_s") or 0) + wait_s
        result["gen_time_s"] = max(0.0, elapsed - result["ratelimit_wait_s"])
        result["hit_budget"] = int(not run.ok and "timeout" in run.error.lower())
        result["wait_flag"] = int(info["ratelimit_wait_s"] > 60)
        if not run.ok or not run.generated_tests:
            raise RuntimeError(run.error or "CoverUp produced no tests")
        valid = [Path(path) for path in run.generated_tests if em.suite_validity(Path(path))[0]]
        if not valid:
            raise RuntimeError("CoverUp produced no importable test file; refusing to score empty coverage")
        print(f"[{row['run_id']}] CoverUp evaluating {len(valid)} tests & mutation score...", flush=True)
        evaluated = em.evaluate(
            row["suite"], row["unit_id"], valid, "CoverUp",
            wall_time_s=result["gen_time_s"], cost_usd=result["cost_usd"], workroot=output_root / "work",
            timeout=int(load_config()["experiment"]["evaluation_timeout_seconds"]),
        )
        result.update(_evaluation_fields(evaluated))
        result.update(_raw_validity_for(calls, row, valid))
        result["status"] = "ok"
        result["error_category"] = ""
    except Exception as exc:
        result["error_category"] = _error_category(exc)
        result["error_message"] = str(exc)[-2000:]
    finally:
        os.environ.clear()
        os.environ.update(old)
    result["end_time"] = dt.datetime.now(dt.timezone.utc).isoformat()
    return result


def _filtered_requirements(layout: dict[str, Any], work: Path) -> Path:
    source = Path(layout.get("package_txt") or Path(layout["package_root"]) / "package.txt")
    target = work / "package.txt"
    stdlib = getattr(__import__("sys"), "stdlib_module_names", set())
    # Project pins for these packages downgrade Pynguin 0.47.0's own runtime
    # inside the container (e.g. pytest 7 vs >=8.3.5), or require missing native C
    # headers (pycurl, gssapi) not needed by the specific modules under test.
    pynguin_conflicts = {
        "pytest", "pygments", "setuptools", "wheel", "pip",
        "pycurl", "gssapi", "kerberos", "urllib_gssapi",
        "py2exe", "python_apt",
    }
    wanted = []
    if source.is_file():
        for line in source.read_text(encoding="utf-8", errors="replace").splitlines():
            name = line.strip()
            package = re.split(r"[<>=\[]", name)[0].replace("-", "_").lower()
            if name and not name.startswith("#") and package not in stdlib:
                if package not in pynguin_conflicts:
                    if package == "psycopg2":
                        wanted.append("psycopg2-binary")
                    else:
                        wanted.append(name)
    target.write_text("\n".join(wanted) + ("\n" if wanted else ""), encoding="utf-8")
    return target


def run_codamosa(row: dict[str, str], output_root: Path) -> dict[str, Any]:
    started = dt.datetime.now(dt.timezone.utc)
    result = _base_result(row, started)
    result["tool_version"] = "0.19.0+chat-completions-patches"
    require_backbone_probed(row["backbone"], row["model_requested"])
    work = output_root / "generated" / row["run_id"]
    if work.exists():
        shutil.rmtree(work, ignore_errors=True)
    output = work / "output"
    output.mkdir(parents=True, exist_ok=True)
    layout = _layout(row["suite"], row["unit_id"])
    project = Path(layout["package_root"]).resolve()
    package = _filtered_requirements(layout, work)
    base, key, model = _secret_env(row["backbone"])
    auth = work / "auth.args"
    auth.write_text("--authorization-key\n" + key + "\n", encoding="utf-8")
    auth.chmod(0o600)
    container = f"exp-{_model_slug(row['run_id']).lower()}-{int(time.time()*1000)%1000000}"
    subprocess.run(["docker", "rm", "-f", container], capture_output=True)
    budget = int(load_config()["experiment"]["budget_seconds"])
    grace = int(load_config()["experiment"]["kill_grace_seconds"])
    # The default Docker bridge network cannot resolve localhost to the host
    # (e.g. a local LLM gateway).  Route local backbone URLs through Docker's
    # host-gateway alias instead; this works with Docker Desktop and Engine.
    host_network = "://localhost:" in base or "://127.0.0.1:" in base
    container_base_url = base
    if host_network:
        container_base_url = base.replace("://localhost:", "://host.docker.internal:").replace(
            "://127.0.0.1:", "://host.docker.internal:")
    command = [
        "docker", "run", "--rm", "--name", container,
        "--label", "teori.experiment=codamosa",
        "--oom-score-adj", "1000",
        *(["--add-host", "host.docker.internal:host-gateway"] if host_network else []),
        "--cpus", str(load_config()["experiment"]["worker_cpus"]),
        "--memory", str(load_config()["experiment"]["worker_memory"]),
        "--memory-swap", str(load_config()["experiment"]["worker_memory"]),
        "-v", f"{project}:/input:ro",
        "-v", f"{output.resolve()}:/output",
        "-v", f"{work.resolve()}:/package:ro",
        "-v", f"{auth.resolve()}:/run/codamosa-auth:ro",
        "-v", f"{(ROOT / 'results').resolve()}:/results",
        "-v", f"{(ROOT / 'src' / 'rate_gate.py').resolve()}:/usr/local/lib/python3.10/site-packages/rate_gate.py:ro",
        "-v", f"{(ROOT / 'codamosa' / 'pynguin' / 'languagemodels' / 'model.py').resolve()}:/usr/local/lib/python3.10/site-packages/pynguin/languagemodels/model.py:ro",
        "-e", "CODAMOSA_LLM_CALLS_LOG=/output/llm_calls.jsonl",
        "-e", "CODAMOSA_REQUEST_TIMEOUT=600",
        "-e", "CODAMOSA_MAX_TRANSPORT_RETRIES=4",
        "-e", "CODAMOSA_MAX_TOKENS=4096",
        "-e", "RPM_GATE_STATE=/results/rate_gate.jsonl",
        "-e", f"RPM_LIMIT={load_config()['experiment'].get('rate_limit_rpm', 50)}",
        "-e", "CODAMOSA_CALL_SPACING=1.2",
        "pynguin-runner:latest", "@/run/codamosa-auth",
        "--assertion-generation", "MUTATION_ANALYSIS",
        "--project-path", "/input",
        "--module-name", layout["module_name"],
        "--output-path", "/output",
        "--maximum-search-time", str(budget),
        "--algorithm", "CODAMOSA",
        "--seed", row["seed"],
        "--output-variables", "TargetModule,LineCoverage,BranchCoverage,LLMCalls,LLMQueryTime",
        "--report-dir", "/output",
        "--model-name", row["model_requested"],
        "--model-base-url", container_base_url,
        "--model-relative-url", "/chat/completions",
        "--temperature", "0.8",
        "--large-language-model-seeding", "True",
        "--uninterpreted-statements", "ONLY",
        "--include-partially-parsable", "True",
        "--allow-expandable-cluster", "True",
        "--seeded-testcases-reuse-probability", "1",
        "--population", "5",
    ]
    t0 = time.monotonic()
    wait_s = _rate_limited()
    print(f"[{row['run_id']}] CodaMOSA search active in Docker container...", flush=True)
    try:
        completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=budget + grace)
        (work / "docker.stdout.log").write_text(completed.stdout or "", encoding="utf-8")
        (work / "docker.stderr.log").write_text(completed.stderr or "", encoding="utf-8")
        if completed.returncode:
            raise RuntimeError(f"CodaMOSA exit {completed.returncode}: {(completed.stdout + completed.stderr)[-2000:]}")
        primary = [path for path in output.rglob("test_*.py") if "_failing" not in path.name]
        if not primary:
            raise RuntimeError("CodaMOSA produced no valid primary test suite")
        valid = [path for path in primary if em.suite_validity(path)[0]]
        if not valid:
            raise RuntimeError("CodaMOSA produced no importable primary test file; refusing to score empty coverage")
        print(f"[{row['run_id']}] CodaMOSA evaluating {len(valid)} tests & mutation score...", flush=True)
        evaluated = em.evaluate(
            row["suite"], row["unit_id"], valid, "CodaMOSA",
            wall_time_s=time.monotonic() - t0, workroot=output_root / "work",
            timeout=int(load_config()["experiment"]["evaluation_timeout_seconds"]),
        )
        result.update(_evaluation_fields(evaluated))
        result.update(_raw_validity_for(output / "llm_calls.jsonl", row, valid))
        info = _read_calls(output / "llm_calls.jsonl")
        result.update(info)
        result["cost_usd"] = _cost(row["backbone"], info["tokens_in"], info["tokens_out"])
        result["ratelimit_wait_s"] = float(info.get("ratelimit_wait_s") or 0) + wait_s
        result["gen_time_s"] = max(0.0, time.monotonic() - t0 - result["ratelimit_wait_s"])
        result["hit_budget"] = int(result["gen_time_s"] >= budget - 5)
        result["wait_flag"] = int(result["ratelimit_wait_s"] > 60)
        result["status"] = "ok"
    except subprocess.TimeoutExpired:
        subprocess.run(["docker", "rm", "-f", container], capture_output=True, text=True)
        result.update({"hit_budget": 1, "error_category": "timeout", "gen_time_s": budget})
    except Exception as exc:
        result["error_category"] = _error_category(exc)
        result["error_message"] = str(exc)[-2000:]
    finally:
        auth.unlink(missing_ok=True)
    result["end_time"] = dt.datetime.now(dt.timezone.utc).isoformat()
    return result


def _error_category(exc: Exception) -> str:
    text = (type(exc).__name__ + " " + str(exc)).lower()
    if "timeout" in text or "timed out" in text:
        return "timeout"
    if "syntax" in text:
        return "syntax"
    # SlipCover cannot import some modules under Python 3.14; this is a
    # deterministic environment failure, not a transient provider error,
    # so it must never be retried as "api".
    if "measuring coverage" in text or "slipcover" in text:
        return "env"
    if "importable" in text or "empty coverage" in text:
        return "invalid_tests"
    if any(value in text for value in ("429", "401", "403", "unauthorized", "invalid_request", "api", "connection", "model")):
        return "api"
    if "memory" in text or "137" in text or "docker" in text or "module" in text or "backbone" in text:
        return "env"
    return "crash"


def run_task(row: dict[str, str], output_root: Path) -> dict[str, Any]:
    print(f"[{row['run_id']}] START -> Tool: {row['tool']} | Target: {row['suite']}:{row['unit_id']}", flush=True)
    if row["tool"] == "CoverUp":
        return run_coverup(row, output_root)
    if row["tool"] == "CodaMOSA":
        return run_codamosa(row, output_root)
    if row["tool"] == "Pynguin":
        return run_pynguin(row, output_root)
    if row["tool"] == "MuTAP":
        return run_mutap(row, output_root)
    raise ValueError("Unsupported tool: " + row["tool"])
