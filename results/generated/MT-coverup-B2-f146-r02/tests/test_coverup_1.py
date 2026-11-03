# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

import pytest

from f146 import specialFilter


def test_empty_list_returns_zero():
    """Covers lines 4 and 12: initialization and return with no iterations."""
    assert specialFilter([]) == 0


def test_numbers_not_greater_than_ten_are_ignored():
    """Covers line 5-6 with the 'num > 10' branch evaluating to False."""
    assert specialFilter([5, 10, -2, 0]) == 0


def test_numbers_greater_than_ten_with_even_digits_are_ignored():
    """Covers lines 7-9 with the odd-digits condition evaluating to False."""
    # 12: first digit odd, last digit even
    # 21: first digit even, last digit odd
    # 22: both digits even
    # 100: first digit 1 odd, last digit 0 even
    assert specialFilter([12, 21, 22, 100]) == 0


def test_numbers_with_odd_first_and_last_digits_are_counted():
    """Covers line 10: count incremented when both first and last digits are odd."""
    # 15 -> 1 and 5, 33 -> 3 and 3, 97 -> 9 and 7, 53 -> 5 and 3
    assert specialFilter([15, 33, 97, 53]) == 4


def test_mixed_input_counts_only_matching_numbers():
    """Exercises all branches together in a single call."""
    # 15 counts, -2 skipped (not > 10), 33 counts, 22 skipped (even digits),
    # 11 counts, 10 skipped (not > 10), 12 skipped (last digit even)
    assert specialFilter([15, -2, 33, 22, 11, 10, 12]) == 3


def test_negative_large_number_with_odd_digits():
    """Negative numbers are never > 10, so they are skipped even with odd digits."""
    assert specialFilter([-15, -33]) == 0
