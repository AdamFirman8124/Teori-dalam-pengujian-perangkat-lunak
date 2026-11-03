# file: project/f131/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

import pytest

from f131 import digits


def test_digits_all_odd_digits():
    # 15 -> digits 1 and 5 are both odd -> product = 1*5 = 5
    assert digits(15) == 5


def test_digits_mixed_digits():
    # 123 -> odd digits 1 and 3 -> product = 1*3 = 3
    assert digits(123) == 3


def test_digits_single_odd_digit():
    # 7 -> single odd digit -> product = 7
    assert digits(7) == 7


def test_digits_no_odd_digits_returns_zero():
    # 2468 -> all digits even -> odd_count == 0 -> return 0
    assert digits(2468) == 0


def test_digits_zero_returns_zero():
    # 0 -> digit 0 is even -> odd_count == 0 -> return 0
    assert digits(0) == 0


def test_digits_single_even_digit_returns_zero():
    # 8 -> digit 8 is even -> odd_count == 0 -> return 0
    assert digits(8) == 0


def test_digits_product_of_multiple_odd_digits():
    # 357 -> odd digits 3, 5, 7 -> product = 3*5*7 = 105
    assert digits(357) == 105
