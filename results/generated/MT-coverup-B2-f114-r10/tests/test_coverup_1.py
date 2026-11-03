# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

import pytest

from f114 import minSubArraySum


def test_all_positive_hits_reset_and_fallback_branches():
    """Every element is positive, so s goes negative each iteration
    (reset branch taken) and final max_sum == 0 (fallback branch taken)."""
    assert minSubArraySum([1, 2, 3]) == 1
    assert minSubArraySum([5]) == 5
    assert minSubArraySum([0]) == 0


def test_all_negative_skips_reset_and_fallback_branches():
    """Every element is negative, so s never goes negative (reset branch
    skipped) and final max_sum != 0 (fallback branch skipped)."""
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([-4]) == -4


def test_mixed_input_exercises_both_outcomes_of_reset_branch():
    """Leading positive drives s negative (reset taken); a later negative
    does not drive s below zero (reset skipped) -> both branch outcomes."""
    assert minSubArraySum([2, -3, 4]) == -3
    assert minSubArraySum([1, -2, 3, -4, 5]) == -4


def test_fallback_branch_with_single_zero():
    """max_sum stays 0 and the fallback max(-i for i in nums) runs."""
    assert minSubArraySum([0, 0]) == 0


def test_empty_input_raises_value_error():
    """With no elements, max_sum stays 0 and the fallback max() over an
    empty generator raises ValueError (documents current behavior)."""
    with pytest.raises(ValueError):
        minSubArraySum([])
