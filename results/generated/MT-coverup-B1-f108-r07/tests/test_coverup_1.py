# file: project/f108/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}

import pytest

from f108 import count_nums


def test_count_nums_empty_list():
    assert count_nums([]) == 0


def test_count_nums_all_positive_sums():
    # 1 -> 1, 11 -> 2, 12 -> 3 : all > 0
    assert count_nums([1, 11, 12]) == 3


def test_count_nums_negative_numbers_branch():
    # -1 -> -1, 11 -> 2, -11 -> -2 : only 11 counts
    assert count_nums([-1, 11, -11]) == 1


def test_count_nums_zero_is_not_counted():
    # 0 -> 0, which is not > 0
    assert count_nums([0]) == 0


def test_count_nums_negative_with_trailing_zero():
    # -10 -> digits [1, 0] with first negated -> -1 + 0 = -1 : not counted
    assert count_nums([-10]) == 0


def test_count_nums_positive_with_trailing_zero():
    # 10 -> 1 + 0 = 1 : counted
    assert count_nums([10]) == 1


def test_count_nums_negative_multi_digit_positive_sum():
    # -19 -> -1 + 9 = 8 : counted (negative branch, positive result)
    assert count_nums([-19]) == 1


def test_count_nums_negative_hundreds():
    # -100 -> -1 + 0 + 0 = -1 : not counted
    assert count_nums([-100]) == 0


def test_count_nums_mixed_list():
    arr = [-19, -10, 0, 10, 12, -100]
    # -19 -> 8 (yes), -10 -> -1 (no), 0 -> 0 (no),
    # 10 -> 1 (yes), 12 -> 3 (yes), -100 -> -1 (no)
    assert count_nums(arr) == 3


def test_count_nums_does_not_mutate_input():
    arr = [-19, 10, 0]
    snapshot = list(arr)
    count_nums(arr)
    assert arr == snapshot
