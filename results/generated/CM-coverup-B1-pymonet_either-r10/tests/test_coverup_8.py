# file: project/pymonet/either.py:189-198
# asked: {"lines": [196, 198], "branches": []}
# gained: {"lines": [196, 198], "branches": []}

from pymonet.either import Right
from pymonet.maybe import Maybe


def test_right_to_maybe_returns_just_with_value():
    either = Right(42)

    result = either.to_maybe()

    assert isinstance(result, Maybe)
    assert result.is_nothing is False
    assert result.value == 42
    assert result == Maybe.just(42)


def test_right_to_maybe_preserves_none_value():
    either = Right(None)

    result = either.to_maybe()

    assert isinstance(result, Maybe)
    assert result.is_nothing is False
    assert result.value is None
    assert result == Maybe.just(None)


def test_right_to_maybe_does_not_mutate_either():
    either = Right('value')

    result = either.to_maybe()

    assert either.value == 'value'
    assert either.is_right() is True
    assert result.value == 'value'
    assert result.is_nothing is False
