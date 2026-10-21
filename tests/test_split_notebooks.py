import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "experiments_linux.ipynb"


def cells():
    data = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    return {c.get("id"): "".join(c.get("source", [])) for c in data["cells"]}


nb = cells()


def test_linux_notebook_name_is_os_specific():
    assert NOTEBOOK.name == "experiments_linux.ipynb"


def test_notebook_uses_canonical_model_label():
    assert "MODEL_ALIASES" in nb["c5d09b00"]
    assert "canonical_model_name" in nb["c5d09b00"]
    assert "BACKBONE_LABEL" not in nb["c5d09b00"]
    assert "_BB_LABEL = record_model_name(" in nb["c5d09b00"]
    source = nb["4ce9652a"]
    assert 'row["model"] = record_model_name(model)' in source
    assert 'row["provider_model"] = model' in source
    assert "BACKBONE_LABEL" not in source


def test_linux_notebook_runs_both_methods_with_safe_ram_profile():
    source = nb["c5d09b00"]
    assert "i5-11400F" in source and "RAM 16 GB" in source
    assert "'CPU_RESERVED_THREADS': '2'" in source
    assert "'TASK_WORKERS': '2'" in source
    assert "'AUTO_SCALE': '1'" in source
    assert "'CONFIG_MAX_LOAD': '2'" in source
    assert "'DESKTOP_HEADROOM_GB': '4'" in source
    assert "'CODAMOSA_RAM_GB_PER_WORKER': '5'" in source
    assert "'CODAMOSA_DOCKER_CPUS': '3'" in source
    # Kedua metode dibaca dari .env; tidak ada yang dikunci kosong.
    assert "COVERUP_MODELS = [coverup_model_name(m)" in source
    assert "COVERUP_MODELS = []" not in source
    assert "CODAMOSA_MODELS = [codamosa_model_name(m)" in source
    assert "CODAMOSA_MODELS = []" not in source
    assert "experiment_results_linux" in source
    assert "60a2d676" in nb


def test_linux_preflight_requires_docker_for_codamosa():
    preflight = nb["f68dcf13"]
    assert "if CODAMOSA_MODELS" in preflight
    assert "if shutil.which" in preflight or "docker" in preflight.lower()


def test_linux_readiness_uses_native_label():
    readiness = nb["b4501a3d"]
    assert "Linux native" in readiness
    assert "by_ram = max_load if not _CODAMOSA_ENABLED" in nb["4ce9652a"]


def test_linux_header_rejects_wsl_as_run_target():
    header = nb["52502ca7"]
    assert "Ubuntu native" in header
    assert "WSL tidak dipakai" in header
    assert "CoverUp" in header and "CodaMOSA" in header
