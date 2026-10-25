# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

import pytest

from f146 import specialFilter


def test_empty_list_returns_zero():
    assert specialFilter([]) == 0


def test_numbers_not_greater_than_ten_are_ignored():
    # Covers the False branch of `num > 10` (line 6)
    assert specialFilter([10, -33, 5, 0, -100]) == 0


def test_numbers_greater_than_ten_with_even_digits_are_ignored():
    # Covers lines 7-8 and the False branch of line 9
    assert specialFilter([12, 20, 22, 100, 246]) == 0


def test_first_digit_odd_last_digit_even_is_ignored():
    # First digit odd, last digit even -> not counted
    assert specialFilter([12, 14, 16, 18]) == 0


def test_first_digit_even_last_digit_odd_is_ignored():
    # First digit even, last digit odd -> not counted
    assert specialFilter([21, 41, 61, 81]) == 0


def test_first_and_last_digits_odd_are_counted():
    # Covers the True branch of line 9 and line 10 (count += 1)
    assert specialFilter([11, 33, 15, 97, 111, 575]) == 6


def test_mixed_input_counts_only_matching_numbers():
    # Covers loop iteration over multiple elements with mixed outcomes
    nums = [1, 10, 12, 13, 33, 44, 57, 99, 100, 101, -15]
    # Matching: 13, 33, 57, 99, 101
    assert specialFilter(nums) == 5


def test_result_is_int_and_non_negative():
    result = specialFilter([11, 22, 33])
    assert isinstance(result, int)
    assert result == 2
