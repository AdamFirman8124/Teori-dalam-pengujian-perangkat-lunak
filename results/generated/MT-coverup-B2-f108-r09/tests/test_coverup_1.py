# file: project/f108/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}

import pytest

from f108 import count_nums


def test_count_nums_empty():
    """Empty input covers lines 3-10 (via the call) and returns 0."""
    assert count_nums([]) == 0


def test_count_nums_positive_only():
    """All positive numbers have positive digit sums."""
    assert count_nums([1, 11, 123]) == 3


def test_count_nums_negative_digit_sum_zero():
    """A negative number whose first digit is 1 yields digit sum 0, not counted.
    Exercises the branch where n < 0 (lines 5-6)."""
    # digits_sum(-11) = -1 + 1 = 0 -> filtered out
    assert count_nums([-11]) == 0


def test_count_nums_negative_digit_sum_positive():
    """A negative number with more digit weight after the first digit yields
    a positive digit sum, so it is counted."""
    # digits_sum(-12) = -1 + 2 = 1 -> counted
    assert count_nums([-12]) == 1


def test_count_nums_mixed():
    """Mix of positives, negatives with positive digit sum, and negatives
    with non-positive digit sum."""
    arr = [1, 1, 2, -11, -12, -1]
    # digit sums: 1, 1, 2, 0, 1, -1 -> only first three, plus -12, are > 0
    assert count_nums(arr) == 4


def test_count_nums_zero():
    """Zero has digit sum 0, so it is not counted."""
    assert count_nums([0, 5]) == 1
