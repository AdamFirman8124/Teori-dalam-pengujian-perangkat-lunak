# file: script_133.py:1-18
# asked: {"lines": [14, 15, 16, 17, 18], "branches": [[16, 17], [16, 18]]}
# gained: {"lines": [14, 15, 16, 17, 18], "branches": [[16, 17], [16, 18]]}

import pytest


def test_sum_squares_basic():
    from script_133 import sum_squares
    assert sum_squares([1, 2, 3]) == 14


def test_sum_squares_perfect_squares():
    from script_133 import sum_squares
    assert sum_squares([1, 4, 9]) == 98


def test_sum_squares_odd_numbers():
    from script_133 import sum_squares
    assert sum_squares([1, 3, 5, 7]) == 84


def test_sum_squares_with_floats():
    from script_133 import sum_squares
    assert sum_squares([1.4, 4.2, 0]) == 29


def test_sum_squares_with_negative():
    from script_133 import sum_squares
    assert sum_squares([-2.4, 1, 1]) == 6


def test_sum_squares_empty_list():
    from script_133 import sum_squares
    assert sum_squares([]) == 0


def test_sum_squares_single_element():
    from script_133 import sum_squares
    assert sum_squares([5]) == 25


def test_sum_squares_single_float():
    from script_133 import sum_squares
    assert sum_squares([2.1]) == 9


def test_sum_squares_all_zeros():
    from script_133 import sum_squares
    assert sum_squares([0, 0, 0]) == 0


def test_sum_squares_negative_values():
    from script_133 import sum_squares
    assert sum_squares([-1.5, -2.5, -3.5]) == 14
