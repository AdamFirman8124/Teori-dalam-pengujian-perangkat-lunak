"""Stop the experiment before the LLM token budget is exhausted.

The provider reports a quota (used/total tokens).  When the remaining budget
drops below a safety margin the run must *pause* cleanly instead of burning the
last tokens on calls that will fail, so a long run can be resumed once the quota
is topped up.

Configuration (all optional):

    LLM_TOKEN_BUDGET_TOTAL   total quota reported by the provider
    LLM_TOKEN_BUDGET_USED    tokens already consumed
    LLM_TOKEN_RESERVE        keep this many tokens in reserve (default 200_000)
    LLM_TOKEN_STOP_FILE      if set, a "pause" marker file so the user can resume

The guard is intentionally side-effect free: it raises :class:`TokenBudgetExhausted`
and callers decide how to stop.
"""
from __future__ import annotations

import os
from dataclasses import dataclass

DEFAULT_RESERVE = 0


class TokenBudgetExhausted(RuntimeError):
    """Raised when the remaining token budget is at or below the reserve."""


@dataclass(frozen=True)
class Budget:
    total: int
    used: int
    reserve: int

    @property
    def remaining(self) -> int:
        return max(0, self.total - self.used)

    @property
    def usable(self) -> int:
        return max(0, self.total - self.used - self.reserve)

    @property
    def pct_remaining(self) -> float:
        return 100.0 * self.remaining / self.total if self.total else 0.0


def _as_int(value: str | None, default: int) -> int:
    try:
        return int(str(value).replace("_", "").replace(",", "").strip())
    except (TypeError, ValueError):
        return default


def current_budget() -> Budget | None:
    """Read the budget from the environment, or ``None`` when unconfigured."""
    total = _as_int(os.environ.get("LLM_TOKEN_BUDGET_TOTAL"), 0)
    if total <= 0:
        return None
    used = _as_int(os.environ.get("LLM_TOKEN_BUDGET_USED"), 0)
    reserve = _as_int(os.environ.get("LLM_TOKEN_RESERVE"), DEFAULT_RESERVE)
    return Budget(total=total, used=used, reserve=reserve)


def check_budget(*, context: str = "") -> Budget | None:
    """Raise :class:`TokenBudgetExhausted` once the token cap is reached.

    With the default reserve of 0 the run stops exactly at the cap (e.g. 50M).
    The provider also reports an exhausted quota, but stopping here keeps the
    checkpoint clean so the run can resume instead of failing mid-task.
    """
    budget = current_budget()
    if budget is None:
        return None
    if budget.remaining <= budget.reserve:
        where = f" ({context})" if context else ""
        detail = (f"reserve {budget.reserve:,}" if budget.reserve
                  else "batas token tercapai")
        raise TokenBudgetExhausted(
            "Token budget habis{0}: sisa {1:,} dari {2:,} token "
            "({3:.1f}%), {4}. Eksperimen dihentikan; isi ulang kuota "
            "lalu set LLM_TOKEN_BUDGET_USED ke nilai baru dan lanjutkan "
            "(run akan resume dari checkpoint).".format(
                where, budget.remaining, budget.total,
                budget.pct_remaining, detail,
            )
        )
    return budget
