# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.validation import Validation


def test_left_to_validation_returns_failed_validation():
    result = Left("error").to_validation()

    assert isinstance(result, Validation)
    assert result == Validation.fail(["error"])
    assert result.value is None
    assert result.errors == ["error"]
    assert result.is_fail()
    assert not result.is_success()


def test_left_to_validation_wraps_value_in_single_element_list():
    value = {"code": 404}
    result = Left(value).to_validation()

    assert isinstance(result, Validation)
    assert result.value is None
    assert result.errors == [value]
    assert len(result.errors) == 1
    assert result.errors[0] is value


@pytest.mark.parametrize("value", [0, "", None, False, 42, "oops", (1, 2)])
def test_left_to_validation_preserves_any_value_as_error(value):
    result = Left(value).to_validation()

    assert isinstance(result, Validation)
    assert result == Validation.fail([value])
    assert result.value is None
    assert result.errors == [value]
    assert result.is_fail()
    assert not result.is_success()


def test_left_to_validation_does_not_mutate_left():
    left = Left("original")

    result = left.to_validation()

    assert left.value == "original"
    assert result.errors == ["original"]
    result.errors.append("extra")
    assert left.value == "original"
    assert Left("original").to_validation().errors == ["original"]
