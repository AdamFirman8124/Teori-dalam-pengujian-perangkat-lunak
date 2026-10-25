# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

import pytest

from f114 import minSubArraySum


def test_min_sub_array_sum_mixed_values():
    nums = [2, -2, -3, -4, 5]
    result = minSubArraySum(nums)
    assert result == -9


def test_min_sub_array_sum_all_positive():
    nums = [1, 2, 3, 4]
    result = minSubArraySum(nums)
    assert result == 1


def test_min_sub_array_sum_single_element():
    assert minSubArraySum([-7]) == -7


def test_min_sub_array_sum_single_positive_element():
    assert minSubArraySum([5]) == 5


def test_min_sub_array_sum_all_negative():
    assert minSubArraySum([-1, -2, -3]) == -6
