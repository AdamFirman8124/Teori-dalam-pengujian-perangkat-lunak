# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

import pytest

from f146 import specialFilter


def test_empty_list():
    assert specialFilter([]) == 0


def test_no_numbers_above_ten():
    assert specialFilter([1, 10, -3, 9]) == 0


def test_above_ten_but_even_first_digit():
    # num > 10 branch taken, but first digit is even -> not counted
    assert specialFilter([22, 44, 68]) == 0


def test_above_ten_but_even_last_digit():
    # num > 10 branch taken, first digit odd but last digit even -> not counted
    assert specialFilter([12, 14, 16]) == 0


def test_first_and_last_digits_odd():
    assert specialFilter([11, 13, 15, 17, 19, 31, 97, 135, 339]) == 9


def test_negative_numbers_ignored():
    # negative numbers are never > 10, so never counted
    assert specialFilter([-11, -33, -97]) == 0


def test_mixed_list():
    assert specialFilter([15, -2, 44, 0, 12, 33, 100, 101]) == 3
