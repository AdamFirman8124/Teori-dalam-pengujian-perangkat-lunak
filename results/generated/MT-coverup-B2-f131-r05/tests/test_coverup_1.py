# file: project/f131/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

from f131 import digits


def test_digits_returns_zero_when_no_odd_digits():
    assert digits(24680) == 0


def test_digits_returns_product_of_odd_digits():
    assert digits(12345679) == 945
