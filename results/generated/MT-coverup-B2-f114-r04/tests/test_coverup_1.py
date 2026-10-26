# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

import pytest

from f114 import minSubArraySum


def test_min_sub_array_sum_mixed():
    # Covers lines 3-9 (loop with s < 0 reset) and 12-13.
    # For [2, 3, 4, 1, 2, 4], the minimum-sum subarray is [4, 1, 2] -> sum 7? No:
    # minimum subarray sum is the single element 1... but the algorithm computes
    # max of negated prefix sums, i.e. min subarray sum = -max_sum.
    # Negated array: [-2, -3, -4, -1, -2, -4]; max subarray sum of negated is -1
    # (best is just [-1]), so min_sum = 1.
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1


def test_min_sub_array_sum_all_positive():
    # Covers line 10-11 branch (max_sum == 0 after loop, since all s stay 0).
    # All elements positive -> min subarray is the smallest single element.
    assert minSubArraySum([5, 3, 8]) == 3


def test_min_sub_array_sum_single_element():
    # Single positive element exercises the max_sum == 0 branch too.
    assert minSubArraySum([7]) == 7


def test_min_sub_array_sum_single_negative():
    # Single negative element exercises the normal loop path.
    assert minSubArraySum([-7]) == -7


def test_min_sub_array_sum_does_not_mutate_input():
    nums = [2, -1, 3]
    snapshot = list(nums)
    minSubArraySum(nums)
    assert nums == snapshot
