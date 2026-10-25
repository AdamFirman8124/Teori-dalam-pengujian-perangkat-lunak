# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

from pymonet.either import Left
from pymonet.validation import Validation


def _assert_is_failure(result):
    assert isinstance(result, Validation)
    is_success = result.is_success() if callable(result.is_success) else result.is_success
    assert is_success is False
    if hasattr(result, "is_fail"):
        is_fail = result.is_fail() if callable(result.is_fail) else result.is_fail
        assert is_fail is True


def test_left_to_validation_returns_failed_validation():
    left = Left(42)

    result = left.to_validation()

    _assert_is_failure(result)
    assert result.errors == [42]
    assert left.value == 42


def test_left_to_validation_wraps_value_in_list():
    value = {"a": 1}

    result = Left(value).to_validation()

    _assert_is_failure(result)
    assert result.errors == [value]
    assert result.errors[0] is value


def test_left_to_validation_with_none_value():
    result = Left(None).to_validation()

    _assert_is_failure(result)
    assert result.errors == [None]


def test_left_to_validation_returns_fresh_list_per_call():
    left = Left("error")

    first = left.to_validation()
    second = left.to_validation()

    _assert_is_failure(first)
    _assert_is_failure(second)
    assert first.errors == second.errors == ["error"]
    assert first.errors is not second.errors
