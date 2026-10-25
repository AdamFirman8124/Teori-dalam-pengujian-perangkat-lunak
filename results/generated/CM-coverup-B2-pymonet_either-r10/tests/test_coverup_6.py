# file: project/pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.maybe import Maybe


def test_left_to_maybe_returns_nothing():
    """Left.to_maybe must return an empty Maybe (Nothing)."""
    left = Left('error value')

    result = left.to_maybe()

    assert isinstance(result, Maybe)
    assert result == Maybe.nothing()
    assert getattr(result, 'is_nothing', True) is True


def test_left_to_maybe_discards_wrapped_value():
    """The payload wrapped in Left must not leak into the resulting Maybe."""
    left = Left(42)

    result = left.to_maybe()

    assert result == Maybe.nothing()
    assert getattr(result, 'value', None) is None


def test_left_to_maybe_is_repeatable_and_side_effect_free():
    """Repeated calls yield equivalent empty Maybes and leave Left unchanged."""
    left = Left('boom')

    first = left.to_maybe()
    second = left.to_maybe()

    assert first == Maybe.nothing()
    assert second == Maybe.nothing()
    assert first == second
    # The Left instance itself is untouched.
    assert isinstance(left, Left)
    assert left.is_left() is True
    assert left.is_right() is False
