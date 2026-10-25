# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

import pytest

from pymonet.either import Left, Right


def test_either_ap_executes_line_46():
    """Either.ap must call applicative.map(self.value) and return the mapped Either."""
    add_one = lambda x: x + 1
    either_fn = Right(add_one)
    either_value = Right(1)

    result = either_fn.ap(either_value)

    assert isinstance(result, Right)
    assert result.value == 2


def test_either_ap_with_left_applicative_returns_left():
    """ap on a Right with a Left applicative delegates to Left.map, which ignores the mapper."""
    either_fn = Right(lambda x: x + 1)
    left_value = Left("error")

    result = either_fn.ap(left_value)

    assert isinstance(result, Left)
    assert result.value == "error"
