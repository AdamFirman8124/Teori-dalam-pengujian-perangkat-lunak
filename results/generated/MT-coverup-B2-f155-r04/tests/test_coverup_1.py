# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f155 import even_odd_count


def test_even_digits_only():
    """Covers the even-digit branch (lines 6-7) with all-even digits."""
    assert even_odd_count(2468) == (4, 0)


def test_odd_digits_only():
    """Covers the odd-digit branch (lines 6, 9) with all-odd digits."""
    assert even_odd_count(1357) == (0, 4)


def test_mixed_digits():
    """Covers both branches within a single call."""
    assert even_odd_count(123456) == (3, 3)


def test_negative_number():
    """Covers the abs(num) call on line 5 with a negative input."""
    assert even_odd_count(-123) == (1, 2)


def test_zero():
    """Covers the single-digit '0' case, which is even."""
    assert even_odd_count(0) == (1, 0)
