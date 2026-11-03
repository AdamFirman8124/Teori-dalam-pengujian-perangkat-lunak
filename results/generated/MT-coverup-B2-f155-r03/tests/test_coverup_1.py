# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f155 import even_odd_count


def test_even_odd_count_mixed_digits():
    """Positive number with both even and odd digits exercises both branches."""
    assert even_odd_count(123) == (1, 2)  # even: 2; odd: 1, 3
    assert even_odd_count(5081) == (2, 2)  # even: 5? no -> even: 0, 8; odd: 5, 1


def test_even_odd_count_negative_number():
    """Negative input exercises the abs() branch."""
    assert even_odd_count(-12) == (1, 1)  # abs(-12) = 12: even: 2; odd: 1
    assert even_odd_count(-246) == (3, 0)


def test_even_odd_count_zero():
    """Zero is a single even digit."""
    assert even_odd_count(0) == (1, 0)


def test_even_odd_count_all_even():
    """All even digits: even branch taken every iteration."""
    assert even_odd_count(2468) == (4, 0)


def test_even_odd_count_all_odd():
    """All odd digits: else branch taken every iteration."""
    assert even_odd_count(1357) == (0, 4)


def test_even_odd_count_single_digit():
    assert even_odd_count(7) == (0, 1)
    assert even_odd_count(8) == (1, 0)
