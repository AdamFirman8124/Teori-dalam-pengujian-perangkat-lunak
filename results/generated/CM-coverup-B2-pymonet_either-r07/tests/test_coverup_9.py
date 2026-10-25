# file: project/pymonet/either.py:200-209
# asked: {"lines": [207, 209], "branches": []}
# gained: {"lines": [207, 209], "branches": []}

import pytest

from pymonet.either import Right
from pymonet.validation import Validation


def test_right_to_validation_returns_successful_validation():
    """Right.to_validation should return a successful Validation
    wrapping the original value with no errors."""
    right = Right(42)

    result = right.to_validation()

    assert isinstance(result, Validation)
    assert result.value == 42
    assert result.errors == []
    assert not result.is_fail()


def test_right_to_validation_with_falsy_value():
    """to_validation must still succeed for falsy values (e.g. None, 0)."""
    for value in (None, 0, "", []):
        result = Right(value).to_validation()

        assert isinstance(result, Validation)
        assert result.value == value
        assert result.errors == []
