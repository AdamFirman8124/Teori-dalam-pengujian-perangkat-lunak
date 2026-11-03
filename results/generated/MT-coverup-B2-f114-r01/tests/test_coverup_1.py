# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

"""Tests for f114.minSubArraySum (HumanEval/114).

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or cleanup is required; each test is fully self-contained.

Coverage targets:
- lines 3-4:  initialization of max_sum / s
- lines 5-6:  loop body accumulating -num
- lines 7-8:  the ``s < 0`` reset branch (taken with positive numbers,
              not taken with negative numbers)
- line 9:     max_sum update inside the loop
- lines 10-11: the ``max_sum == 0`` fallback branch (taken when all
              numbers are positive, not taken when any subarray sum is
              negative)
- lines 12-13: final negation and return
"""

import pytest

from f114 import minSubArraySum


def test_negative_numbers_take_s_negative_branch_and_skip_fallback():
    # With all-negative input, s never drops below 0 (line 8 not taken)
    # and max_sum ends non-zero, so line 11 is not executed.
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([-1, -2, -3, 4]) == -6
    assert minSubArraySum([-1]) == -1


def test_positive_numbers_take_reset_branch_and_fallback_branch():
    # With all-positive input, s goes negative on every iteration
    # (line 8 taken) and max_sum stays 0, so line 11 executes.
    assert minSubArraySum([1, 2, 3]) == 1
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([5]) == 5


def test_mixed_input_covers_both_branches_of_loop():
    # Mixed input exercises the loop with s both negative (reset) and
    # positive (kept), and the non-zero max_sum path.
    assert minSubArraySum([1, -2, 3, -1, 2]) == -2
    assert minSubArraySum([3, -4, 1, -1, 2]) == -4


def test_zero_input():
    # A single zero: s stays 0 (line 8 not taken), max_sum == 0 so the
    # fallback runs and yields 0.
    assert minSubArraySum([0]) == 0
