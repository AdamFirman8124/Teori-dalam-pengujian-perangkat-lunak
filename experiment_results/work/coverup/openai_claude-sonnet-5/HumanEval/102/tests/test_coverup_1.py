# file: script_102.py:1-16
# asked: {"lines": [10, 11, 12, 13, 14, 15, 16], "branches": [[10, 11], [10, 12], [12, 13], [12, 14], [14, 15], [14, 16]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 16], "branches": [[10, 11], [10, 12], [12, 13], [12, 14], [14, 15], [14, 16]]}

import pytest
from script_102 import choose_num


def test_choose_num_x_greater_than_y():
    """Test when x > y, should return -1"""
    assert choose_num(15, 10) == -1
    assert choose_num(100, 50) == -1


def test_choose_num_y_is_even():
    """Test when y is even, should return y"""
    assert choose_num(10, 14) == 14
    assert choose_num(1, 20) == 20


def test_choose_num_x_equals_y_both_odd():
    """Test when x == y and both are odd, should return -1"""
    assert choose_num(13, 13) == -1
    assert choose_num(7, 7) == -1


def test_choose_num_y_is_odd_x_less_than_y():
    """Test when y is odd and x < y, should return y - 1"""
    assert choose_num(12, 15) == 14
    assert choose_num(10, 17) == 16
    assert choose_num(1, 5) == 4
