# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

from f114 import minSubArraySum


def test_min_sub_array_sum_mixed_single_negative():
    assert minSubArraySum([2, 3, 4, 1, 2, -4, 3, 1, 2]) == -4


def test_min_sub_array_sum_all_positive():
    assert minSubArraySum([2, 3, 4, 1, 2, 3, 1, 2]) == 1


def test_min_sub_array_sum_all_negative():
    assert minSubArraySum([-1, -2, -3]) == -6


def test_min_sub_array_sum_single_negative():
    assert minSubArraySum([-3]) == -3


def test_min_sub_array_sum_single_positive():
    assert minSubArraySum([5]) == 5


def test_min_sub_array_sum_mixed_negative_result():
    assert minSubArraySum([1, -2, -3, 4]) == -5
