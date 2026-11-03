# file: project/f102/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest

from f102 import choose_num


def test_choose_num_x_greater_than_y_returns_minus_one():
    # Covers lines 3-4: x > y branch
    assert choose_num(12, 1) == -1


def test_choose_num_y_even_returns_y():
    # Covers lines 5-6: y % 2 == 0 branch
    assert choose_num(12, 12) == 12


def test_choose_num_x_equals_y_odd_returns_minus_one():
    # Covers lines 7-8: x == y branch (with y odd)
    assert choose_num(13, 13) == -1


def test_choose_num_y_odd_x_less_than_y_returns_y_minus_one():
    # Covers line 9: fallthrough return y - 1
    assert choose_num(12, 13) == 12
