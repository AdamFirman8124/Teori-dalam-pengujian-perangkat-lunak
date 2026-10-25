# file: project/f131/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

import pytest

from f131 import digits


def test_digits_all_even_returns_zero():
    assert digits(2468) == 0
    assert digits(0) == 0


def test_digits_single_odd_digit():
    assert digits(7) == 7
    assert digits(1) == 1


def test_digits_all_odd_product():
    assert digits(135) == 15
    assert digits(999) == 729


def test_digits_mixed_even_and_odd():
    assert digits(1234) == 3
    assert digits(246135) == 15


def test_digits_ignores_even_digits_in_product():
    assert digits(20) == 0
    assert digits(102) == 1
