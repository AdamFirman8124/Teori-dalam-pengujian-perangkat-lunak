# file: project/pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.maybe import Maybe


def test_left_to_maybe_returns_maybe():
    """Left.to_maybe must return an instance of Maybe."""
    left = Left("error value")

    result = left.to_maybe()

    assert isinstance(result, Maybe)


def test_left_to_maybe_returns_empty_maybe():
    """Left.to_maybe must return the empty Maybe (same type as
    Maybe.nothing()), not a populated one."""
    left = Left(42)

    result = left.to_maybe()
    empty = Maybe.nothing()

    # The result must be of the same concrete type as the empty Maybe
    # (i.e. the Nothing variant, not the Just/Box variant).
    assert type(result) is type(empty)


def test_left_to_maybe_is_repeatable_and_side_effect_free():
    """Calling to_maybe repeatedly yields empty Maybes and leaves the
    Left instance unchanged."""
    left = Left("boom")

    first = left.to_maybe()
    second = left.to_maybe()

    assert type(first) is type(second)
    assert type(first) is type(Maybe.nothing())
    # The Left itself is untouched (still a Left, same payload).
    assert isinstance(left, Left)
    assert left.is_left() is True
    assert left.is_right() is False
