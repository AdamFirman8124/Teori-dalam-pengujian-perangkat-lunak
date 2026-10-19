#!/usr/bin/env python3
"""Merge validated rows/status from a collaborator (e.g. MuTAP) without races."""
from __future__ import annotations

import argparse
import csv
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

KEY = ("method", "model", "dataset", "task", "run")
STATUS_KEY = ("method", "model", "dataset", "task")


def _read_rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _key(row: dict) -> tuple[str, ...]:
    return tuple(str(row.get(field) or "") for field in KEY)


def _status_key(row: dict) -> tuple[str, ...]:
    return tuple(str(row.get(field) or "") for field in STATUS_KEY)


def _merge(existing: list[dict], incoming: list[dict], replace: bool,
           key_fn=_key) -> list[dict]:
    merged = {key_fn(row): row for row in existing}
    for row in incoming:
        key = key_fn(row)
        if key in merged and merged[key] != row and not replace:
            raise ValueError(f"conflicting row {key}; pass --replace to prefer incoming")
        merged[key] = row
    return [merged[key] for key in sorted(merged)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("incoming", type=Path, help="folder containing rows.csv and status.json")
    parser.add_argument("--target", type=Path, default=Path("experiment_results"))
    parser.add_argument("--replace", action="store_true")
    args = parser.parse_args()

    incoming_rows = args.incoming / "rows.csv"
    incoming_status = args.incoming / "status.json"
    if not incoming_rows.is_file() or not incoming_status.is_file():
        parser.error("incoming folder must contain rows.csv and status.json")

    target = args.target.resolve()
    target.mkdir(parents=True, exist_ok=True)
    old_rows = _read_rows(target / "rows.csv") if (target / "rows.csv").is_file() else []
    new_rows = _read_rows(incoming_rows)
    old_status = json.loads((target / "status.json").read_text(encoding="utf-8")) \
        if (target / "status.json").is_file() else []
    new_status = json.loads(incoming_status.read_text(encoding="utf-8"))
    if not isinstance(new_status, list):
        parser.error("incoming status.json must be a JSON array")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = target / "backups" / ("pre-collaborator-merge-" + stamp)
    backup.mkdir(parents=True)
    for name in ("rows.csv", "status.json"):
        source = target / name
        if source.is_file():
            shutil.copy2(source, backup / name)

    rows = _merge(old_rows, new_rows, args.replace)
    statuses = _merge(old_status, new_status, args.replace, _status_key)
    fields = sorted({key for row in rows for key in row})
    with (target / "rows.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    (target / "status.json").write_text(
        json.dumps(statuses, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"merged rows={len(rows)} statuses={len(statuses)}; backup={backup}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
