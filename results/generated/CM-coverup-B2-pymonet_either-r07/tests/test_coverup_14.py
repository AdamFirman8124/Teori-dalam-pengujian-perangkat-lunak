# file: project/pymonet/either.py:97-104
# asked: {"lines": [104], "branches": []}
# gained: {"lines": [104], "branches": []}

import pytest

from pymonet.either import Left, Right


def test_left_bind_returns_self_and_executes_line_104():
    """Left.bind must return the very same Left instance (line 104: `return self`)."""
    left = Left("error value")

    result = left.bind(lambda value: value + 1)

    # Postcondition: bind returns the identical instance, untouched.
    assert result is left
    assert result.value == "error value"
    assert result.is_left() is True
    assert result.is_right() is False


def test_left_bind_ignores_mapper_side_effects():
    """The mapper passed to Left.bind is never invoked."""
    left = Left(42)
    calls = []

    def mapper(value):
        calls.append(value)
        return value * 2

    result = left.bind(mapper)

    assert calls == []  # mapper was never called
    assert result is left
    assert result.value == 42


def test_left_bind_with_none_mapper():
    """Left.bind accepts any argument (even None) and still returns self."""
    left = Left("oops")

    result = left.bind(None)

    assert result is left
    assert result.value == "oops"


def test_left_bind_contrast_with_right_bind():
    """Sanity check: Right.bind does apply the mapper, Left.bind does not."""
    right = Right(10)

    assert right.bind(lambda value: value + 1) == 11

    left = Left(10)
    assert left.bind(lambda value: value + 1) is left
