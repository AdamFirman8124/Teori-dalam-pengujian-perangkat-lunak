

# Generated at 2026-10-25 03:50:57.979574
# Unit test for function minSubArraySum
def test_minSubArraySum():import random
import pytest


@pytest.mark.parametrize("nums, expected", [
    ([1], 1),
    ([-1], -1),
    ([0], 0),
    ([1, 2, 3], 1),
    ([-1, -2, -3], -6),
    ([2, -1], -1),
    ([-2, 1], -2),
    ([0, 0], 0),
    ([3, -4, 2, -1, 6], -4),
])
def test_minSubArraySum(nums, expected):
    assert module_0.minSubArraySum(nums) == expected


def brute_min_subarray_sum(nums):
    return min(
        sum(nums[i:j])
        for i in range(len(nums))
        for j in range(i + 1, len(nums) + 1)
    )


def test_minSubArraySum_random_against_bruteforce():
    for _ in range(1000):
        nums = [random.randint(-10, 10) for _ in range(random.randint(1, 12))]
        assert module_0.minSubArraySum(nums) == brute_min_subarray_sum(nums)

# Generated at 2026-10-25 03:51:03.780820
# Unit test for function minSubArraySum
def test_minSubArraySum():assert module_0.minSubArraySum([3, -4, 2, -3, -1, 7, -5]) == -6

# Generated at 2026-10-25 03:51:06.199632
# Unit test for function minSubArraySum

# Generated at 2026-10-25 03:51:08.770638
# Unit test for function minSubArraySum

# Generated at 2026-10-25 03:51:11.185397
# Unit test for function minSubArraySum

# Generated at 2026-10-25 03:51:13.600488
# Unit test for function minSubArraySum

# Generated at 2026-10-25 03:51:16.015394
# Unit test for function minSubArraySum

# Generated at 2026-10-25 03:51:18.430997
# Unit test for function minSubArraySum

# Generated at 2026-10-25 03:51:20.847245
# Unit test for function minSubArraySum

# Generated at 2026-10-25 03:51:23.262716
# Unit test for function minSubArraySum

# Generated at 2026-10-25 03:51:25.678995
# Unit test for function minSubArraySum

# Generated at 2026-10-25 03:51:28.093291
# Unit test for function minSubArraySum

# Generated at 2026-10-25 03:51:30.507896
# Unit test for function minSubArraySum

# Generated at 2026-10-25 03:51:32.923123
# Unit test for function minSubArraySum