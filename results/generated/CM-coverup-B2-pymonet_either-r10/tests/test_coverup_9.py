# file: project/pymonet/either.py:200-209
# asked: {"lines": [207, 209], "branches": []}
# gained: {"lines": [207, 209], "branches": []}

import sys

import pytest

from pymonet.either import Right


def test_right_to_validation_executes_missing_lines(monkeypatch):
    """Right.to_validation must lazily import Validation and return a
    successful Validation wrapping the Right's value (lines 207-209)."""
    # Ensure the lazy import inside to_validation actually executes
    # by removing any previously imported pymonet.validation module.
    monkeypatch.delitem(sys.modules, "pymonet.validation", raising=False)

    right = Right(42)
    validation = right.to_validation()

    # Postconditions: a successful Validation carrying the original value.
    assert validation.is_success()
    assert validation.value == 42
