# file: project/pymonet/either.py:70-79
# asked: {"lines": [77, 79], "branches": []}
# gained: {"lines": [77, 79], "branches": []}

from pymonet.either import Either
from pymonet.lazy import Lazy


def test_either_to_lazy_returns_lazy_instance():
    either = Either(42)
    result = either.to_lazy()
    assert isinstance(result, Lazy)


def test_either_to_lazy_preserves_value():
    either = Either("hello")
    lazy = either.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.is_evaluated is False
    assert lazy.get() == "hello"
    assert lazy.is_evaluated is True


def test_either_to_lazy_defers_evaluation_until_get(monkeypatch):
    either = Either(1)
    lazy = either.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.is_evaluated is False
    monkeypatch.setattr(either, "value", 2)
    assert lazy.get() == 2
    # Lazy memoizes: further changes to Either do not change evaluated value
    monkeypatch.setattr(either, "value", 3)
    assert lazy.get() == 2
