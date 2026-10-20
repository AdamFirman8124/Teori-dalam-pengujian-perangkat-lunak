import json
import pathlib

ROOT = pathlib.Path(r"C:\Users\adamf\Documents\Kuliah\ITS\Semester 1\Topik Dalam Pengujian Perangkat Lunak\Project")
NOTEBOOKS = {
    "coverup": ROOT / "experiments_coverup_windows.ipynb",
    "codamosa": ROOT / "experiments_codamosa_linux.ipynb",
}


def cells(name):
    data = json.loads(NOTEBOOKS[name].read_text(encoding="utf-8"))
    return {c.get("id"): "".join(c.get("source", [])) for c in data["cells"]}


coverup = cells("coverup")
codamosa = cells("codamosa")


def test_split_notebook_names_are_method_and_os_specific():
    assert NOTEBOOKS["coverup"].name == "experiments_coverup_windows.ipynb"
    assert NOTEBOOKS["codamosa"].name == "experiments_codamosa_linux.ipynb"


def test_notebooks_use_real_sol_model_without_backbone_alias():
    for source in (coverup["c5d09b00"], codamosa["c5d09b00"]):
        assert "gpt-5.6-sol" in source
        assert "gpt-5.6-luna" not in source
        assert "BACKBONE_LABEL" not in source
        assert "_BB_LABEL = (COVERUP_MODELS or CODAMOSA_MODELS)[0].split('/')[-1]" in source
    for source in (coverup["4ce9652a"], codamosa["4ce9652a"]):
        assert 'row["model"] = model' in source
        assert "BACKBONE_LABEL" not in source


def test_windows_coverup_has_i5_16gb_profile_and_no_codamosa():
    source = coverup["c5d09b00"]
    assert "i5-11400F" in source and "RAM 16 GB" in source
    assert "'CPU_RESERVED_THREADS': '2'" in source
    assert "'TASK_WORKERS': '3'" in source
    assert "'EVAL_MUTANT_WORKERS': '2'" in source
    assert "CODAMOSA_MODELS = []" in source
    assert "experiment_results_coverup_windows" in source
    assert "60a2d676" not in coverup


def test_linux_codamosa_has_safe_ram_profile_and_no_coverup():
    source = codamosa["c5d09b00"]
    assert "i5-11400F" in source and "RAM 16 GB" in source
    assert "'CPU_RESERVED_THREADS': '2'" in source
    assert "'TASK_WORKERS': '2'" in source
    assert "'AUTO_SCALE': '1'" in source
    assert "'CONFIG_MAX_LOAD': '2'" in source
    assert "'DESKTOP_HEADROOM_GB': '4'" in source
    assert "'CODAMOSA_RAM_GB_PER_WORKER': '5'" in source
    assert "'CODAMOSA_DOCKER_CPUS': '3'" in source
    assert "COVERUP_MODELS = []" in source
    assert "experiment_results_codamosa_linux" in source
    assert "60a2d676" in codamosa


def test_windows_preflight_does_not_require_docker():
    preflight = coverup["f68dcf13"]
    assert "if CODAMOSA_MODELS" in preflight
    assert "Dilewati: notebook ini tidak memakai Docker." in preflight


def test_linux_header_rejects_wsl_as_run_target():
    header = codamosa[next(key for key in codamosa if key and key not in {
        "c5d09b00", "devreadiness-md", "b4501a3d", "a9f680bb", "aae5cac3",
        "f68dcf13", "60a2d676", "000d81a2", "4ce9652a", "fb2ed2d1",
        "dc51281c", "valid-comparison-md", "valid-comparison-chart",
        "llm-calls-table-md", "llm-calls-table", "suite-metrics-table-md",
        "suite-metrics-table", "wilcoxon-table-md", "wilcoxon-table",
        "paper-tables-md", "paper-tables"
    })]
    assert "Ubuntu native" in header
    assert "WSL tidak dipakai" in header
