# file: project/pymonet/either.py:189-198
# asked: {"lines": [196, 198], "branches": []}
# gained: {"lines": [196, 198], "branches": []}

from pymonet.either import Right
from pymonet.maybe import Maybe


def test_right_to_maybe_returns_just_with_value():
    right = Right(42)
    result = right.to_maybe()
    assert isinstance(result, Maybe)
    assert result.value == 42
    assert right.value == 42


def test_right_to_maybe_preserves_various_values():
    for value in ["hello", None, [1, 2], {"a": 1}]:
        right = Right(value)
        result = right.to_maybe()
        assert isinstance(result, Maybe)
        assert result.value == value
        assert result.value is value
