# file: project/f102/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest

from f102 import choose_num


def test_choose_num_x_greater_than_y_returns_minus_one():
    # Covers lines 3-4 (branch x > y is True)
    assert choose_num(5, 3) == -1


def test_choose_num_y_even_returns_y():
    # Covers lines 5-6 (branch x > y is False, y % 2 == 0 is True)
    assert choose_num(2, 4) == 4


def test_choose_num_x_equals_y_odd_returns_minus_one():
    # Covers lines 7-8 (branch y % 2 == 0 is False, x == y is True)
    assert choose_num(3, 3) == -1


def test_choose_num_returns_largest_even_below_y():
    # Covers line 9 (all branches False: x < y, y odd, x != y)
    assert choose_num(2, 5) == 4
    assert choose_num(1, 7) == 6
