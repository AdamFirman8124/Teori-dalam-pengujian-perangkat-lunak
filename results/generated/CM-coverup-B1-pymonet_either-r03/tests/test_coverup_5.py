# file: project/pymonet/either.py:70-79
# asked: {"lines": [77, 79], "branches": []}
# gained: {"lines": [77, 79], "branches": []}

import pytest

from pymonet.either import Left, Right


def test_left_to_lazy_returns_lazy_with_value():
    """Either.to_lazy on Left should return a Lazy wrapping the Left value."""
    from pymonet.lazy import Lazy

    either = Left(42)
    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.is_evaluated is False
    assert lazy.get() == 42


def test_right_to_lazy_returns_lazy_with_value():
    """Either.to_lazy on Right should return a Lazy wrapping the Right value."""
    from pymonet.lazy import Lazy

    either = Right("hello")
    lazy = either.to_lazy()

    assert isinstance(lazy, Lazy)
    assert lazy.is_evaluated is False
    assert lazy.get() == "hello"


def test_to_lazy_is_actually_lazy(monkeypatch):
    """The returned Lazy must not evaluate the value until fold/get is called."""
    from pymonet import lazy as lazy_module

    called = []

    class TrackingEither(Left):
        @property
        def value(self):
            called.append("accessed")
            return super().value

    # Left stores value as attribute; build instance manually to keep control
    either = Left.__new__(Left)
    object.__setattr__(either, "value", 7)

    lazy = either.to_lazy()
    assert called == []
    assert lazy.is_evaluated is False

    result = lazy.get()
    assert result == 7
    assert lazy.is_evaluated is True
