#!/usr/bin/env python3
"""Classify experiment statuses without calling an LLM.

Examples:
    python tools/classify_failures.py --source experiment_results
    python tools/classify_failures.py --status path/to/status.json --outdir reports
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INFRASTRUCTURE_RULES = (
    ("OUT_OF_MEMORY", ("codamosa_oom", "exit code 137", "sigkill", "cannot allocate memory", "out of memory")),
    ("CONTAINER_MOUNT", ("need to specify a mount", "mount to /input", "no such file or directory: '/input'")),
    ("PROVIDER_RATE_LIMIT", ("rate limit", "too many requests", "status code 429", "error 429")),
    ("PROVIDER_OR_NETWORK", ("service unavailable", "bad gateway", "connection error", "connection reset", "failed to resolve", "dns", "timed out", "timeout")),
    ("DOCKER_INFRASTRUCTURE", ("docker daemon", "cannot connect to the docker", "docker exit code")),
)

MODEL_RULES = (
    ("INVALID_SUITE", ("invalid_generated_test", "no test functions", "no assertions", "empty/comment-only suite", "suite utama")),
    ("NO_GENERATED_TEST", ("tidak menghasilkan test", "does not achieve full coverage", "test doesn't improve coverage", "too many attempts")),
)


def read_status(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Status must be a JSON array: {path}")
    return [item for item in data if isinstance(item, dict)]


def latest_status(source: Path) -> tuple[Path, str]:
    runs = source / "runs"
    candidates = []
    if runs.is_dir():
        candidates = sorted(
            (path for path in runs.iterdir() if (path / "status.json").exists()),
            key=lambda path: (path / "status.json").stat().st_mtime,
            reverse=True,
        )
    if candidates:
        path = candidates[0] / "status.json"
        return path, candidates[0].name
    path = source / "status.json"
    if path.exists():
        return path, "active"
    raise FileNotFoundError(f"No status.json found under {source}")


def _match(text: str, rules: tuple) -> tuple[str, str] | None:
    for reason, markers in rules:
        for marker in markers:
            if marker in text:
                return reason, marker
    return None


def classify(item: dict) -> dict:
    status = str(item.get("status") or "UNKNOWN")
    message = str(item.get("message") or "")
    text = message.lower()

    if status == "OK":
        category, reason, marker, retry = "success", "OK", "", False
    else:
        infra = _match(text, INFRASTRUCTURE_RULES)
        model = _match(text, MODEL_RULES)
        if infra:
            category, reason, marker, retry = "infrastructure_failure", infra[0], infra[1], True
        elif status == "INVALID_GENERATED_TEST" or model:
            match = model or ("INVALID_SUITE", "invalid_generated_test")
            category, reason, marker, retry = "model_failure", match[0], match[1], False
        else:
            category, reason, marker, retry = "unknown_failure", "UNCLASSIFIED", "", None

    return {
        "method": item.get("method"),
        "model": item.get("model"),
        "dataset": item.get("dataset"),
        "task": str(item.get("task") or ""),
        "status": status,
        "failure_category": category,
        "failure_reason": reason,
        "matched_marker": marker,
        "recommended_retry": retry,
        "message": message,
    }


def summarize(records: list[dict], status_path: Path, run_id: str) -> dict:
    category_counts = Counter(record["failure_category"] for record in records)
    status_counts = Counter(record["status"] for record in records)
    reason_counts = Counter(record["failure_reason"] for record in records)
    per_method: dict[str, Counter] = defaultdict(Counter)
    for record in records:
        method = str(record.get("method") or "UNKNOWN")
        per_method[method][record["failure_category"]] += 1

    return {
        "run_id": run_id,
        "status_path": str(status_path.resolve()),
        "total_statuses": len(records),
        "status_counts": dict(sorted(status_counts.items())),
        "category_counts": dict(sorted(category_counts.items())),
        "reason_counts": dict(sorted(reason_counts.items())),
        "per_method": {method: dict(sorted(counts.items())) for method, counts in sorted(per_method.items())},
        "retry_keys": [
            {key: record.get(key) for key in ("method", "model", "dataset", "task", "failure_reason")}
            for record in records if record["recommended_retry"] is True
        ],
        "model_failure_keys": [
            {key: record.get(key) for key in ("method", "model", "dataset", "task", "failure_reason")}
            for record in records if record["failure_category"] == "model_failure"
        ],
        "unknown_failure_keys": [
            {key: record.get(key) for key in ("method", "model", "dataset", "task", "failure_reason")}
            for record in records if record["failure_category"] == "unknown_failure"
        ],
    }


def write_csv(path: Path, records: list[dict]) -> None:
    columns = (
        "method", "model", "dataset", "task", "status", "failure_category",
        "failure_reason", "matched_marker", "recommended_retry", "message",
    )
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(records)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=str(ROOT / "experiment_results"))
    parser.add_argument("--status", help="Explicit status.json; overrides --source")
    parser.add_argument("--outdir", help="Defaults to <source>/failure_analysis")
    args = parser.parse_args()

    source = Path(args.source)
    if args.status:
        status_path, run_id = Path(args.status), Path(args.status).parent.name
    else:
        status_path, run_id = latest_status(source)
    records = [classify(item) for item in read_status(status_path)]
    summary = summarize(records, status_path, run_id)

    outdir = Path(args.outdir) if args.outdir else source / "failure_analysis"
    outdir.mkdir(parents=True, exist_ok=True)
    write_csv(outdir / "failure_classification.csv", records)
    (outdir / "failure_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(f"Run: {run_id}")
    print(f"Status: {status_path}")
    print(f"Category counts: {summary['category_counts']}")
    print(f"Retry infrastructure failures: {len(summary['retry_keys'])}")
    print(f"Model failures to retain: {len(summary['model_failure_keys'])}")
    print(f"Output: {outdir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
