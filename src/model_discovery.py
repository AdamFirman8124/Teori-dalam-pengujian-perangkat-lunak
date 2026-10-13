"""Discover and probe the LLM models available on the provider at run time.

Before an experiment starts we:

1. query ``GET /models`` to list every model the gateway currently offers;
2. probe each model with a *minimal* chat request (a handful of tokens) to learn
   which ones actually respond right now;
3. record everything - run timestamp, available models, unavailable models and
   the reason - into an inspectable report so the dataset documents exactly what
   was tried and when.

Nothing here is required for the experiment to run: if discovery fails the
result is reported as "unknown" rather than crashing the run.
"""
from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone


@dataclass
class ModelProbe:
    name: str
    available: bool
    status: str                 # OK | UNAVAILABLE | ERROR
    detail: str = ""
    latency_s: float | None = None
    http_status: int | None = None


@dataclass
class DiscoveryReport:
    timestamp_utc: str = ""
    base_url: str = ""
    models_endpoint: str = ""
    listed_models: list[str] = field(default_factory=list)
    available_models: list[str] = field(default_factory=list)
    unavailable_models: list[str] = field(default_factory=list)
    probes: list[dict] = field(default_factory=list)
    list_ok: bool = False
    list_error: str = ""
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


def _now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def list_models(base_url: str, api_key: str, *, timeout: float = 30.0) -> tuple[list[str], str]:
    """Return (model_ids, error).  ``model_ids`` is empty on failure."""
    url = base_url.rstrip("/") + "/models"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {api_key}"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.load(resp)
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
        return [], f"{type(exc).__name__}: {exc}"

    items = payload.get("data", payload if isinstance(payload, list) else [])
    ids: list[str] = []
    for item in items:
        if isinstance(item, dict):
            mid = item.get("id") or item.get("name")
            if mid:
                ids.append(str(mid))
        elif isinstance(item, str):
            ids.append(item)
    return ids, ""


def probe_model(base_url: str, api_key: str, model: str, *,
                completions_path: str = "/chat/completions",
                timeout: float = 60.0, max_tokens: int = 1) -> ModelProbe:
    """Send a tiny request to check whether ``model`` actually works now.

    Uses one token of output so probing the whole catalogue costs almost
    nothing.  A response (even an empty one) means the model is reachable;
    HTTP/connection failures mark it UNAVAILABLE.
    """
    url = base_url.rstrip("/") + completions_path
    body = {
        "model": model,
        "messages": [{"role": "user", "content": "ping"}],
        "max_tokens": max_tokens,
        "temperature": 0,
    }
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url, data=data,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            resp.read()
            latency = time.perf_counter() - started
            return ModelProbe(model, True, "OK", "responded", round(latency, 3),
                              getattr(resp, "status", 200))
    except urllib.error.HTTPError as exc:
        detail = ""
        try:
            detail = exc.read().decode("utf-8", "replace")[:300]
        except Exception:
            pass
        return ModelProbe(model, False, "UNAVAILABLE",
                          f"HTTP {exc.code}: {detail}", None, exc.code)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return ModelProbe(model, False, "ERROR", f"{type(exc).__name__}: {exc}")


def discover_and_probe(base_url: str, api_key: str, *,
                       completions_path: str = "/chat/completions",
                       probe: bool = True,
                       only: list[str] | None = None,
                       include: str = "",
                       timeout: float = 60.0,
                       workers: int = 8) -> DiscoveryReport:
    """Full discovery: list models, optionally probe each one.

    Probing is parallelised (``workers`` concurrent requests) because an
    unresponsive model would otherwise stall the whole catalogue behind its
    timeout.  Order is preserved for a stable report.

    ``include`` is a regex; when set, only matching model ids are probed.  This
    keeps the experiment to a chosen family (e.g. ``gpt|claude``) without paying
    probe requests for the rest of the catalogue.
    """
    report = DiscoveryReport(
        timestamp_utc=_now_utc(),
        base_url=base_url,
        models_endpoint=base_url.rstrip("/") + "/models",
    )
    if not api_key:
        report.list_error = "no API key configured"
        report.notes.append("Discovery skipped: missing API key.")
        return report

    ids, err = list_models(base_url, api_key)
    report.listed_models = ids
    report.list_ok = not err
    report.list_error = err
    if err:
        report.notes.append("Could not list models; discovery incomplete.")
        return report
    if not ids:
        report.notes.append("Provider returned an empty model list.")

    if only:
        ids = [m for m in ids if m in only]
    if include:
        _re = re.compile(include, re.IGNORECASE)
        ids = [m for m in ids if _re.search(m)]

    if probe:
        from concurrent.futures import ThreadPoolExecutor
        n = max(1, min(workers, len(ids) or 1))
        with ThreadPoolExecutor(max_workers=n, thread_name_prefix="model-probe") as ex:
            results = list(ex.map(
                lambda m: probe_model(base_url, api_key, m,
                                      completions_path=completions_path, timeout=timeout),
                ids,
            ))
        for p in results:
            report.probes.append(asdict(p))
            (report.available_models if p.available else report.unavailable_models).append(p.name)
    else:
        report.available_models = list(ids)

    return report


def write_report(report: DiscoveryReport, path) -> None:
    """Write the discovery report as pretty JSON, creating parent dirs."""
    from pathlib import Path
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(report.to_dict(), indent=2, ensure_ascii=False) + "\n",
                 encoding="utf-8")


def render_markdown(report: DiscoveryReport) -> str:
    """Human-readable summary suitable for the experiment results."""
    lines = [
        "# Model Discovery Report",
        "",
        f"- **Run time (UTC):** {report.timestamp_utc}",
        f"- **Provider:** {report.base_url}",
        f"- **Models endpoint:** {report.models_endpoint}",
        f"- **Models listed:** {len(report.listed_models)}",
        f"- **Available now:** {len(report.available_models)}",
        f"- **Unavailable:** {len(report.unavailable_models)}",
        f"- **List succeeded:** {report.list_ok}",
    ]
    if report.list_error:
        lines.append(f"- **List error:** {report.list_error}")
    lines.append("")
    if report.available_models:
        lines += ["## Available models", ""]
        lines += [f"- `{m}`" for m in report.available_models]
        lines.append("")
    if report.unavailable_models:
        lines += ["## Unavailable models", ""]
        detail = {p["name"]: p for p in report.probes}
        for m in report.unavailable_models:
            why = detail.get(m, {}).get("detail", "")
            why = " ".join(why.split())  # collapse newlines for a tidy table
            lines.append(f"- `{m}` - {why}")
        lines.append("")
    if report.notes:
        lines += ["## Notes", ""] + [f"- {n}" for n in report.notes]
        lines.append("")
    return "\n".join(lines)
