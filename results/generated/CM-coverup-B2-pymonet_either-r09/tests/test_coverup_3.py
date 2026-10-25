# file: project/pymonet/either.py:48-57
# asked: {"lines": [55, 57], "branches": []}
# gained: {"lines": [55, 57], "branches": []}

from pymonet.box import Box
from pymonet.either import Either, Left, Right


def test_either_to_box():
    either = Either(42)
    result = either.to_box()
    assert isinstance(result, Box)
    assert result.value == 42
    assert result == Box(42)


def test_left_to_box():
    left = Left(10)
    result = left.to_box()
    assert isinstance(result, Box)
    assert result.value == 10
    assert result == Box(10)


def test_right_to_box():
    right = Right(20)
    result = right.to_box()
    assert isinstance(result, Box)
    assert result.value == 20
    assert result == Box(20)
