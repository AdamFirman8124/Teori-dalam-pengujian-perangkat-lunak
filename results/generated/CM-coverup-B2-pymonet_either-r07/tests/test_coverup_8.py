# file: project/pymonet/either.py:189-198
# asked: {"lines": [196, 198], "branches": []}
# gained: {"lines": [196, 198], "branches": []}

from pymonet.either import Right
from pymonet.maybe import Maybe


def test_right_to_maybe_returns_just_with_value():
    result = Right(42).to_maybe()
    assert isinstance(result, Maybe)
    assert result.value == 42
    assert result == Maybe.just(42)


def test_right_to_maybe_with_string_value():
    result = Right("success").to_maybe()
    assert isinstance(result, Maybe)
    assert result.value == "success"
    assert result == Maybe.just("success")
