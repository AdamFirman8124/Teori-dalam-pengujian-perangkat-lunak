# file: project/pymonet/either.py:106-111
# asked: {"lines": [111], "branches": []}
# gained: {"lines": [111], "branches": []}

import pytest

from pymonet.either import Left, Right


def test_left_ap_returns_copy_of_self():
    """Left.ap must return a new Left wrapping the same value (line 111)."""
    left = Left("error value")
    other = Right(lambda x: x + 1)

    result = left.ap(other)

    assert isinstance(result, Left)
    assert result is not left
    assert result.value == "error value"
    assert left.value == "error value"  # original unchanged


def test_left_ap_ignores_monad_argument():
    """Left.ap ignores the monad argument entirely."""
    sentinel = object()
    result = Left(42).ap(sentinel)

    assert isinstance(result, Left)
    assert result.value == 42


def test_left_ap_with_left_monad():
    result = Left("err").ap(Left("other"))

    assert isinstance(result, Left)
    assert result.value == "err"
