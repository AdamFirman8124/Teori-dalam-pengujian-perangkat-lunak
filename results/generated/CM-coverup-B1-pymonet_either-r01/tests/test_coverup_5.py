# file: project/pymonet/either.py:70-79
# asked: {"lines": [77, 79], "branches": []}
# gained: {"lines": [77, 79], "branches": []}

from pymonet.either import Either, Left, Right
from pymonet.lazy import Lazy


def test_either_to_lazy_returns_lazy_with_value():
    either = Either(42)
    result = either.to_lazy()
    assert isinstance(result, Lazy)
    assert result.is_evaluated is False
    assert result.constructor_fn() == 42
    assert result.get() == 42


def test_right_to_lazy_returns_lazy_with_value():
    either = Right(10)
    result = either.to_lazy()
    assert isinstance(result, Lazy)
    assert result.constructor_fn() == 10
    assert result.get() == 10


def test_left_to_lazy_returns_lazy_with_value():
    either = Left("error")
    result = either.to_lazy()
    assert isinstance(result, Lazy)
    assert result.constructor_fn() == "error"
    assert result.get() == "error"
