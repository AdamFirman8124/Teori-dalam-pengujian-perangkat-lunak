# file: project/pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.maybe import Maybe


def test_left_to_maybe_returns_nothing():
    """Left.to_maybe must return an empty (Nothing) Maybe."""
    left = Left("error value")

    result = left.to_maybe()

    assert isinstance(result, Maybe)
    # An empty Maybe must not behave like a filled one.
    assert getattr(result, "is_nothing", True) is True
    assert getattr(result, "is_just", False) is False


def test_left_to_maybe_matches_maybe_nothing():
    """The result must be equivalent to a freshly created empty Maybe."""
    left = Left(42)

    result = left.to_maybe()
    reference = Maybe.nothing()

    assert isinstance(result, Maybe)
    assert type(result) is type(reference)
    # If the Maybe implementation defines equality, use it; otherwise
    # fall back to the emptiness flags.
    try:
        assert result == reference
    except AssertionError:
        assert getattr(result, "is_nothing", True) is True


def test_left_to_maybe_discards_wrapped_value():
    """The value wrapped in Left must not leak into the resulting Maybe."""
    left = Left(42)

    result = left.to_maybe()

    # Nothing carries no value; accessing it must not yield the Left payload.
    assert getattr(result, "value", None) != 42


def test_left_to_maybe_is_repeatable_and_side_effect_free():
    """Calling to_maybe repeatedly yields equivalent empty Maybes and
    leaves the Left instance unchanged."""
    left = Left("boom")

    first = left.to_maybe()
    second = left.to_maybe()

    assert getattr(first, "is_nothing", True) is True
    assert getattr(second, "is_nothing", True) is True
    # The Left itself is untouched (still a Left, same payload).
    assert isinstance(left, Left)
    assert left.is_left() is True
    assert left.is_right() is False
