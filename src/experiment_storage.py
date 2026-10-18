"""Safe, resumable storage for experiment snapshots.

A run is written to ``runs/<run_id>`` first. Active files change only after
a complete, valid run is available and its quality beats the active snapshot.
The old active pair is copied to one backup before promotion.
"""
from __future__ import annotations

import csv
import json
import os
import shutil
import tempfile
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path
import time


class ResultStore:
    """Store candidate runs and safely promote the best snapshot."""

    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        self.runs = self.root / "runs"
        self.backups = self.root / "backups"
        self.runs.mkdir(parents=True, exist_ok=True)
        self.backups.mkdir(parents=True, exist_ok=True)
        self.run_id = ""
        self.candidate: Path | None = None

    def begin(self, label: str = "run") -> str:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        safe = "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in label)
        self.run_id = f"{stamp}_{safe}"
        self.candidate = self.runs / self.run_id
        suffix = 1
        while self.candidate.exists():
            time.sleep(0.01)
            self.run_id = f"{stamp}_{safe}_{suffix}"
            self.candidate = self.runs / self.run_id
            suffix += 1
        self.candidate.mkdir(parents=True, exist_ok=False)
        return self.run_id

    @staticmethod
    def _atomic_write(path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, raw = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
        temp = Path(raw)
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temp, path)
        finally:
            temp.unlink(missing_ok=True)

    @staticmethod
    def _create_unique_directory(path: Path) -> Path:
        """Create ``path`` without overwriting an earlier backup.

        Notebook cells can be rerun with the same ``run_id``.  Backups are
        retained, so a collision gets a numeric suffix rather than raising
        ``FileExistsError`` or replacing the previous snapshot.
        """
        candidate = path
        suffix = 1
        while True:
            try:
                candidate.mkdir(parents=True, exist_ok=False)
                return candidate
            except FileExistsError:
                candidate = path.parent / f"{path.name}_{suffix}"
                suffix += 1

    @staticmethod
    def _csv_text(rows: list[dict]) -> str:
        if not rows:
            return ""
        columns = sorted({key for row in rows for key in row})
        stream = StringIO(newline="")
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
        return stream.getvalue()

    def checkpoint(self, rows: list[dict], statuses: list[dict]) -> None:
        if self.candidate is None:
            raise RuntimeError("ResultStore.begin() must be called first")
        self._atomic_write(self.candidate / "rows.csv", self._csv_text(rows))
        self._atomic_write(
            self.candidate / "status.json",
            json.dumps(statuses, indent=2, ensure_ascii=False) + "\n",
        )

    @staticmethod
    def _quality(rows: list[dict], statuses: list[dict]) -> tuple:
        ok = sum(item.get("status") == "OK" for item in statuses)
        values = []
        for row in rows:
            for key in ("pass_rate", "line_pct", "mutation_score"):
                value = row.get(key)
                try:
                    if value not in (None, ""):
                        values.append(float(value))
                except (TypeError, ValueError):
                    continue
        mean = sum(values) / len(values) if values else -1.0
        return ok, round(mean, 9), len(rows)

    @staticmethod
    def _read_active(root: Path) -> tuple[list[dict], list[dict]]:
        rows, statuses = [], []
        rows_path, status_path = root / "rows.csv", root / "status.json"
        if rows_path.exists() and rows_path.stat().st_size:
            with rows_path.open(encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
        if status_path.exists():
            try:
                loaded = json.loads(status_path.read_text(encoding="utf-8"))
                if isinstance(loaded, list):
                    statuses = loaded
            except (OSError, json.JSONDecodeError):
                pass
        return rows, statuses

    @staticmethod
    def mutant_set_conflicts(rows: list[dict]) -> dict:
        """Tasks whose successful rows used more than one mutant set.

        Comparing coverage/pass-rate/mutation-score across methods or models is
        only fair when every successful row on a task was measured against the
        identical mutant set.  A conflict means the comparison would not be
        apples-to-apples, so such a run must not be promoted as trustworthy.
        """
        seen: dict = {}
        conflicts: dict = {}
        for row in rows:
            task = (row.get("dataset"), str(row.get("task")))
            mutant_id = row.get("mutant_set_id")
            if mutant_id in (None, ""):
                continue
            previous = seen.setdefault(task, mutant_id)
            if previous != mutant_id:
                conflicts.setdefault(task, set()).update({previous, mutant_id})
        return {task: sorted(ids) for task, ids in conflicts.items()}

    @staticmethod
    def unmeasured_rows(rows: list[dict]) -> int:
        """Rows marked successful whose metrics are all missing.

        A harness/environment failure (e.g. a broken ``pytest`` launcher) makes
        every measurement collapse to ``pass_rate=0`` with empty ``line_pct``
        and ``mutation_score``.  Such rows are not results, and promoting them
        would publish zeros as if they were measurements.
        """
        unmeasured = 0
        for row in rows:
            values = []
            for key in ("line_pct", "branch_pct", "mutation_score", "pass_rate"):
                value = row.get(key)
                try:
                    if value not in (None, ""):
                        values.append(float(value))
                except (TypeError, ValueError):
                    continue
            if not values or all(value == 0.0 for value in values):
                unmeasured += 1
        return unmeasured

    def finalize(self, rows: list[dict], statuses: list[dict], *, expected_statuses: int) -> dict:
        """Save candidate and promote only when complete and no worse."""
        self.checkpoint(rows, statuses)
        conflicts = self.mutant_set_conflicts(rows)
        unmeasured = self.unmeasured_rows(rows)
        valid = len(statuses) == expected_statuses and not conflicts and all(
            item.get("status") in {"OK", "BLOCKED", "INVALID_GENERATED_TEST"}
            for item in statuses
        )
        old_rows, old_statuses = self._read_active(self.root)
        old_quality = self._quality(old_rows, old_statuses)
        new_quality = self._quality(rows, statuses)
        # Zero measured results means the harness never ran: never promote.
        trustworthy = bool(rows) and unmeasured < len(rows)
        promoted = valid and trustworthy and (not old_statuses or new_quality >= old_quality)
        backup = None
        if promoted:
            backup_path = self.backups / self.run_id
            if old_statuses or (self.root / "rows.csv").exists():
                backup_path = self._create_unique_directory(backup_path)
                for name in ("rows.csv", "status.json"):
                    source = self.root / name
                    if source.exists():
                        shutil.copy2(source, backup_path / name)
                backup = str(backup_path)
            self._atomic_write(self.root / "rows.csv", self._csv_text(rows))
            self._atomic_write(
                self.root / "status.json",
                json.dumps(statuses, indent=2, ensure_ascii=False) + "\n",
            )
        manifest = {
            "run_id": self.run_id, "valid": valid, "promoted": promoted,
            "backup": backup, "expected_statuses": expected_statuses,
            "actual_statuses": len(statuses), "old_quality": old_quality,
            "new_quality": new_quality, "unmeasured_rows": unmeasured,
            "trustworthy": trustworthy,
            "mutant_set_conflicts": {
                f"{dataset}:{task}": ids for (dataset, task), ids in conflicts.items()
            },
        }
        self._atomic_write(
            self.candidate / "manifest.json",
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        )
        return manifest

