# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

import pytest

from f114 import minSubArraySum


def test_mixed_values_covers_reset_branch_and_nonzero_max_sum():
    # Negated running sums: -1 (reset to 0), 2, -1 (reset to 0) -> max_sum = 2.
    # Exercises lines 3-9 including the `s < 0` reset branch (line 8),
    # and takes the False branch of `if max_sum == 0` (skips line 11).
    assert minSubArraySum([1, -2, 3]) == -2


def test_all_negative_values_no_reset_nonzero_max_sum():
    # All negated values are positive, so `s < 0` never triggers (False branch
    # of line 7); max_sum != 0 so line 11 is skipped again.
    assert minSubArraySum([-1, -2, -3]) == -6


def test_all_positive_values_covers_zero_max_sum_branch():
    # All negated values are negative, so s stays 0 and max_sum == 0,
    # executing lines 10-11 (max over negated elements).
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1


def test_single_element_cases():
    # [5]: negated -5 triggers the reset branch and the max_sum == 0 branch.
    assert minSubArraySum([5]) == 5
    # [-5]: negated 5 never resets and max_sum != 0.
    assert minSubArraySum([-5]) == -5


def test_empty_list_raises_value_error():
    # With no elements the loop body never runs, max_sum stays 0, and
    # max(-i for i in nums) over an empty sequence raises ValueError.
    with pytest.raises(ValueError):
        minSubArraySum([])
