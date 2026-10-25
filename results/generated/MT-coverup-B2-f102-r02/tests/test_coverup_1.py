# file: project/f102/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest

from f102 import choose_num


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (5, 3, -1),   # x > y -> -1
        (1, 4, 4),    # y even -> y
        (4, 4, 4),    # x == y but y even -> y (even branch wins)
        (3, 3, -1),   # x == y and y odd -> -1
        (2, 7, 6),    # y odd, x < y -> y - 1
        (0, 1, 0),    # y odd, x < y, boundary -> 0
    ],
)
def test_choose_num_all_branches(x, y, expected):
    result = choose_num(x, y)
    assert result == expected


def test_choose_num_x_greater_than_y_returns_minus_one():
    assert choose_num(10, 9) == -1


def test_choose_num_even_y_returns_y():
    assert choose_num(0, 100) == 100


def test_choose_num_equal_odd_returns_minus_one():
    assert choose_num(7, 7) == -1


def test_choose_num_odd_y_less_than_x_returns_y_minus_one():
    result = choose_num(1, 9)
    assert result == 8
    assert result % 2 == 0
    assert result < 9
