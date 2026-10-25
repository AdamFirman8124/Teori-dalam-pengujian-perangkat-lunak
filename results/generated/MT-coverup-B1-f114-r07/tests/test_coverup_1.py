# file: project/f114/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "branches": [[5, 6], [5, 10], [7, 8], [7, 9], [10, 11], [10, 12]]}

from f114 import minSubArraySum


def test_min_subarray_sum_with_mixed_values():
    nums = [-2, 3, -4]
    original = nums.copy()

    assert minSubArraySum(nums) == -4
    assert nums == original


def test_min_subarray_sum_with_all_positive_values():
    nums = [3, 1, 2]
    original = nums.copy()

    assert minSubArraySum(nums) == 1
    assert nums == original
