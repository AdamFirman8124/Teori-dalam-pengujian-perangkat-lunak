# file: project/pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.maybe import Maybe


def _flag(obj, name):
    """Read a boolean-ish attribute that may be a property or a method."""
    attr = getattr(obj, name)
    return attr() if callable(attr) else attr


def test_left_to_maybe_returns_nothing():
    """Left.to_maybe must return an empty (Nothing) Maybe."""
    left = Left('error value')

    result = left.to_maybe()

    assert isinstance(result, Maybe)
    assert _flag(result, 'is_nothing') is True


def test_left_to_maybe_discards_wrapped_value():
    """The value wrapped in Left must not leak into the resulting Maybe."""
    left = Left(42)

    result = left.to_maybe()

    assert isinstance(result, Maybe)
    assert _flag(result, 'is_nothing') is True
    assert getattr(result, 'value', None) is None


def test_left_to_maybe_is_repeatable_and_side_effect_free():
    """Repeated calls yield empty Maybes and leave the Left unchanged."""
    left = Left('boom')

    first = left.to_maybe()
    second = left.to_maybe()

    assert isinstance(first, Maybe)
    assert isinstance(second, Maybe)
    assert _flag(first, 'is_nothing') is True
    assert _flag(second, 'is_nothing') is True
    # The Left itself is untouched (still a Left, same payload).
    assert isinstance(left, Left)
    assert left.is_left() is True
    assert left.is_right() is False
    assert left.value == 'boom'
