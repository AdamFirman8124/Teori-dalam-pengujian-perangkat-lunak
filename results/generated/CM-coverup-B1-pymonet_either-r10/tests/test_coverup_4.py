# file: project/pymonet/either.py:59-68
# asked: {"lines": [66, 68], "branches": []}
# gained: {"lines": [66, 68], "branches": []}

from pymonet.either import Left, Right
from pymonet.monad_try import Try


def test_right_to_try_returns_successful_try_with_same_value():
    result = Right(42).to_try()

    assert isinstance(result, Try)
    assert result.value == 42
    assert result.is_success is True


def test_left_to_try_returns_failed_try_with_same_value():
    result = Left("error").to_try()

    assert isinstance(result, Try)
    assert result.value == "error"
    assert result.is_success is False
    assert result == Try("error", is_success=False)


def test_to_try_preserves_value_identity():
    value = {"key": "value"}

    right_result = Right(value).to_try()
    left_result = Left(value).to_try()

    assert right_result.value is value
    assert left_result.value is value
    assert right_result.is_success is True
    assert left_result.is_success is False
