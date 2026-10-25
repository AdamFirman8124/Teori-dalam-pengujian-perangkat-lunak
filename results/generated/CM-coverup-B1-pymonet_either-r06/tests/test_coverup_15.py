# file: project/pymonet/either.py:106-111
# asked: {"lines": [111], "branches": []}
# gained: {"lines": [111], "branches": []}

import pytest

from pymonet.either import Left, Right


def test_left_ap_returns_copy_of_self():
    """Left.ap should ignore the passed monad and return a new Left
    wrapping the same value (covers line 111: return Left(self.value))."""
    left = Left("error")

    result = left.ap(Right(lambda x: x + 1))

    assert isinstance(result, Left)
    assert result is not left          # a copy, not the same object
    assert result.value == "error"     # same value as the original


def test_left_ap_ignores_argument_value():
    """Left.ap must not use the argument's value in any way."""
    left = Left(42)

    result = left.ap(Left("other"))

    assert isinstance(result, Left)
    assert result.value == 42
