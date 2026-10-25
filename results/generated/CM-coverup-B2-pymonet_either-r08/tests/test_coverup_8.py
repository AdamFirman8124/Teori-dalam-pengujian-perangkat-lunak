# file: project/pymonet/either.py:189-198
# asked: {"lines": [196, 198], "branches": []}
# gained: {"lines": [196, 198], "branches": []}

from pymonet.either import Right
from pymonet.maybe import Maybe


def test_right_to_maybe_returns_just_with_value():
    right = Right(42)

    result = right.to_maybe()

    assert isinstance(result, Maybe)
    assert result == Maybe.just(42)
    assert result.value == 42


def test_right_to_maybe_matches_maybe_just_directly():
    value = {"key": "data"}
    right = Right(value)

    result = right.to_maybe()

    assert result == Maybe.just(value)
    assert result.value == value
    assert result.value is value


def test_right_to_maybe_with_none_value():
    right = Right(None)

    result = right.to_maybe()

    assert isinstance(result, Maybe)
    assert result == Maybe.just(None)
    assert result.value is None
