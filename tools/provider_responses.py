"""Consolidate every provider round-trip into ONE file with clear status.

Reads all per-call JSONL files written by CoverUp/CODAMOSA and produces:
  experiment_results/provider_responses.jsonl   one line per provider call
  experiment_results/provider_responses_summary.md  human-readable summary

Each line classifies the outcome so "error" and "cache hit" are no longer
confusing:
  outcome = "error" | "cache_hit" | "ok"
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "experiment_results"
LLM = OUT / "llm_calls"

CACHE_HEADER_KEYS = ("x-cache", "cf-cache-status", "x-litellm-cache-key",
                     "x-cache-status", "cache-status", "x-proxy-cache")

# Token/cost values for an error cannot be inferred when the provider omits a
# usage block.  Keep them null (unknown), never zero (free).


def _cache_hit(entry: dict) -> bool:
    if entry.get("cache_hit") is True:
        return True
    # Prompt cache usage is authoritative even when no cache header is exposed.
    if int(entry.get("cache_read_tokens") or 0) > 0:
        return True
    headers = entry.get("response_headers") or {}
    if isinstance(headers, dict):
        for key, value in headers.items():
            low = str(key).lower()
            if any(token in low for token in CACHE_HEADER_KEYS):
                if "hit" in str(value).lower():
                    return True
    return False


def _error_code(entry: dict) -> str:
    raw = entry.get("error")
    if not raw:
        return ""
    text = str(raw)
    for code in ("upstream_error", "rate_limit_exceeded", "insufficient_quota",
                 "invalid_request_error", "model_not_found", "timeout"):
        if code in text:
            return code
    return text[:120]


def _classify(entry: dict) -> str:
    status = entry.get("status_code")
    if entry.get("error") or (isinstance(status, int) and status >= 400):
        return "error"
    if _cache_hit(entry):
        return "cache_hit"
    return "ok"


def main() -> int:
    records = []
    if LLM.exists():
        for path in sorted(LLM.rglob("*.jsonl")):
            try:
                rel = path.relative_to(LLM)
                method, dataset, task = rel.parts[0], rel.parts[-2], path.stem
                model = "/".join(rel.parts[1:-2]).replace("openai_", "openai/")
            except (ValueError, IndexError):
                continue
            with path.open(encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    outcome = _classify(entry)
                    prompt_tokens = entry.get("prompt_tokens")
                    completion_tokens = entry.get("completion_tokens")
                    total_tokens = entry.get("total_tokens")
                    cost_usd = entry.get("cost_usd")
                    # Historical error logs hard-coded zero even when the web
                    # dashboard billed tokens. Treat that as unknown, not free.
                    if outcome == "error" and not entry.get("usage_reported"):
                        if total_tokens in (0, "0", None):
                            prompt_tokens = completion_tokens = total_tokens = None
                        if cost_usd in (0, "0", None):
                            cost_usd = None
                    records.append({
                        "ts": entry.get("ts"),
                        "method": method,
                        "model": entry.get("model") or model,
                        "dataset": dataset,
                        "task": task,
                        "outcome": outcome,
                        "status_code": entry.get("status_code"),
                        "error_code": _error_code(entry),
                        "cache_hit": outcome == "cache_hit",
                        "latency_s": entry.get("latency_s"),
                        "prompt_tokens": prompt_tokens,
                        "completion_tokens": completion_tokens,
                        "total_tokens": total_tokens,
                        "cache_read_tokens": int(entry.get("cache_read_tokens") or 0),
                        "cache_write_tokens": int(entry.get("cache_write_tokens") or 0),
                        "cost_usd": cost_usd,
                        "usage_reported": bool(entry.get("usage_reported"))
                        or total_tokens not in (None, 0),
                        "billed_unknown": outcome == "error" and total_tokens is None,
                        "output_chars": len(str(entry.get("output") or "")),
                        "error_message": str(entry.get("error") or "")[:500],
                    })

    target = OUT / "provider_responses.jsonl"
    with target.open("w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    total = len(records)
    by_outcome = Counter(r["outcome"] for r in records)
    by_error = Counter(r["error_code"] for r in records if r["outcome"] == "error")
    token_total = sum(int(r.get("total_tokens") or 0) for r in records)
    token_cache_read = sum(int(r.get("cache_read_tokens") or 0) for r in records)
    token_cache_write = sum(int(r.get("cache_write_tokens") or 0) for r in records)
    billed_unknown = sum(bool(r.get("billed_unknown")) for r in records)
    per_task = defaultdict(Counter)
    for r in records:
        per_task[(r["method"], r["model"])][r["outcome"]] += 1

    lines = ["# Provider responses (satu file)", "",
             f"- Total panggilan: **{total}**",
             f"- `ok`        : {by_outcome.get('ok', 0)}",
             f"- `cache_hit` : {by_outcome.get('cache_hit', 0)}",
             f"- `error`     : {by_outcome.get('error', 0)}",
             f"- Total token tercatat : **{token_total}** (termin pembaca cache: {token_cache_read}, "
             f"penulis cache: {token_cache_write}; keduanya subset dari prompt, bukan tambahan)",
             f"- Error yang tokennya tidak dilaporkan provider: **{billed_unknown}** "
             "(tetap ditagih, nilainya tidak dapat direkonstruksi dari log)",
             "", "## Error per kode"]

    if by_error:
        for code, count in by_error.most_common():
            lines.append(f"- `{code}`: {count}")
    else:
        lines.append("- (tidak ada)")
    lines += ["", "## Per metode + model"]
    for (method, model), counts in sorted(per_task.items()):
        detail = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
        lines.append(f"- **{method} / {model}**: {detail}")
    lines += ["", f"Detail per panggilan: `{target.relative_to(ROOT)}`", ""]

    (OUT / "provider_responses_summary.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {target} ({total} calls)")
    print("outcomes:", dict(by_outcome))
    if by_error:
        print("errors:", dict(by_error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
