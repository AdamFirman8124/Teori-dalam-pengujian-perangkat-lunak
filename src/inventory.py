from __future__ import annotations

import ast
import csv
import random
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from statistics import quantiles

from protocol import load_config, resolve_path


@dataclass(frozen=True)
class CMUnit:
    base: str
    unit_id: str

    @property
    def project(self) -> str:
        path = Path(self.base)
        return path.parts[1] if len(path.parts) > 1 else path.name


def mt_units() -> list[str]:
    root = resolve_path(load_config()["paths"]["mt"])
    return sorted(
        (path.name for path in root.iterdir() if path.is_dir() and path.name[1:].isdigit()),
        key=lambda value: int(value[1:]),
    )


def cm_units() -> list[CMUnit]:
    manifest = resolve_path(load_config()["paths"]["cm_manifest"])
    with manifest.open(newline="", encoding="utf-8") as handle:
        return [CMUnit(base=row[0], unit_id=row[1]) for row in csv.reader(handle) if row]


def module_path(unit: CMUnit) -> Path:
    root = resolve_path(load_config()["paths"]["cm_root"])
    base = root / unit.base
    relative = Path(*unit.unit_id.split("."))
    file_path = base / relative.with_suffix(".py")
    package_path = base / relative / "__init__.py"
    if file_path.is_file():
        return file_path
    if package_path.is_file():
        return package_path
    raise FileNotFoundError(f"Cannot resolve {unit.unit_id} under {base}")


def source_metrics(path: Path) -> tuple[int, int, int]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    loc = len(lines)
    sloc = sum(bool(line.strip()) and not line.lstrip().startswith("#") for line in lines)
    tree = ast.parse(text)
    branches = sum(
        isinstance(node, (ast.If, ast.For, ast.AsyncFor, ast.While, ast.Try, ast.Match, ast.IfExp))
        for node in ast.walk(tree)
    )
    branches += sum(len(node.handlers) for node in ast.walk(tree) if isinstance(node, ast.Try))
    return loc, sloc, branches


def tertile(value: int, cuts: tuple[float, float]) -> int:
    if value <= cuts[0]:
        return 0
    if value <= cuts[1]:
        return 1
    return 2


def build_characteristics() -> list[dict[str, object]]:
    rows = []
    for unit in cm_units():
        path = module_path(unit)
        loc, sloc, branches = source_metrics(path)
        rows.append({"unit_id": unit.unit_id, "project": unit.project, "loc": loc, "sloc": sloc, "n_branches": branches})
    loc_cuts = tuple(quantiles([int(row["loc"]) for row in rows], n=3))
    branch_cuts = tuple(quantiles([int(row["n_branches"]) for row in rows], n=3))
    for row in rows:
        row["stratum"] = f"L{tertile(int(row['loc']), loc_cuts)}B{tertile(int(row['n_branches']), branch_cuts)}"
        row["is_pilot"] = 0
        row["in_sample"] = 0
    return rows


def choose_units(rows: list[dict[str, object]], seed: int, sample_size: int, project_fraction_cap: float) -> None:
    rng = random.Random(seed)
    pilot_candidates = sorted(rows, key=lambda row: (int(row["loc"]), int(row["n_branches"]), str(row["unit_id"])))
    pilot_projects: set[str] = set()
    pilots = []
    for row in pilot_candidates:
        project = str(row["project"])
        if project not in pilot_projects:
            pilots.append(row)
            pilot_projects.add(project)
        if len(pilots) == 3:
            break
    for row in pilots:
        row["is_pilot"] = 1

    groups: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        if not row["is_pilot"]:
            groups.setdefault(str(row["stratum"]), []).append(row)
    for group in groups.values():
        rng.shuffle(group)

    cap = max(1, int(sample_size * project_fraction_cap))
    selected = []
    project_counts: Counter[str] = Counter()
    strata = sorted(groups)
    while len(selected) < sample_size:
        progressed = False
        for stratum in strata:
            group = groups[stratum]
            for index, row in enumerate(group):
                project = str(row["project"])
                if project_counts[project] < cap:
                    selected.append(group.pop(index))
                    project_counts[project] += 1
                    progressed = True
                    break
            if len(selected) == sample_size:
                break
        if not progressed:
            raise RuntimeError("Cannot satisfy CM sample project cap")
    for row in selected:
        row["in_sample"] = 1


def write_inventory(output: Path) -> tuple[int, int]:
    config = load_config()
    rows = build_characteristics()
    choose_units(
        rows,
        seed=int(config["experiment"]["seed"]),
        sample_size=int(config["experiment"]["cm_sample_size"]),
        project_fraction_cap=float(config["experiment"]["cm_project_fraction_cap"]),
    )
    output.mkdir(parents=True, exist_ok=True)
    fields = ["unit_id", "project", "loc", "sloc", "n_branches", "stratum", "is_pilot", "in_sample"]
    with (output / "module_characteristics.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    with (output / "cm_sample.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(row for row in rows if row["is_pilot"] or row["in_sample"])
    return len(mt_units()), len(rows)
