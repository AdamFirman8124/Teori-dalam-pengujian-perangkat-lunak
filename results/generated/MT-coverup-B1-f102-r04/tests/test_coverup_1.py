# file: project/f102/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

from f102 import choose_num


def test_choose_num_returns_minus_one_when_x_is_greater():
    assert choose_num(4, 3) == -1


def test_choose_num_returns_y_when_y_is_even():
    assert choose_num(1, 4) == 4


def test_choose_num_returns_minus_one_when_equal_and_odd():
    assert choose_num(3, 3) == -1


def test_choose_num_returns_previous_even_number_when_y_is_odd():
    assert choose_num(1, 5) == 4
