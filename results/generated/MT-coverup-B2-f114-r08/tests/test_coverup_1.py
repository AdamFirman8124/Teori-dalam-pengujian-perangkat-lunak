# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

import pytest

from f114 import minSubArraySum


def test_min_sub_array_sum_mixed_hits_reset_branch_and_zero_max_branch():
    # Every prefix sum goes negative (s < 0 True branch, line 8) and
    # max_sum stays 0, so the `max_sum == 0` True branch (line 11) runs.
    # The minimum subarray sum of [2, 3, 4, 1, 2, 4] is the single element 1.
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([5]) == 5


def test_min_sub_array_sum_mixed_hits_both_s_branches_and_nonzero_max():
    # [1, -2, 3]: s goes negative (reset branch), then positive (s < 0 False
    # branch), then negative again; max_sum ends at 2, so the
    # `max_sum == 0` False branch is taken and line 11 is skipped.
    assert minSubArraySum([1, -2, 3]) == -2


def test_min_sub_array_sum_all_negative_never_resets():
    # All-negative input: s never drops below 0, so only the False branch of
    # `s < 0` executes, and max_sum != 0 so line 11 is skipped.
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([-5]) == -5


def test_min_sub_array_sum_all_positive_uses_negated_max():
    # All-positive input: s is reset to 0 every iteration, max_sum stays 0,
    # and the fallback `max(-i for i in nums)` (line 11) produces the answer.
    assert minSubArraySum([1, 2, 3]) == 1


def test_min_sub_array_sum_empty_input_raises():
    # With no elements the loop body never runs, max_sum stays 0, and the
    # fallback max() over an empty sequence raises ValueError.
    with pytest.raises(ValueError):
        minSubArraySum([])
