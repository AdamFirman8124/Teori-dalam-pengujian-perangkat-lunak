# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

import pytest

from f146 import specialFilter


def test_empty_input_returns_zero():
    """Covers lines 4 and 12 (loop never runs)."""
    assert specialFilter([]) == 0


def test_numbers_not_above_ten_are_ignored():
    """Covers the False branch of line 6 (num > 10)."""
    assert specialFilter([1, 10, -3, -11, 0]) == 0


def test_numbers_above_ten_with_even_digits_are_ignored():
    """Covers lines 7-8 and the False branch of line 9."""
    assert specialFilter([20, 44, 100, 88]) == 0


def test_only_first_digit_odd_is_ignored():
    """Covers line 9 with first digit odd but last digit even."""
    assert specialFilter([12, 14, 16, 18]) == 0


def test_only_last_digit_odd_is_ignored():
    """Covers line 9 with first digit even but last digit odd."""
    assert specialFilter([21, 41, 61, 81]) == 0


def test_numbers_with_odd_first_and_last_digits_are_counted():
    """Covers line 10 (count += 1) for several qualifying numbers."""
    assert specialFilter([11, 15, 33, 97, 101]) == 5


def test_mixed_input_counts_only_qualifying_numbers():
    """Covers all branches together in a single pass."""
    assert specialFilter([15, -2, 44, 12, 33, 10, 21, 97]) == 3
