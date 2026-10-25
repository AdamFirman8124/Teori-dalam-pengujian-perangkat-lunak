# file: project/f102/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

from f102 import choose_num


def test_x_greater_than_y_returns_minus_one():
    assert choose_num(5, 3) == -1
    assert choose_num(10, 2) == -1


def test_y_even_returns_y():
    assert choose_num(2, 4) == 4
    assert choose_num(4, 4) == 4


def test_x_equals_y_odd_returns_minus_one():
    assert choose_num(5, 5) == -1
    assert choose_num(7, 7) == -1


def test_y_odd_x_less_than_y_returns_y_minus_one():
    assert choose_num(2, 5) == 4
    assert choose_num(3, 5) == 4
