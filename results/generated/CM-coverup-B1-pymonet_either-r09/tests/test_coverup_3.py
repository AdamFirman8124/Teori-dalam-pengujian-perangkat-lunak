# file: project/pymonet/either.py:48-57
# asked: {"lines": [55, 57], "branches": []}
# gained: {"lines": [55, 57], "branches": []}

from pymonet.either import Either
from pymonet.box import Box


def test_either_to_box_returns_box():
    either = Either(42)
    result = either.to_box()
    assert isinstance(result, Box)
    assert result.value == 42


def test_either_to_box_preserves_value_and_does_not_mutate():
    either = Either("hello")
    result = either.to_box()
    assert isinstance(result, Box)
    assert result.value == "hello"
    assert either.value == "hello"


def test_either_to_box_with_none_value():
    either = Either(None)
    result = either.to_box()
    assert isinstance(result, Box)
    assert result.value is None
