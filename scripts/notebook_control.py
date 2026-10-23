from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCAL_ENV = ROOT / "config" / "local.env"


def load_local_env() -> list[str]:
    loaded = []
    if not LOCAL_ENV.exists():
        return loaded
    for raw in LOCAL_ENV.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        if value and value != "REPLACE_ME":
            os.environ[name] = value
            loaded.append(name)
    return loaded


def presence() -> dict[str, bool]:
    return {
        name: bool(os.environ.get(name))
        for name in ("LLM_API_KEY", "LLM_BASE_URL", "LLM_API_KEY_B2", "LLM_BASE_URL_B2")
    }


def run(command: list[str], *, timeout: int = 600, check: bool = True) -> subprocess.CompletedProcess[str]:
    print("$", " ".join(command))
    started = time.monotonic()
    result = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
    print(result.stdout)
    print(f"exit={result.returncode} elapsed={time.monotonic() - started:.1f}s")
    if check and result.returncode:
        detail = {
            2: "Protocol gate blocked. Read the command output and fix the stated configuration; no paid run was started.",
        }.get(result.returncode, "Command failed; read the output above for the actionable error.")
        raise RuntimeError(f"Command failed with exit code {result.returncode}. {detail}")
    return result


def status() -> dict[str, object]:
    files = {}
    for name in ("pilot_matrix.csv", "pilot_results.csv", "run_matrix.csv", "results.csv"):
        path = ROOT / "results" / name
        if path.exists():
            with path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.DictReader(handle))
            files[name] = {
                "rows": len(rows),
                "ok": sum(row.get("status") == "ok" for row in rows),
                "failed": sum(row.get("status") == "failed" for row in rows),
                "pending": sum(row.get("status") == "pending" for row in rows),
                "cost_usd": round(sum(float(row.get("cost_usd") or 0) for row in rows), 6),
            }
    return {"credentials": presence(), "files": files}


def print_status() -> None:
    print(json.dumps(status(), indent=2))
