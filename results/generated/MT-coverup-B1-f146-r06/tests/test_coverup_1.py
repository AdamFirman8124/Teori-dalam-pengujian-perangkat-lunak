# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

import pytest

from f146 import specialFilter


def test_empty_list_returns_zero():
    assert specialFilter([]) == 0


def test_numbers_not_greater_than_ten_are_ignored():
    # Covers the False branch of `num > 10` (line 6)
    assert specialFilter([10, -13, 9, 0, -5]) == 0


def test_numbers_greater_than_ten_with_odd_first_and_last_digit():
    # Covers lines 7-9 and the True branch of line 9, and line 10 (count += 1)
    assert specialFilter([15, 33, 73, 91, 111]) == 5


def test_numbers_greater_than_ten_with_even_first_or_last_digit():
    # Covers the False branch of line 9
    assert specialFilter([12, 20, 44, 98, 100]) == 0


def test_mixed_input_counts_only_matching_numbers():
    # Exercises both branches of line 9 in a single call
    # Matches: 11, 35, 57, 79, 99 -> 5
    assert specialFilter([11, 22, 35, 46, 57, 68, 79, 88, 99, 10]) == 5


def test_negative_numbers_are_ignored_even_if_abs_matches():
    # str(-15) is '-15', but num > 10 is False so it is skipped entirely
    assert specialFilter([-15, -33]) == 0


def test_large_numbers():
    assert specialFilter([13579, 97531, 135780]) == 2
