# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

import pytest

from f146 import specialFilter


def test_empty_list():
    """Empty input: lines 4 and 12 execute, loop body never runs."""
    assert specialFilter([]) == 0


def test_no_numbers_greater_than_ten():
    """Numbers <= 10 take the False branch of 'num > 10' (line 6)."""
    assert specialFilter([10, 9, -11, 0, 3]) == 0


def test_numbers_greater_than_ten_but_not_both_odd_digits():
    """Numbers > 10 whose first or last digit is even: line 9 condition False."""
    # 12: first digit 1 (odd), last digit 2 (even) -> not counted
    # 20: first digit 2 (even), last digit 0 (even) -> not counted
    # 21: first digit 2 (even), last digit 1 (odd) -> not counted
    assert specialFilter([12, 20, 21, 44, 100]) == 0


def test_numbers_greater_than_ten_with_both_odd_digits():
    """Numbers > 10 with odd first and last digit: all lines including 9-10 execute."""
    assert specialFilter([11, 13, 15, 97, 31]) == 5


def test_mixed_input():
    """Mixed input exercising every branch in a single call."""
    nums = [1, 10, 11, 12, 33, 44, 135, -15, 79]
    # qualifying: 11, 33, 135, 79
    assert specialFilter(nums) == 4


def test_negative_numbers_ignored():
    """Negative numbers are never > 10, so they take the False branch."""
    assert specialFilter([-11, -13, -97]) == 0


def test_result_is_non_negative_int():
    """Postcondition: result is always a non-negative int."""
    result = specialFilter([11, 22, 33])
    assert isinstance(result, int)
    assert result >= 0
