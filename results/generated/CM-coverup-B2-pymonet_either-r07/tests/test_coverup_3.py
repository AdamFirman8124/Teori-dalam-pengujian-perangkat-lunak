# file: project/pymonet/either.py:48-57
# asked: {"lines": [55, 57], "branches": []}
# gained: {"lines": [55, 57], "branches": []}

import pytest

from pymonet.either import Left, Right
from pymonet.box import Box


@pytest.mark.parametrize("either", [Left("error-value"), Right(42)])
def test_to_box_wraps_value_in_box(either):
    """Either.to_box should return a Box containing the Either's value."""
    result = either.to_box()

    assert isinstance(result, Box)
    assert result.value == either.value


def test_to_box_on_left():
    """Left.to_box should wrap the error value in a Box."""
    left = Left("error")
    result = left.to_box()

    assert isinstance(result, Box)
    assert result.value == "error"


def test_to_box_on_right():
    """Right.to_box should wrap the success value in a Box."""
    right = Right(42)
    result = right.to_box()

    assert isinstance(result, Box)
    assert result.value == 42
