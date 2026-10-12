"""Regression tests for CoverUp transport-error retry (coverup/src/coverup/llm.py).

Root cause of the observed ``BLOCKED: CoverUp ... InternalServerError ...
Connection error ... giving up``: an OpenAI-compatible router wrapped a
transient connection reset as ``litellm.InternalServerError`` / 5xx.  That class
is a subclass of ``openai.APIError`` but was *not* handled, so it fell through
to the generic APIError branch which returned ``None`` immediately.
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "coverup" / "src"))
sys.path.insert(0, str(ROOT / "src"))


def _chatter(monkeypatch, max_retries=4):
    import openai  # noqa: F401
    import litellm  # noqa: F401
    from coverup.llm import Chatter

    monkeypatch.setattr(asyncio, "sleep", _no_sleep)
    # Avoid a real rate-limiter / network dependency.
    c = Chatter.__new__(Chatter)
    c._model = "openai/claude-sonnet-5"
    c._model_temperature = None
    c._max_backoff = 64
    c._max_connection_retries = max_retries
    c.token_rate_limit = None
    c._add_cost = lambda cost: None
    c._log_msg = lambda ctx, msg: None
    c._log_json = lambda ctx, j: None
    c._signal_retry = lambda: None
    c._functions = {}
    c._max_func_calls_per_chat = 50
    c._extra_request_pars = None
    return c


async def _no_sleep(_seconds):
    return None


def _run(coro):
    return asyncio.run(coro)


def test_internal_server_error_is_retried_then_succeeds(monkeypatch):
    import litellm

    chatter = _chatter(monkeypatch)
    calls = {"n": 0}
    sentinel = object()

    async def fake_acreate(**request):
        calls["n"] += 1
        if calls["n"] < 3:
            raise litellm.exceptions.InternalServerError(
                message="OpenAIException - Connection error.",
                model="claude-sonnet-5",
                llm_provider="openai",
            )
        return sentinel

    monkeypatch.setattr(litellm, "acreate", fake_acreate)
    result = _run(chatter._send_request({"model": chatter._model,
                                         "messages": []}, ctx=None))
    assert result is sentinel
    assert calls["n"] == 3


def test_transport_retries_are_bounded(monkeypatch):
    import litellm

    chatter = _chatter(monkeypatch, max_retries=2)
    calls = {"n": 0}

    async def always_fail(**request):
        calls["n"] += 1
        raise litellm.exceptions.InternalServerError(
            message="Connection error.",
            model="claude-sonnet-5",
            llm_provider="openai",
        )

    monkeypatch.setattr(litellm, "acreate", always_fail)
    result = _run(chatter._send_request({"model": chatter._model,
                                         "messages": []}, ctx=None))
    assert result is None
    # initial attempt + max_retries retries, then give up
    assert calls["n"] == 3


def test_quota_exhaustion_is_not_retried(monkeypatch):
    import openai

    chatter = _chatter(monkeypatch)
    calls = {"n": 0}

    async def quota_fail(**request):
        calls["n"] += 1
        raise openai.RateLimitError(
            message="You exceeded your current quota, please check your plan",
            response=_fake_response(429),
            body=None,
        )

    import litellm
    monkeypatch.setattr(litellm, "acreate", quota_fail)
    with pytest.raises(openai.RateLimitError):
        _run(chatter._send_request({"model": chatter._model,
                                    "messages": []}, ctx=None))
    assert calls["n"] == 1


def _fake_response(status_code):
    import httpx
    return httpx.Response(status_code=status_code, request=httpx.Request("POST", "https://x"))
