# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

import pytest

from f114 import minSubArraySum


def test_min_sub_array_sum_positive_elements():
    # Negated array is [-2,-3,-4,-1,-2,4,-3,-1,-2]; best subarray is [4] -> min sum -4
    result = minSubArraySum([2, 3, 4, 1, 2, -4, 3, 1, 2])
    assert result == -4


def test_min_sub_array_sum_single_negative():
    # Single negative element: minimal-sum subarray is [-3]
    result = minSubArraySum([-3])
    assert result == -3


def test_min_sub_array_sum_all_positive():
    # All-positive input keeps s at 0, so max_sum == 0 and the fallback
    # branch (lines 10-11) runs: max(-i for i in nums) = -2 -> min sum 2
    result = minSubArraySum([2, 3, 4])
    assert result == 2


def test_min_sub_array_sum_single_positive():
    # Single positive element: fallback branch gives max(-i) = -5 -> min sum 5
    result = minSubArraySum([5])
    assert result == 5


def test_min_sub_array_sum_mixed_with_negative_result():
    # Negated array is [-1,2,3,-4]; best subarray is [2,3] -> min sum -5
    result = minSubArraySum([1, -2, -3, 4])
    assert result == -5


def test_min_sub_array_sum_all_negative():
    # All-negative input: running s accumulates positives, max_sum = 6 -> min sum -6
    result = minSubArraySum([-1, -2, -3])
    assert result == -6
