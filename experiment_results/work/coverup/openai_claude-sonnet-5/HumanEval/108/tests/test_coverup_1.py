# file: script_108.py:1-17
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17], "branches": [[13, 13], [13, 14]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17], "branches": [[13, 13], [13, 14]]}

import pytest
from script_108 import count_nums


def test_count_nums_empty():
    assert count_nums([]) == 0


def test_count_nums_all_positive():
    assert count_nums([1, 1, 2]) == 3


def test_count_nums_mixed():
    assert count_nums([-1, 11, -11]) == 1


def test_count_nums_single_negative():
    assert count_nums([-1]) == 0


def test_count_nums_negative_with_positive_digit_sum():
    assert count_nums([-123]) == 1


def test_count_nums_negative_with_negative_digit_sum():
    assert count_nums([-321]) == 0


def test_count_nums_zero():
    assert count_nums([0]) == 0


def test_count_nums_multiple_negatives():
    # -5: digits are -5, sum = -5 (not > 0)
    # -10: digits are -1, 0, sum = -1 (not > 0)
    # -15: digits are -1, 5, sum = 4 (> 0)
    assert count_nums([-5, -10, -15]) == 1


def test_count_nums_large_negative():
    # -999: digits are -9, 9, 9, sum = -9 + 9 + 9 = 9 (> 0)
    assert count_nums([-999]) == 1


def test_count_nums_mixed_with_zero():
    assert count_nums([0, 1, -1, 2, -2]) == 2


def test_count_nums_negative_sum_equal_zero():
    # -100: digits are -1, 0, 0, sum = -1 (not > 0)
    assert count_nums([-100]) == 0
