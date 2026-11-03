# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f155 import even_odd_count


def test_even_odd_count_mixed_digits():
    """Covers both the even branch (line 7) and odd branch (line 9)."""
    assert even_odd_count(123456) == (3, 3)


def test_even_odd_count_all_even():
    """Covers the even branch only."""
    assert even_odd_count(2468) == (4, 0)


def test_even_odd_count_all_odd():
    """Covers the odd branch only."""
    assert even_odd_count(1357) == (0, 4)


def test_even_odd_count_negative_number():
    """Covers the abs() call on a negative number."""
    assert even_odd_count(-123456) == (3, 3)


def test_even_odd_count_zero():
    """Zero is a single even digit."""
    assert even_odd_count(0) == (1, 0)


def test_even_odd_count_negative_zero():
    """Negative zero behaves like zero."""
    assert even_odd_count(-0) == (1, 0)


def test_even_odd_count_single_digit_even():
    assert even_odd_count(8) == (1, 0)


def test_even_odd_count_single_digit_odd():
    assert even_odd_count(9) == (0, 1)


def test_even_odd_count_returns_tuple():
    """Postcondition: result is a tuple of two non-negative ints summing to digit count."""
    result = even_odd_count(1029384756)
    assert isinstance(result, tuple)
    assert len(result) == 2
    even, odd = result
    assert even >= 0 and odd >= 0
    assert even + odd == 10
    assert result == (5, 5)
