# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f155 import even_odd_count


def test_even_odd_count_mixed_digits():
    """Covers even branch (line 6-7), odd branch (line 8-9) and return (line 10)."""
    result = even_odd_count(1234)
    assert result == (2, 2)


def test_even_odd_count_all_even():
    result = even_odd_count(2468)
    assert result == (4, 0)


def test_even_odd_count_all_odd():
    result = even_odd_count(1357)
    assert result == (0, 4)


def test_even_odd_count_negative_number():
    """Covers the abs() call on a negative input (line 5)."""
    result = even_odd_count(-21)
    assert result == (1, 1)


def test_even_odd_count_zero():
    result = even_odd_count(0)
    assert result == (1, 0)


def test_even_odd_count_negative_all_even():
    result = even_odd_count(-846)
    assert result == (3, 0)
