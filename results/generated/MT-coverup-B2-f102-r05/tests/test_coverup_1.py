# file: project/f102/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest

from f102 import choose_num


@pytest.mark.parametrize(
    "x, y, expected",
    [
        # Line 4 branch: x > y -> returns -1 immediately
        (12, 1, -1),
        (5, 4, -1),
        (-1, -2, -1),
        # Line 6 branch: x <= y and y is even -> returns y
        (12, 12, 12),
        (1, 10, 10),
        (-4, 0, 0),
        # Line 8 branch: x <= y, y is odd, x == y -> returns -1
        (13, 13, -1),
        (7, 7, -1),
        (-3, -3, -1),
        # Line 9 branch: x <= y, y is odd, x < y -> returns y - 1
        (12, 13, 12),
        (1, 7, 6),
        (-5, -1, -2),
    ],
)
def test_choose_num_branches(x, y, expected):
    """Cover every line/branch of choose_num: x>y, y even, x==y (odd y), and fallback."""
    assert choose_num(x, y) == expected


def test_choose_num_x_greater_than_y_returns_minus_one():
    # Exercises line 3 condition True -> line 4
    assert choose_num(20, 19) == -1


def test_choose_num_even_upper_bound_returns_y():
    # Exercises line 5 condition True -> line 6
    assert choose_num(2, 8) == 8


def test_choose_num_equal_odd_bounds_returns_minus_one():
    # Exercises line 7 condition True -> line 8
    assert choose_num(9, 9) == -1


def test_choose_num_fallback_returns_largest_even_below_y():
    # Exercises line 9 (no early return taken)
    assert choose_num(3, 11) == 10
