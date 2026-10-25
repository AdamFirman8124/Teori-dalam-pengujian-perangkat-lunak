# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

from pymonet.either import Left
from pymonet.validation import Validation


def test_left_to_validation_returns_failed_validation():
    left = Left("error")
    result = left.to_validation()

    assert isinstance(result, Validation)
    assert result == Validation.fail(["error"])
    assert result.value is None
    assert result.errors == ["error"]


def test_left_to_validation_wraps_value_in_list():
    value = 42
    left = Left(value)
    result = left.to_validation()

    assert isinstance(result, Validation)
    assert result.value is None
    assert result.errors == [value]
    assert result.errors == [left.value]
