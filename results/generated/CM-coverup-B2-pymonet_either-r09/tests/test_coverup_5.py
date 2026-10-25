# file: project/pymonet/either.py:70-79
# asked: {"lines": [77, 79], "branches": []}
# gained: {"lines": [77, 79], "branches": []}

from pymonet.either import Either
from pymonet.lazy import Lazy


def test_either_to_lazy_returns_lazy_not_evaluated():
    either = Either(42)
    lazy = either.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.is_evaluated is False
    assert callable(lazy.constructor_fn)


def test_either_to_lazy_preserves_value():
    either = Either("hello")
    lazy = either.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.get() == "hello"
    assert lazy.is_evaluated is True
    assert lazy.value == "hello"


def test_either_to_lazy_is_lazy_references_current_value(monkeypatch):
    either = Either(1)
    lazy = either.to_lazy()
    assert isinstance(lazy, Lazy)
    assert lazy.is_evaluated is False
    monkeypatch.setattr(either, "value", 2)
    assert lazy.get() == 2
    assert lazy.value == 2
