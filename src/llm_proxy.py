from __future__ import annotations

import json
import os
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

LOG_LOCK = threading.Lock()


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
    with LOG_LOCK, path.open("a", encoding="utf-8") as handle:
        handle.write(payload)
        handle.flush()


def usage(response: dict[str, Any]) -> tuple[int | None, int | None]:
    data = response.get("usage") or {}
    return data.get("prompt_tokens", data.get("input_tokens")), data.get("completion_tokens", data.get("output_tokens"))


class ProxyHandler(BaseHTTPRequestHandler):
    server_version = "ExperimentLLMProxy/1"

    def log_message(self, format: str, *args: object) -> None:
        return

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0"))
        raw_request = self.rfile.read(length)
        try:
            request_body = json.loads(raw_request)
        except json.JSONDecodeError:
            self.send_error(400, "Request body must be JSON")
            return
        if request_body.get("stream"):
            self.send_error(400, "Streaming is disabled so responses remain auditable")
            return
        base = os.environ["UPSTREAM_BASE_URL"].rstrip("/")
        path = self.path
        if base.endswith("/v1") and path.startswith("/v1/"):
            path = path[3:]
        upstream = base + path
        key = os.environ["UPSTREAM_API_KEY"]
        attempts = int(os.getenv("PROXY_RETRY_ATTEMPTS", "4"))
        started = time.monotonic()
        wait_seconds = 0.0
        response_bytes = b""
        status = 599
        response_body: dict[str, Any] = {}
        error = None
        for attempt in range(attempts):
            outbound = urllib.request.Request(
                upstream,
                data=raw_request,
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                method="POST",
            )
            try:
                with urllib.request.urlopen(outbound, timeout=float(os.getenv("PROXY_REQUEST_TIMEOUT", "600"))) as response:
                    status = response.status
                    response_bytes = response.read()
                response_body = json.loads(response_bytes)
                break
            except urllib.error.HTTPError as exc:
                status = exc.code
                response_bytes = exc.read()
                try:
                    response_body = json.loads(response_bytes)
                except json.JSONDecodeError:
                    response_body = {"error": {"message": response_bytes.decode(errors="replace")}}
                if status not in {429, 500, 502, 503, 504} or attempt + 1 == attempts:
                    break
                delay = min(60.0, 2.0**attempt)
                wait_seconds += delay
                time.sleep(delay)
            except (TimeoutError, urllib.error.URLError) as exc:
                error = str(exc)
                if attempt + 1 == attempts:
                    response_body = {"error": {"message": error}}
                    response_bytes = json.dumps(response_body).encode()
                    break
                delay = min(60.0, 2.0**attempt)
                wait_seconds += delay
                time.sleep(delay)
        tokens_in, tokens_out = usage(response_body)
        record = {
            "run_id": os.environ["RUN_ID"],
            "timestamp": time.time(),
            "backbone": os.environ["BACKBONE"],
            "model_requested": request_body.get("model"),
            "model_returned": response_body.get("model"),
            "request": request_body,
            "response": response_body,
            "tokens_in": tokens_in,
            "tokens_out": tokens_out,
            "latency_s": time.monotonic() - started,
            "http_status": status,
            "ratelimit_wait_s": wait_seconds,
            "error": error,
        }
        append_jsonl(Path(os.environ["LLM_LOG_PATH"]), record)
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)


def serve(host: str, port: int) -> None:
    required = ["UPSTREAM_BASE_URL", "UPSTREAM_API_KEY", "RUN_ID", "BACKBONE", "LLM_LOG_PATH"]
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        raise RuntimeError("Missing proxy environment variables: " + ", ".join(missing))
    ThreadingHTTPServer((host, port), ProxyHandler).serve_forever()
