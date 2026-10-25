# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.validation import Validation


def test_left_to_validation_returns_failed_validation_with_value_as_single_error():
    left = Left("error-value")

    result = left.to_validation()

    assert isinstance(result, Validation)
    assert result.is_fail() is True
    assert result.is_success() is False if hasattr(result, "is_success") else True
    assert result.errors == ["error-value"]
    assert result.value is None
    # Original Left is unchanged
    assert left.value == "error-value"
    assert left.is_left() is True


@pytest.mark.parametrize("value", [42, 0, "", None, ("a", 1), {"code": 404}])
def test_left_to_validation_wraps_any_value_in_error_list(value):
    left = Left(value)

    result = left.to_validation()

    assert isinstance(result, Validation)
    assert result.is_fail() is True
    assert result.errors == [value]
    assert len(result.errors) == 1
    assert result.errors[0] == value
    assert result.value is None
    assert left.value == value


def test_left_to_validation_returns_new_validation_each_call():
    left = Left("boom")

    first = left.to_validation()
    second = left.to_validation()

    assert first is not second
    assert first.errors == second.errors == ["boom"]
    assert first.errors is not second.errors
    # Mutating one result does not pollute the other or the Left
    first.errors.append("extra")
    assert second.errors == ["boom"]
    assert left.value == "boom"
    assert left.to_validation().errors == ["boom"]
