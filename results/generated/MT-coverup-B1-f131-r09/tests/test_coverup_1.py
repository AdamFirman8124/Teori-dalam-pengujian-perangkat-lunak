# file: project/f131/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

from f131 import digits


def test_digits_all_even_returns_zero():
    assert digits(2468) == 0


def test_digits_mixed_returns_product_of_odds():
    # 1 * 3 * 5 = 15, even digits 2, 4 ignored
    assert digits(12345) == 15


def test_digits_single_odd_digit():
    assert digits(7) == 7


def test_digits_single_even_digit_returns_zero():
    assert digits(2) == 0
