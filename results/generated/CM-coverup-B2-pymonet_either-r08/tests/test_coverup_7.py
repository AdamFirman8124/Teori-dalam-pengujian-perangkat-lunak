# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.validation import Validation


def test_left_to_validation_returns_failed_validation():
    """Left.to_validation must return a failed Validation whose errors
    contain the Left's value wrapped in a list."""
    left = Left("error_value")

    result = left.to_validation()

    assert isinstance(result, Validation)
    assert result.is_fail() is True
    assert result.value is None
    assert result.errors == ["error_value"]


def test_left_to_validation_uses_local_import(monkeypatch):
    """Lines 145-147 execute a local import of Validation; verify the
    imported symbol is actually used to build the result, by patching
    pymonet.validation.Validation and observing the call."""
    sentinel = object()

    class FakeValidation:
        calls = []

        @classmethod
        def fail(cls, errors):
            cls.calls.append(errors)
            return sentinel

    # The import inside to_validation resolves pymonet.validation.Validation
    # at call time, so patching the module attribute covers the import line
    # and proves the returned object comes from it.
    monkeypatch.setattr("pymonet.validation.Validation", FakeValidation)

    result = Left(42).to_validation()

    assert result is sentinel
    assert FakeValidation.calls == [[42]]
