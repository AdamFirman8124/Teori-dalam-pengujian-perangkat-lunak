import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from matrix import generate_matrix


def test_pilot_matrix(tmp_path):
    path = tmp_path / "pilot.csv"
    # 8 units x ((Pynguin baseline) + 2 tools x 2 backbones) x R=2 = 8 x (2 + 8).
    assert generate_matrix(path, pilot=True) == 80
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8")))
    assert len({row["run_id"] for row in rows}) == 80
    assert Counter(row["suite"] for row in rows) == {"MT": 50, "CM": 30}
    assert {row["tool"] for row in rows} == {"Pynguin", "CodaMOSA", "CoverUp"}
    assert {row["backbone"] for row in rows} == {"", "B1", "B2"}
    # Pynguin carries no backbone and no model (baseline tool without LLM).
    assert all(row["model_requested"] == "" for row in rows if row["tool"] == "Pynguin")


def test_main_matrix(tmp_path):
    # 203 units x (10 Pynguin baseline + 40 LLM) = 10,150 runs, per the
    # pedoman Fase 6 design matrix (Pynguin MT 1,630 + CM 400; LLM 8,120).
    assert generate_matrix(tmp_path / "main.csv", pilot=False) == 10150
