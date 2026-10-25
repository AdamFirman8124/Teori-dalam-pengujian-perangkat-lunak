# file: project/pymonet/either.py:189-198
# asked: {"lines": [196, 198], "branches": []}
# gained: {"lines": [196, 198], "branches": []}

from pymonet.either import Right
from pymonet.maybe import Maybe


def test_right_to_maybe_returns_just_with_same_value():
    right = Right(42)
    result = right.to_maybe()
    assert isinstance(result, Maybe)
    assert result == Maybe.just(42)
    assert result.value == 42
    # original Either is unchanged
    assert right.value == 42


def test_right_to_maybe_with_string_value():
    right = Right("success")
    result = right.to_maybe()
    assert result == Maybe.just("success")
    assert result.value == "success"
