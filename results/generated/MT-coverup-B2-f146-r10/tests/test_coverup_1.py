# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

from f146 import specialFilter


def test_empty_list_returns_zero():
    """Covers line 4 (count = 0) and line 12 (return) with an empty iterable."""
    assert specialFilter([]) == 0


def test_numbers_not_greater_than_ten_are_ignored():
    """Covers the False branch of 'num > 10' on line 6."""
    assert specialFilter([-15, -1, 0, 4, 10]) == 0


def test_first_digit_even_is_not_counted():
    """Covers the False branch of line 9 when the first digit is even."""
    assert specialFilter([22, 44, 86, 246]) == 0


def test_last_digit_even_is_not_counted():
    """Covers the short-circuit False branch of line 9 (first digit odd, last digit even)."""
    assert specialFilter([18, 30, 56, 90]) == 0


def test_both_digits_odd_are_counted():
    """Covers the True branch of line 9 and the increment on line 10."""
    assert specialFilter([15, 33, 57, 79, 97, 11]) == 6


def test_mixed_input():
    """Covers every line and branch in a single call."""
    assert specialFilter([15, -2, 1, 22, 18, 33, 97, 10, 11, 12]) == 4
