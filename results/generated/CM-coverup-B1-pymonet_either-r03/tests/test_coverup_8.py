# file: project/pymonet/either.py:200-209
# asked: {"lines": [207, 209], "branches": []}
# gained: {"lines": [207, 209], "branches": []}

import pytest

from pymonet.either import Right
from pymonet.validation import Validation


def test_right_to_validation_returns_successful_validation():
    """Right.to_validation should return a successful Validation wrapping the same value."""
    right = Right(42)

    result = right.to_validation()

    assert isinstance(result, Validation)
    assert result.value == 42
    assert result.errors == []


def test_right_to_validation_with_none_value():
    """Right(None).to_validation() should still produce a successful Validation."""
    right = Right(None)

    result = right.to_validation()

    assert isinstance(result, Validation)
    assert result.value is None
    assert result.errors == []
