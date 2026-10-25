# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

import pytest

from f114 import minSubArraySum


def test_min_sub_array_sum_mixed_values():
    # Mixed positives/negatives: the minimal-sum subarray is [-2, -3, -4]
    # whose sum is -9; lines 3-9 and 12-13 execute, line 10-11 branch not taken.
    nums = [2, -2, -3, -4, 5]
    result = minSubArraySum(nums)
    assert result == -9


def test_min_sub_array_sum_all_positive():
    # All-positive input: s never goes positive after negation, max_sum stays 0,
    # so lines 10-11 execute (fallback to max of negated values = -min(nums)).
    # The minimal subarray sum of all-positive nums is its smallest element.
    nums = [1, 2, 3, 4]
    result = minSubArraySum(nums)
    assert result == 1


def test_min_sub_array_sum_single_element():
    # Single negative element exercises the main loop once.
    assert minSubArraySum([-7]) == -7


def test_min_sub_array_sum_single_positive_element():
    # Single positive element exercises the max_sum == 0 fallback branch;
    # the minimal subarray sum is the element itself.
    assert minSubArraySum([5]) == 5
