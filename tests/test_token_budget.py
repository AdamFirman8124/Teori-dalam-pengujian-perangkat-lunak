"""The token-budget guard must stop a run before the quota is exhausted."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import token_budget as tb  # noqa: E402


def test_unconfigured_budget_is_none(monkeypatch):
    monkeypatch.delenv("LLM_TOKEN_BUDGET_TOTAL", raising=False)
    assert tb.current_budget() is None
    assert tb.check_budget() is None


def test_budget_arithmetic(monkeypatch):
    monkeypatch.setenv("LLM_TOKEN_BUDGET_TOTAL", "50_000_000")
    monkeypatch.setenv("LLM_TOKEN_BUDGET_USED", "46_519_404")
    monkeypatch.setenv("LLM_TOKEN_RESERVE", "200_000")
    b = tb.current_budget()
    assert b.total == 50_000_000
    assert b.used == 46_519_404
    assert b.reserve == 200_000
    assert b.remaining == 3_480_596
    assert b.usable == 3_280_596


def test_guard_passes_when_plenty_left(monkeypatch):
    monkeypatch.setenv("LLM_TOKEN_BUDGET_TOTAL", "50_000_000")
    monkeypatch.setenv("LLM_TOKEN_BUDGET_USED", "1_000_000")
    monkeypatch.delenv("LLM_TOKEN_RESERVE", raising=False)
    assert tb.check_budget(context="x") is not None


def test_guard_does_not_stop_early_with_default_reserve(monkeypatch):
    """With reserve 0 the run continues while any token is left (7% here)."""
    monkeypatch.setenv("LLM_TOKEN_BUDGET_TOTAL", "50_000_000")
    monkeypatch.setenv("LLM_TOKEN_BUDGET_USED", "46_519_404")
    monkeypatch.delenv("LLM_TOKEN_RESERVE", raising=False)
    assert tb.check_budget() is not None


def test_guard_raises_at_cap(monkeypatch):
    monkeypatch.setenv("LLM_TOKEN_BUDGET_TOTAL", "50_000_000")
    monkeypatch.setenv("LLM_TOKEN_BUDGET_USED", "50_000_000")
    monkeypatch.delenv("LLM_TOKEN_RESERVE", raising=False)
    with pytest.raises(tb.TokenBudgetExhausted) as excinfo:
        tb.check_budget(context="CoverUp:gpt-5.5 HumanEval 7")
    assert "CoverUp:gpt-5.5 HumanEval 7" in str(excinfo.value)
    assert "dihentikan" in str(excinfo.value)


def test_guard_raises_when_reserve_set(monkeypatch):
    monkeypatch.setenv("LLM_TOKEN_BUDGET_TOTAL", "50_000_000")
    # current real state: 7% left, only 3.48M tokens remaining
    monkeypatch.setenv("LLM_TOKEN_BUDGET_USED", "46_519_404")
    monkeypatch.setenv("LLM_TOKEN_RESERVE", "4_000_000")
    with pytest.raises(tb.TokenBudgetExhausted):
        tb.check_budget()

