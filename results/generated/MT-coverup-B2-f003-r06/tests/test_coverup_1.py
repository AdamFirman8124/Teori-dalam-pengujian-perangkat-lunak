# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

"""Tests for f003.below_zero, covering all previously unexecuted lines (6-13)."""

from f003 import below_zero


def test_below_zero_returns_true_when_balance_drops_negative():
    """Lines 6, 8, 9, 10, 11: balance goes below zero -> early return True."""
    # Balance trajectory: 1 -> 3 -> -2, so the `balance < 0` branch is taken.
    result = below_zero([1, 2, -5])
    assert result is True


def test_below_zero_returns_true_on_first_operation():
    """Lines 6, 8, 9, 10, 11: negative on the very first operation."""
    result = below_zero([-1])
    assert result is True


def test_below_zero_returns_false_when_balance_stays_nonnegative():
    """Lines 6, 8, 9, 10 (False branch) and 13: loop completes -> return False."""
    # Balance trajectory: 1 -> 3 -> 1, never negative.
    result = below_zero([1, 2, -2])
    assert result is False


def test_below_zero_returns_false_for_empty_list():
    """Lines 6 and 13: loop body never executes -> return False."""
    result = below_zero([])
    assert result is False


def test_below_zero_returns_false_for_zero_balance():
    """Line 10 boundary: balance of exactly 0 is not below zero -> False."""
    result = below_zero([5, -5])
    assert result is False
