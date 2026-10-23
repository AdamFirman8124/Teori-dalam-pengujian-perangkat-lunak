import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from inventory import cm_units, mt_units, write_inventory


def test_dataset_counts():
    assert len(mt_units()) == 163
    assert len(cm_units()) == 425


def test_cm_sampling(tmp_path):
    assert write_inventory(tmp_path) == (163, 425)
    with (tmp_path / "cm_sample.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert sum(int(row["is_pilot"]) for row in rows) == 3
    sample = [row for row in rows if int(row["in_sample"])]
    assert len(sample) == 40
    assert not any(int(row["is_pilot"]) and int(row["in_sample"]) for row in rows)
    assert max(Counter(row["project"] for row in sample).values()) <= 10
    assert {row["stratum"] for row in sample} == {"L0B0", "L0B1", "L1B0", "L1B1", "L1B2", "L2B0", "L2B1", "L2B2"}
