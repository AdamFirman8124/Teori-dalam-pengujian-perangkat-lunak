# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

import pytest

from f003 import below_zero


def test_below_zero_returns_true_when_balance_drops_negative():
    """Balance goes below zero mid-sequence -> True (covers lines 6-11)."""
    assert below_zero([1, 2, -5]) is True


def test_below_zero_returns_true_on_first_negative_operation():
    """A single negative operation immediately drives balance below zero."""
    assert below_zero([-1]) is True


def test_below_zero_returns_false_when_balance_stays_nonnegative():
    """Balance never drops below zero -> False (covers lines 6-10, 13)."""
    assert below_zero([1, 2, 3]) is False


def test_below_zero_returns_false_for_empty_operations():
    """Empty operation list: loop body never runs, returns False."""
    assert below_zero([]) is False


def test_below_zero_returns_false_when_balance_hits_exactly_zero():
    """Balance touching exactly zero is not below zero -> False (boundary)."""
    assert below_zero([5, -5, 3]) is False


def test_below_zero_returns_true_after_temporary_recovery():
    """Balance recovers to positive but later dips below zero -> True."""
    assert below_zero([10, -5, -10, 100]) is True
