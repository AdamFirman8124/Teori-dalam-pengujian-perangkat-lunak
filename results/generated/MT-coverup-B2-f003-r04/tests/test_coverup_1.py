# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

"""Tests for f003.below_zero covering all lines and branches (lines 6-13)."""

import pytest

from f003 import below_zero


def test_below_zero_returns_true_when_balance_drops_below_zero():
    # Covers: balance = 0, loop entry, balance += op, if-True branch, return True
    assert below_zero([1, 2, -5]) is True


def test_below_zero_returns_true_on_first_negative_operation():
    # Covers: balance = 0, loop entry, balance += op, if-True branch, return True
    assert below_zero([-1]) is True


def test_below_zero_returns_false_when_balance_never_negative():
    # Covers: balance = 0, loop entry, balance += op, if-False branch, return False
    assert below_zero([1, 2, -3]) is False


def test_below_zero_returns_false_for_empty_operations():
    # Covers: balance = 0, loop skipped (zero iterations), return False
    assert below_zero([]) is False


def test_below_zero_balance_of_exactly_zero_is_not_below_zero():
    # Covers: if-False branch when balance == 0 (boundary), return False
    assert below_zero([5, -5]) is False


def test_below_zero_true_only_after_crossing_zero_not_at_zero():
    # Balance touches zero but never goes negative -> False; then dips -> True
    assert below_zero([3, -3, 1]) is False
    assert below_zero([3, -3, 1, -2]) is True


@pytest.mark.parametrize(
    "operations,expected",
    [
        ([], False),
        ([1], False),
        ([-1], True),
        ([1, 2, 3], False),
        ([1, 2, -4], True),
        ([10, -10, 10, -10], False),
        ([10, -11], True),
    ],
)
def test_below_zero_parametrized(operations, expected):
    # Exercises every line/branch across multiple inputs
    assert below_zero(operations) is expected
