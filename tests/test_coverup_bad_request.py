"""BadRequestError must be split into permanent vs transient (upstream 400).

Observed failure:

    Error: <class 'litellm.exceptions.BadRequestError'>
           litellm.BadRequestError: OpenAIException -
           The upstream service could not complete the request.
    ---- giving up

The OctaLabs gateway returns HTTP 400 with "upstream service could not complete
the request" for a *transient* hiccup.  The old handler treated every
BadRequestError as fatal ("maximum context length") and gave up immediately,
marking the task BLOCKED even though the model was fine.
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "coverup" / "src"))
sys.path.insert(0, str(ROOT / "src"))

import httpx  # noqa: E402
import openai  # noqa: E402
import litellm  # noqa: E402


async def _no_sleep(_seconds):
    return None


def _chatter(monkeypatch, max_retries=4):
    from coverup.llm import Chatter

    monkeypatch.setattr(asyncio, "sleep", _no_sleep)
    c = Chatter.__new__(Chatter)
    c._model = "openai/claude-sonnet-5"
    c._model_temperature = None
    c._max_backoff = 64
    c._max_connection_retries = max_retries
    c.token_rate_limit = None
    c._add_cost = lambda cost: None
    c._add_usage = lambda pt, ct, tt: None
    c._log_msg = lambda ctx, msg: None
    c._log_json = lambda ctx, j: None
    c._signal_retry = lambda: None
    c._functions = {}
    c._max_func_calls_per_chat = 50
    c._extra_request_pars = None
    return c


def _bad_request(msg):
    request = httpx.Request("POST", "https://router.octalabs.id/v1/chat/completions")
    response = httpx.Response(status_code=400, request=request)
    return openai.BadRequestError(message=msg, response=response, body=None)


def _run(coro):
    return asyncio.new_event_loop().run_until_complete(coro)


def test_upstream_400_is_retried_then_recovers(monkeypatch):
    c = _chatter(monkeypatch, max_retries=4)
    calls = {"n": 0}

    async def fake_acreate(**kwargs):
        calls["n"] += 1
        if calls["n"] == 1:
            raise _bad_request("The upstream service could not complete the request.")
        return "OK"

    monkeypatch.setattr(litellm, "acreate", fake_acreate)
    result = _run(c._send_request({"messages": []}, object()))
    assert result == "OK"
    assert calls["n"] == 2  # retried once, then succeeded


def test_upstream_400_gives_up_after_max_retries(monkeypatch):
    c = _chatter(monkeypatch, max_retries=2)
    calls = {"n": 0}

    async def fake_acreate(**kwargs):
        calls["n"] += 1
        raise _bad_request("The upstream service could not complete the request.")

    monkeypatch.setattr(litellm, "acreate", fake_acreate)
    result = _run(c._send_request({"messages": []}, object()))
    assert result is None
    assert calls["n"] == 3  # initial + 2 retries, then gives up


def test_context_length_400_is_permanent(monkeypatch):
    c = _chatter(monkeypatch, max_retries=4)
    calls = {"n": 0}

    async def fake_acreate(**kwargs):
        calls["n"] += 1
        raise _bad_request("This model's maximum context length is 8192 tokens.")

    monkeypatch.setattr(litellm, "acreate", fake_acreate)
    result = _run(c._send_request({"messages": []}, object()))
    assert result is None
    assert calls["n"] == 1  # fail fast, no retry
