# file: project/f131/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

import pytest

from f131 import digits


def test_digits_all_even_digits_returns_zero():
    assert digits(2468) == 0


def test_digits_negative_raises_value_error():
    # str(-24) contains '-', which int() cannot parse
    with pytest.raises(ValueError):
        digits(-24)


def test_digits_single_odd_digit():
    assert digits(3) == 3


def test_digits_mixed_digits_returns_product_of_odds():
    assert digits(1234) == 3


def test_digits_all_odd_digits_returns_product():
    assert digits(135) == 15


def test_digits_zero_returns_zero():
    assert digits(0) == 0
