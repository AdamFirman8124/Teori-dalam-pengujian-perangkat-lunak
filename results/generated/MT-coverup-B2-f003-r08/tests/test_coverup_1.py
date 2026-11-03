# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

"""Tests for f003.below_zero — covering lines 6-13 and all branches."""

from typing import List

import pytest

from f003 import below_zero


def test_returns_true_when_balance_drops_below_zero():
    # Covers lines 6, 8, 9, 10 (True branch) and 11 (early return True).
    operations: List[int] = [1, 2, -4]
    result = below_zero(operations)
    assert result is True


def test_returns_true_on_first_negative_operation():
    # Covers the immediate dip below zero on the very first operation.
    operations: List[int] = [-1]
    result = below_zero(operations)
    assert result is True


def test_returns_false_when_balance_never_drops_below_zero():
    # Covers lines 6, 8, 9, 10 (False branch) and 13 (return False).
    operations: List[int] = [1, 2, 3]
    result = below_zero(operations)
    assert result is False


def test_returns_false_when_balance_hits_exactly_zero():
    # balance == 0 is NOT below zero, so the False branch of line 10
    # and the final return on line 13 must be taken.
    operations: List[int] = [5, -5, 3]
    result = below_zero(operations)
    assert result is False


def test_returns_false_for_empty_operations():
    # Covers the loop-not-entered branch of line 8, then line 13.
    operations: List[int] = []
    result = below_zero(operations)
    assert result is False


def test_early_return_stops_processing_remaining_operations():
    # Once the balance dips below zero, True is returned immediately;
    # subsequent (even positive) operations cannot change the outcome.
    operations: List[int] = [10, -20, 100]
    result = below_zero(operations)
    assert result is True


def test_result_is_a_bool():
    # Postcondition: the return value is strictly a bool, not just truthy/falsy.
    assert isinstance(below_zero([1, -2]), bool)
    assert isinstance(below_zero([1, 1]), bool)
