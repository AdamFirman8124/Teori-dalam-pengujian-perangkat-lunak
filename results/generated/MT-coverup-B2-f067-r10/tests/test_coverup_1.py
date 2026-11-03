# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f067 import fruit_distribution


def test_fruit_distribution_mixed_digits_and_words():
    """Covers lines 3-7, exercising both branches of `i.isdigit()`."""
    # "5" and "6" are digits -> appended; "apples", "and", "oranges" are not.
    result = fruit_distribution("5 apples and 6 oranges", 19)
    assert result == 19 - (5 + 6)
    assert result == 8


def test_fruit_distribution_with_zero_and_single_digit():
    """Covers digit parsing including a '0' token."""
    result = fruit_distribution("0 apples and 1 oranges", 3)
    assert result == 3 - (0 + 1)
    assert result == 2


def test_fruit_distribution_no_digits():
    """Covers the False branch of `i.isdigit()` exclusively (empty lis)."""
    result = fruit_distribution("apples oranges", 10)
    assert result == 10 - 0
    assert result == 10


def test_fruit_distribution_all_digits():
    """Covers the True branch of `i.isdigit()` exclusively."""
    result = fruit_distribution("2 3", 10)
    assert result == 10 - (2 + 3)
    assert result == 5


def test_fruit_distribution_multi_digit_numbers():
    """Verifies multi-digit tokens are parsed as full integers."""
    result = fruit_distribution("12 apples 34 oranges", 100)
    assert result == 100 - (12 + 34)
    assert result == 54
