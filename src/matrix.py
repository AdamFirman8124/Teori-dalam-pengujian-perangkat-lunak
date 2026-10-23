from __future__ import annotations

import csv
import hashlib
import random
from pathlib import Path

from inventory import mt_units
from protocol import ROOT, load_config


def stable_seed(base: int, *parts: object) -> int:
    value = "|".join(map(str, (base, *parts))).encode()
    return int.from_bytes(hashlib.sha256(value).digest()[:8], "big") & 0x7FFFFFFF


def selected_cm(pilot: bool) -> list[dict[str, str]]:
    with (ROOT / "results" / "cm_sample.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    flag = "is_pilot" if pilot else "in_sample"
    return [row for row in rows if row[flag] == "1"]


def generate_matrix(output: Path, pilot: bool) -> int:
    config = load_config()
    experiment = config["experiment"]
    repetitions = int(experiment["pilot_repetitions"] if pilot else experiment["repetitions"])
    base_seed = int(experiment["seed"])
    mt = mt_units()[:5] if pilot else mt_units()
    cm = selected_cm(pilot)
    rows = []
    for suite, units in (("MT", [{"unit_id": value, "project": "MuTAP-benchmarks"} for value in mt]), ("CM", cm)):
        for tool in ("CodaMOSA", "CoverUp"):
            for backbone, model in config["backbones"].items():
                for unit in units:
                    for run_idx in range(1, repetitions + 1):
                        unit_id = unit["unit_id"]
                        rows.append({
                            "run_id": f"{suite}-{tool.lower()}-{backbone}-{unit_id.replace('.', '_')}-r{run_idx:02d}",
                            "suite": suite,
                            "unit_id": unit_id,
                            "project": unit["project"],
                            "tool": tool,
                            "backbone": backbone,
                            "model_requested": model["model_requested"],
                            "run_idx": run_idx,
                            "seed": stable_seed(base_seed, suite, tool, backbone, unit_id, run_idx),
                            "status": "pending",
                        })
    rng = random.Random(base_seed)
    rng.shuffle(rows)
    fields = list(rows[0])
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)
