# file: project/f108/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}

import pytest

from f108 import count_nums


def test_count_nums_empty():
    """Empty input: exercises line 10 with an empty filter result."""
    assert count_nums([]) == 0


def test_count_nums_all_positive():
    """Positive numbers: exercises digits_sum without the negative branch (lines 4-5, 7-9)."""
    # digit sums: 1, 1, 2 -> all positive
    assert count_nums([1, 1, 2]) == 3


def test_count_nums_with_negatives():
    """Negative numbers: exercises the negative branch (line 6).

    digit sums: -1 -> -1, 11 -> 2, -11 -> -1 + 1 = 0, so only 11 counts.
    """
    assert count_nums([-1, 11, -11]) == 1


def test_count_nums_zero():
    """Zero: digit sum is 0, which is not > 0, so it is not counted."""
    assert count_nums([0]) == 0


def test_count_nums_mixed():
    """Mixed input covering both branches of the n < 0 check.

    digit sums: 12 -> 3, -12 -> -1 + 2 = 1, 0 -> 0, 7 -> 7, -7 -> -7
    -> 12, -12 and 7 count.
    """
    assert count_nums([12, -12, 0, 7, -7]) == 3


def test_count_nums_multi_digit_negative():
    """Multi-digit negative: verifies first-digit negation in digits_sum.

    digit sum of -123 is -(1) + 2 + 3 = 4 -> counted;
    digit sum of -45 is -(4) + 5 = 1 -> counted;
    digit sum of -50 is -(5) + 0 = -5 -> not counted.
    """
    assert count_nums([-123, -45, -50]) == 2
