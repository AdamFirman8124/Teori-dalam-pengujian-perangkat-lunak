# file: project/pymonet/either.py:200-209
# asked: {"lines": [207, 209], "branches": []}
# gained: {"lines": [207, 209], "branches": []}

import pytest

from pymonet.either import Right
from pymonet.validation import Validation


def test_right_to_validation_returns_successful_validation():
    right = Right(42)

    result = right.to_validation()

    assert isinstance(result, Validation)
    assert result.value == 42
    assert result.errors == []
