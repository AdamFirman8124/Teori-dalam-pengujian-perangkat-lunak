# file: project/f131/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

from f131 import digits


def test_digits_all_odd_digits():
    assert digits(135) == 15
    assert digits(97531) == 945
    assert digits(7) == 7


def test_digits_mixed_odd_and_even_digits():
    assert digits(1234) == 3
    assert digits(246135) == 15
    assert digits(101) == 1


def test_digits_no_odd_digits():
    assert digits(2468) == 0
    assert digits(8) == 0
    assert digits(22222) == 0


def test_digits_zero():
    assert digits(0) == 0
