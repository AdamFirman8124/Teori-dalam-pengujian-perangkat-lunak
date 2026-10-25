# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

from f114 import minSubArraySum
import pytest


def test_all_positive_returns_smallest_element():
    nums = [2, 3, 4, 1, 2, 4]
    snapshot = list(nums)
    assert minSubArraySum(nums) == 1
    assert nums == snapshot


def test_single_positive_covers_reset_and_zero_max():
    nums = [5]
    snapshot = list(nums)
    assert minSubArraySum(nums) == 5
    assert nums == snapshot


def test_single_negative_covers_no_reset():
    nums = [-5]
    snapshot = list(nums)
    assert minSubArraySum(nums) == -5
    assert nums == snapshot


def test_single_zero_covers_boundary_s_equals_zero():
    nums = [0]
    snapshot = list(nums)
    assert minSubArraySum(nums) == 0
    assert nums == snapshot


def test_all_negative_returns_total_sum():
    nums = [-2, -3, -1, -5]
    snapshot = list(nums)
    assert minSubArraySum(nums) == -11
    assert nums == snapshot


def test_mixed_covers_both_reset_branches_and_nonzero_max():
    nums = [1, -2, 3, -4, 5, -6]
    snapshot = list(nums)
    assert minSubArraySum(nums) == -6
    assert nums == snapshot


def test_mixed_with_zero_min():
    nums = [0, 5]
    snapshot = list(nums)
    assert minSubArraySum(nums) == 0
    assert nums == snapshot


def test_empty_covers_zero_iterations_branch():
    with pytest.raises(ValueError):
        minSubArraySum([])
