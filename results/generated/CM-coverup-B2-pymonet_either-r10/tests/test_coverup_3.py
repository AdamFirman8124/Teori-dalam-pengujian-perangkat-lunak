# file: project/pymonet/either.py:48-57
# asked: {"lines": [55, 57], "branches": []}
# gained: {"lines": [55, 57], "branches": []}

from pymonet.box import Box
from pymonet.either import Left, Right


def test_left_to_box_preserves_value():
    value = object()
    result = Left(value).to_box()

    assert isinstance(result, Box)
    assert result.value is value


def test_right_to_box_preserves_value():
    value = object()
    result = Right(value).to_box()

    assert isinstance(result, Box)
    assert result.value is value
