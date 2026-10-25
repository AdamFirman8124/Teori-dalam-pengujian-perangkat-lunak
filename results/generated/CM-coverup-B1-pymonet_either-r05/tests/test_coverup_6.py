# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.validation import Validation


def test_left_to_validation_returns_failed_validation():
    left = Left(42)

    result = left.to_validation()

    # to_validation must import and use pymonet.validation.Validation
    assert isinstance(result, Validation)
    assert result.is_fail() is True
    assert result.errors == [42]
    # the original Left value is wrapped as the single error
    assert result.value is None or result.value == left.value


def test_left_to_validation_wraps_value_in_error_list():
    left = Left("boom")

    result = left.to_validation()

    assert isinstance(result, Validation)
    assert result.errors == ["boom"]
    assert result.is_fail() is True
