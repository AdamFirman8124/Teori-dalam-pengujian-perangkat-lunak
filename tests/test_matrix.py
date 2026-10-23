import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from matrix import generate_matrix


def test_pilot_matrix(tmp_path):
    path = tmp_path / "pilot.csv"
    assert generate_matrix(path, pilot=True) == 64
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8")))
    assert len({row["run_id"] for row in rows}) == 64
    assert Counter(row["suite"] for row in rows) == {"MT": 40, "CM": 24}
    assert {row["tool"] for row in rows} == {"CodaMOSA", "CoverUp"}
    assert {row["backbone"] for row in rows} == {"B1", "B2"}


def test_main_matrix(tmp_path):
    assert generate_matrix(tmp_path / "main.csv", pilot=False) == 8120
