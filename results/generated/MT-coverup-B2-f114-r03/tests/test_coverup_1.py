# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

"""Tests for f114.minSubArraySum covering lines 3-13 and all their branches.

The function is pure (no I/O, no globals, no mutation of its argument), so no
monkeypatching or fixture-based teardown is required; each test leaves no
residual state behind.
"""

import pytest

from f114 import minSubArraySum


def test_all_positive_hits_max_sum_zero_branch():
    # With all-positive values, every accumulated s is reset to 0
    # (line 7 True branch) so max_sum stays 0, forcing line 11 to run
    # (line 10 True branch). Result is the smallest single element.
    nums = [2, 3, 4, 1, 2, 4]
    assert minSubArraySum(nums) == 1


def test_all_negative_hits_kadane_branch():
    # With all-negative values, s never goes negative (line 7 False branch)
    # and max_sum ends non-zero (line 10 False branch), so line 11 is skipped.
    # The minimum subarray is the whole array.
    nums = [-1, -2, -3]
    assert minSubArraySum(nums) == -6


def test_mixed_signs_covers_both_branches():
    # Mixed signs exercise both outcomes of the `s < 0` comparison and keep
    # max_sum > 0, so the max_sum == 0 fallback (lines 10-11) is not taken.
    nums = [1, -2, 3, -4, 5]
    assert minSubArraySum(nums) == -4  # best (most negative) subarray is [-4]


def test_single_positive_element():
    # Single element: covers loop body, s < 0 True branch and the
    # max_sum == 0 fallback computing max(-i for i in nums).
    assert minSubArraySum([7]) == 7


def test_single_negative_element():
    # Single negative element: covers s < 0 False branch and the
    # max_sum != 0 path.
    assert minSubArraySum([-7]) == -7


def test_input_is_not_mutated():
    # Postcondition: the argument list is left untouched (no state pollution).
    nums = [3, -1, 4, -1, 5]
    snapshot = list(nums)
    result = minSubArraySum(nums)
    assert nums == snapshot
    assert result == -1  # most negative single element / subarray [-1]


def test_result_never_exceeds_smallest_single_element():
    # Postcondition: the returned value must be <= any single element,
    # since every element is itself a subarray.
    nums = [5, -9, 6, -2, 3]
    result = minSubArraySum(nums)
    assert result == min(nums)
