# file: project/pymonet/either.py:70-79
# asked: {"lines": [77, 79], "branches": []}
# gained: {"lines": [77, 79], "branches": []}

import pytest

from pymonet.either import Either, Left, Right
from pymonet.lazy import Lazy


def test_either_to_lazy_returns_lazy_wrapping_value():
    """Either.to_lazy should return a Lazy instance whose constructor
    returns the original value when evaluated."""
    either = Either(42)

    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.is_evaluated is False
    assert lazy.get() == 42


def test_left_to_lazy_returns_lazy_wrapping_value():
    """Left.to_lazy should wrap the Left value in a Lazy."""
    left = Left("error")

    lazy = left.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == "error"


def test_right_to_lazy_returns_lazy_wrapping_value():
    """Right.to_lazy should wrap the Right value in a Lazy."""
    right = Right("success")

    lazy = right.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.get() == "success"


def test_to_lazy_is_pure_and_does_not_mutate_either(monkeypatch):
    """to_lazy must not mutate the Either instance; the Lazy constructor
    should only be invoked via Lazy(), which we spy on with monkeypatch."""
    either = Either(None)
    calls = []
    original_init = Lazy.__init__

    def spy_init(self, constructor_fn):
        calls.append(constructor_fn)
        original_init(self, constructor_fn)

    monkeypatch.setattr(Lazy, "__init__", spy_init)

    lazy = either.to_lazy()

    assert len(calls) == 1
    assert lazy.get() is None
    assert either.value is None
