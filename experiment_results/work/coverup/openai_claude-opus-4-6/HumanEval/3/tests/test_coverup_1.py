# file: script_3.py:4-20
# asked: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}
# gained: {"lines": [13, 15, 16, 17, 18, 20], "branches": [[15, 16], [15, 20], [17, 15], [17, 18]]}

from typing import List

import pytest

from script_3 import below_zero


def test_below_zero_never_negative_returns_false():
    # Exercises lines 13, 15, 16, 17 (condition false) and 20.
    operations: List[int] = [1, 2, 3]
    result = below_zero(operations)
    assert result is False
    assert operations == [1, 2, 3]  # input not mutated


def test_below_zero_dips_negative_returns_true():
    # Exercises lines 13, 15, 16, 17 (true) and 18 (early return True).
    operations: List[int] = [1, 2, -4, 5]
    result = below_zero(operations)
    assert result is True
    assert operations == [1, 2, -4, 5]  # input not mutated


def test_below_zero_immediate_withdrawal_returns_true():
    # First iteration goes straight to negative -> lines 16, 17, 18.
    assert below_zero([-1]) is True


def test_below_zero_empty_operations_returns_false():
    # Loop body (lines 16-18) skipped; line 20 reached directly.
    assert below_zero([]) is False


def test_below_zero_touches_zero_but_not_below():
    # Balance reaches exactly 0, never below -> condition on line 17 stays false.
    assert below_zero([5, -5]) is False


def test_below_zero_negative_at_end_returns_true():
    # Multiple iterations before dipping below zero.
    assert below_zero([10, -5, -3, -1, -2]) is True


@pytest.mark.parametrize(
    "operations, expected",
    [
        ([0], False),
        ([0, 0, 0], False),
        ([1, -1, 1, -1], False),
        ([-1, 5], True),
        ([2, -3, 1], True),
        ([100, -50, -50, -1], True),
    ],
)
def test_below_zero_parametrized(operations, expected):
    # Covers both branches of line 17 and both terminal returns.
    assert below_zero(operations) is expected
