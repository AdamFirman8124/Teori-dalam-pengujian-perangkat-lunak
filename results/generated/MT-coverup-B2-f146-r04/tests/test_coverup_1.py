# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

import pytest

from f146 import specialFilter


def test_empty_list_returns_zero():
    """Covers lines 4, 5, 12: initialization, loop over empty iterable, return."""
    assert specialFilter([]) == 0


def test_numbers_not_greater_than_ten_are_ignored():
    """Covers the False branch of line 6 (num > 10)."""
    assert specialFilter([10, 5, 0, -3, -15]) == 0


def test_numbers_greater_than_ten_with_even_first_or_last_digit():
    """Covers lines 7-8 and the False branch of line 9."""
    # 22: first digit even; 21: first digit even; 24: last digit even; 44: both even
    assert specialFilter([22, 21, 24, 44]) == 0


def test_numbers_with_odd_first_and_last_digit_are_counted():
    """Covers line 10 (count += 1) and the True branch of line 9."""
    # 15, 33, 97, 11 all have odd first and last digits and are > 10
    assert specialFilter([15, 33, 97, 11]) == 4


def test_mixed_input_full_branch_coverage():
    """Covers all branches in a single call: line 6 both ways, line 9 both ways, line 10."""
    nums = [1, 10, 12, 15, 23, 35, 100, 111]
    # qualifying: 15, 35, 111 (first and last digits both odd, num > 10)
    assert specialFilter(nums) == 3
