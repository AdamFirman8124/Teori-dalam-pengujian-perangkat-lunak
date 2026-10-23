#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from notebook_control import load_local_env
from protocol import load_config, require_environment


def request(backbone: str) -> dict:
    config = load_config()["backbones"][backbone]
    base = os.environ[config["base_url_env"]].rstrip("/")
    key = os.environ[config["api_key_env"]]
    payload = {
        "model": config["model_requested"],
        "messages": [{"role": "user", "content": "Call the echo tool with value exactly probe. You MUST use the echo function."}],
        "temperature": 0,
        "max_tokens": 128,
        "tools": [{
            "type": "function",
            "function": {
                "name": "echo",
                "description": "Return a value",
                "parameters": {
                    "type": "object",
                    "properties": {"value": {"type": "string"}},
                    "required": ["value"],
                },
            },
        }],
        "tool_choice": "required",
    }
    with httpx.Client(timeout=90) as client:
        response = client.post(base + "/chat/completions", headers={"Authorization": "Bearer " + key}, json=payload)
    # Some middleware emits SSE trailing data ("data: [DONE]") after the JSON
    # object, breaking response.json().  Parse only the first JSON object.
    try:
        body = response.json()
    except ValueError:
        first_line = response.text.split("\n", 1)[0]
        try:
            body = json.loads(first_line)
        except ValueError:
            body = {"error": {"message": response.text[:1000]}}
    if response.status_code != 200:
        message = str((body.get("error") or {}).get("message") or body)[:1000]
        supported = []
        match = re.search(r"Supported models? (?:are|is) ([^.]+)", message, re.I)
        if match:
            supported = [value.strip() for value in match.group(1).split(",")]
        return {
            "backbone": backbone,
            "passed": False,
            "model_requested": config["model_requested"],
            "model_returned": None,
            "function_calling": False,
            "http_status": response.status_code,
            "supported_models_reported": supported,
            "error": message,
            "action": (
                f"Configure {config['base_url_env']} and {config['api_key_env']} for an endpoint "
                f"that exposes {config['model_requested']}; do not replace B2 with auto because that "
                "would duplicate B1 and violate File B's two-backbone design."
            ),
        }
    choice = (body.get("choices") or [{}])[0]
    calls = (choice.get("message") or {}).get("tool_calls") or []
    usage = body.get("usage") or {}
    passed = bool(calls)
    return {
        "backbone": backbone,
        "passed": passed,
        "model_requested": config["model_requested"],
        "model_returned": body.get("model"),
        "function_calling": passed,
        "http_status": response.status_code,
        "tokens_in": usage.get("prompt_tokens", usage.get("input_tokens")),
        "tokens_out": usage.get("completion_tokens", usage.get("output_tokens")),
        "finish_reason": choice.get("finish_reason"),
        **({"error": "Endpoint returned no tool call"} if not passed else {}),
    }


class ProbeBlocked(RuntimeError):
    """Raised when no backbone passed, in which case no API task should start."""


def validate_gate(results: list[dict[str, object]], require_both: bool) -> int:
    failed = [result for result in results if not result.get("passed")]
    if not failed:
        return 0
    if require_both:
        message = (
            "PROBE GATE BLOCKED: "
            + ", ".join(str(result.get("backbone")) for result in failed)
            + ". No pilot runs were started. "
            + "Supply the missing endpoint/key and rerun scripts/probe_endpoints.py."
        )
        print("Probe details saved to", ROOT / "results" / "endpoint_probe.json")
        raise SystemExit(message)
    print("PROBE GATE DEGRADED:", ", ".join(str(result.get("backbone")) for result in failed))
    print("Rows for a failed backbone are blocked by the runner's probe gate.")
    return 0


def main() -> int:
    load_local_env()
    require_environment(load_config())
    results = []
    for backbone in ("B1", "B2"):
        try:
            results.append(request(backbone))
        except Exception as exc:
            results.append({
                "backbone": backbone,
                "passed": False,
                "model_requested": load_config()["backbones"][backbone]["model_requested"],
                "model_returned": None,
                "function_calling": False,
                "error": f"{type(exc).__name__}: {exc}",
            })
    path = ROOT / "results" / "endpoint_probe.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    for result in results:
        print(json.dumps(result, indent=2))
    failed = [result["backbone"] for result in results if not result.get("passed")]
    require_both = os.environ.get("PROBE_REQUIRE_BOTH", "1") == "1"
    if not failed:
        print("Both endpoint function-calling probes passed; wrote", path)
        return 0
    return validate_gate(results, require_both)


if __name__ == "__main__":
    raise SystemExit(main())
