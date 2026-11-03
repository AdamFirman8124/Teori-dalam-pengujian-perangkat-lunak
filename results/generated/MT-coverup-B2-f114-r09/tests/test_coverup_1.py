# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

"""Tests for f114.minSubArraySum.

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or fixture-based cleanup is required; each test simply
calls the function with fresh literal inputs, leaving no state behind.

Branch coverage achieved:
- Lines 3-9: loop body executes in every test.
- Line 7 True / line 8 (s < 0 -> s = 0): exercised by all-positive,
  mixed-sign, and single-positive-element inputs.
- Line 7 False (s >= 0, accumulate): exercised by all-negative and
  mixed-sign inputs.
- Line 10 True / line 11 (max_sum == 0 fallback): exercised by
  all-positive and single-positive-element inputs.
- Line 10 False (max_sum > 0, fallback skipped): exercised by
  all-negative and mixed-sign inputs.
"""

import pytest

from f114 import minSubArraySum


def test_min_sub_array_sum_all_positive_hits_fallback_branch():
    # With all-positive numbers every running sum goes negative and is
    # reset to 0, so max_sum stays 0 and the fallback on line 11 runs.
    # The minimum subarray of positives is its smallest single element.
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1


def test_min_sub_array_sum_all_negative_hits_accumulate_branch():
    # With all-negative numbers s never drops below 0, so the reset
    # branch (line 8) is skipped, max_sum ends up positive, and the
    # fallback on line 11 is NOT taken. The minimum subarray is the
    # whole array.
    assert minSubArraySum([-1, -2, -3]) == -6


def test_min_sub_array_sum_mixed_signs_exercises_both_branches():
    # Mixed signs make the running sum both reset (s < 0) and
    # accumulate (s >= 0); the fallback is skipped because max_sum > 0.
    # Best (most negative) subarray here is [-1, -2] == -3.
    assert minSubArraySum([2, -1, -2, 4]) == -3


def test_min_sub_array_sum_single_positive_element():
    # Single positive element: reset branch taken, fallback taken.
    assert minSubArraySum([5]) == 5


def test_min_sub_array_sum_single_negative_element():
    # Single negative element: reset branch skipped, fallback skipped.
    assert minSubArraySum([-7]) == -7


def test_min_sub_array_sum_returns_int_for_int_input():
    # Postcondition: result is an int when the input consists of ints.
    result = minSubArraySum([1, -2, 3])
    assert isinstance(result, int)
    assert result == -2
