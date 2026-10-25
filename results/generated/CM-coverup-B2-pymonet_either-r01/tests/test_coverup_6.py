# file: project/pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.maybe import Maybe


def test_left_to_maybe_returns_nothing():
    """Left.to_maybe must return a Maybe of the same (empty) subclass
    as Maybe.nothing() — i.e. not the 'just' subclass."""
    left = Left("error value")

    result = left.to_maybe()

    assert isinstance(result, Maybe)
    assert type(result) is type(Maybe.nothing())


def test_left_to_maybe_discards_wrapped_value():
    """The value wrapped in Left must not leak into the resulting Maybe."""
    left = Left(42)

    result = left.to_maybe()

    assert type(result) is type(Maybe.nothing())
    # Nothing carries no payload; whatever value attribute exists must
    # not be the Left payload.
    assert getattr(result, "value", None) != 42


def test_left_to_maybe_is_repeatable_and_side_effect_free():
    """Calling to_maybe repeatedly yields equivalent empty Maybes and
    leaves the Left instance unchanged."""
    left = Left("boom")

    first = left.to_maybe()
    second = left.to_maybe()

    assert type(first) is type(Maybe.nothing())
    assert type(second) is type(Maybe.nothing())
    # The Left itself is untouched (still a Left, same payload).
    assert isinstance(left, Left)
    assert left.is_left() is True
    assert left.is_right() is False
