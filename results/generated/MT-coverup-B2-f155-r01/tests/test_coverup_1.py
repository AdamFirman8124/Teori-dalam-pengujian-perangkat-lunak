# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f155 import even_odd_count


def test_even_odd_count_mixed_digits():
    """Covers loop, even branch (line 7) and odd branch (line 9), and return (line 10)."""
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(1234) == (2, 2)


def test_even_odd_count_negative_uses_abs():
    """Covers the abs(num) branch with a negative input."""
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-135) == (0, 3)


def test_even_odd_count_zero_is_even():
    """Covers the even branch with a single zero digit."""
    assert even_odd_count(0) == (1, 0)


def test_even_odd_count_all_even_digits():
    """Covers only the even branch (line 7) for every iteration."""
    assert even_odd_count(2468) == (4, 0)


def test_even_odd_count_all_odd_digits():
    """Covers only the odd branch (line 9) for every iteration."""
    assert even_odd_count(1357) == (0, 4)
