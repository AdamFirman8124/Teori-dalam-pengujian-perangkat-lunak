# file: project/f102/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

"""Tests for f102.choose_num covering all lines and branches (lines 3-9)."""

import pytest

from f102 import choose_num


def test_x_greater_than_y_returns_minus_one():
    """Branch: x > y -> return -1 (line 4)."""
    assert choose_num(5, 3) == -1
    assert choose_num(10, 2) == -1


def test_y_even_returns_y():
    """Branch: y % 2 == 0 -> return y (line 6)."""
    assert choose_num(2, 8) == 8
    assert choose_num(4, 4) == 4  # x == y but y even: even check wins first
    assert choose_num(12, 20) == 20


def test_x_equals_y_odd_returns_minus_one():
    """Branch: x == y with odd y -> return -1 (line 8)."""
    assert choose_num(7, 7) == -1
    assert choose_num(1, 1) == -1


def test_y_odd_x_less_than_y_returns_y_minus_one():
    """Branch: y odd and x < y -> return y - 1 (line 9)."""
    assert choose_num(3, 9) == 8
    assert choose_num(1, 5) == 4
    assert choose_num(2, 7) == 6


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (5, 3, -1),   # x > y
        (2, 8, 8),    # y even
        (7, 7, -1),   # x == y, y odd
        (3, 9, 8),    # y odd, x < y
        (0, 0, 0),    # x == y, y even
        (4, 5, 4),    # y odd, y - 1 even
    ],
)
def test_choose_num_parametrized(x, y, expected):
    """Exhaustive parametrized coverage of every return path."""
    assert choose_num(x, y) == expected
