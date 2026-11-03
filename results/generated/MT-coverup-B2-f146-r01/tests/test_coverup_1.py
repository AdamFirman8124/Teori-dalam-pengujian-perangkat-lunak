# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

import pytest

from f146 import specialFilter


def test_empty_list_returns_zero():
    """Covers line 4 (count = 0) and line 12 (return count) with an empty loop body."""
    assert specialFilter([]) == 0


def test_numbers_not_greater_than_ten_are_skipped():
    """Covers the False branch of 'num > 10' (line 6), including negatives and 10 itself."""
    assert specialFilter([1, 2, 3, 10, 0, -5, -73, -15]) == 0


def test_numbers_greater_than_ten_with_even_first_or_last_digit():
    """Covers the False branch of the odd-digit check (line 9).

    21: first digit even (short-circuits the 'and' before checking the last digit)
    12: first digit odd, last digit even
    20: first digit even, last digit even
    100: first digit odd, last digit even
    """
    assert specialFilter([21, 12, 20, 100]) == 0


def test_numbers_greater_than_ten_with_odd_first_and_last_digit():
    """Covers the True branch of the odd-digit check (line 9) and the increment (line 10)."""
    assert specialFilter([11, 13, 35, 97, 101, 12345]) == 6


def test_mixed_input_covers_all_branches():
    """A single call exercising every branch: loop, 'num > 10' both ways,
    odd-digit check both ways, and the increment."""
    # 15 -> counted, -73 -> skipped (not > 10), 14 -> last digit even,
    # -15 -> skipped, 33 -> counted, 12 -> last digit even,
    # 101 -> counted, 10 -> skipped (not > 10), 88 -> first digit even
    assert specialFilter([15, -73, 14, -15, 33, 12, 101, 10, 88]) == 3
