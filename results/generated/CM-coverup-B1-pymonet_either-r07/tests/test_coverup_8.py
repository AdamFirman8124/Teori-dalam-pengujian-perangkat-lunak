# file: project/pymonet/either.py:189-198
# asked: {"lines": [196, 198], "branches": []}
# gained: {"lines": [196, 198], "branches": []}

from pymonet.either import Right
from pymonet.maybe import Maybe


def test_right_to_maybe_returns_just_with_int():
    right = Right(42)
    result = right.to_maybe()
    assert isinstance(result, Maybe)
    assert result == Maybe.just(42)
    assert result.is_nothing is False
    assert result.value == 42
    # original Either unchanged
    assert right.value == 42


def test_right_to_maybe_returns_just_with_string():
    right = Right("hello")
    result = right.to_maybe()
    assert result == Maybe.just("hello")
    assert result.is_nothing is False
    assert result.value == "hello"
    assert result.get_or_else("default") == "hello"


def test_right_to_maybe_preserves_object_identity():
    value = {"key": "value"}
    right = Right(value)
    result = right.to_maybe()
    assert result == Maybe.just(value)
    assert result.value is value
    assert right.value is value
