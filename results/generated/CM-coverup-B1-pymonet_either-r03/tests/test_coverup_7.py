# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

from pymonet.either import Left
from pymonet.validation import Validation


def test_left_to_validation_returns_failed_validation():
    result = Left(42).to_validation()

    assert isinstance(result, Validation)
    assert result.is_fail() is True
    assert result.is_success() is False
    assert result.errors == [42]


def test_left_to_validation_wraps_value_in_new_list():
    value = [1, 2]
    result = Left(value).to_validation()

    assert result.is_fail() is True
    assert result.errors == [[1, 2]]
    assert result.errors is not value
    assert result.errors[0] is value


def test_left_to_validation_with_none_value():
    result = Left(None).to_validation()

    assert result.is_fail() is True
    assert result.errors == [None]
