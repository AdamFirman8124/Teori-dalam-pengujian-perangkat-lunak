#!/usr/bin/env python3
"""Summarize run failures by reproducible error category."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


def category(message: str) -> str:
    text = (message or "").lower()
    checks = (
        ("invalid_generated_test", "invalid generated suite"),
        ("rate limit", "provider rate limit"),
        ("429", "provider rate limit"),
        ("timeout", "timeout"),
        ("oom", "resource/OOM"),
        ("exit code 137", "resource/OOM"),
        ("modulenotfounderror", "dependency/import"),
        ("no matching distribution", "dependency/import"),
        ("syntaxerror", "syntax/parse"),
        ("tidak menghasilkan test", "model produced no test"),
    )
    return next((label for marker, label in checks if marker in text), "other")


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "experiment_results_linux/status.json")
    statuses = json.loads(path.read_text(encoding="utf-8"))
    counts = Counter(category(x.get("message", "")) for x in statuses if x.get("status") != "OK")
    print(json.dumps(dict(sorted(counts.items())), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
