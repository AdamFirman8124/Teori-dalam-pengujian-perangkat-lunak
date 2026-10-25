# file: project/pymonet/either.py:48-57
# asked: {"lines": [55, 57], "branches": []}
# gained: {"lines": [55, 57], "branches": []}

from pymonet.box import Box
from pymonet.either import Right


def test_either_to_box_preserves_value():
    value = object()

    result = Right(value).to_box()

    assert isinstance(result, Box)
    assert result.value is value
