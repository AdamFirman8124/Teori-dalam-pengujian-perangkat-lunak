# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.validation import Validation


@pytest.mark.parametrize("value", [42, "error", None, 0, ""])
def test_left_to_validation_returns_failed_validation(value):
    left = Left(value)

    result = left.to_validation()

    assert isinstance(result, Validation)
    assert result == Validation.fail([value])
    assert result.is_fail() is True
    assert result.is_success() is False
    assert result.errors == [value]
    assert left.value == value


def test_left_to_validation_wraps_value_in_list():
    result = Left("something went wrong").to_validation()

    assert result == Validation.fail(["something went wrong"])
    assert result.errors == ["something went wrong"]
    assert result.is_fail() is True
    assert result.is_success() is False
