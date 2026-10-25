

# Generated at 2026-10-25 04:09:50.689422
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

# Generated at 2026-10-25 04:09:55.948441
# Unit test for function minSubArraySum
def test_minSubArraySum():assert module_0.minSubArraySum([3, -4, 2, -3, -1, 7, -5]) == -6

# Generated at 2026-10-25 04:09:58.489127
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:10:00.904514
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:10:03.320559
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:10:05.908252
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:10:08.323790
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:10:10.740202
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:10:13.155895
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:10:15.573924
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:10:17.987986
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:10:20.405788
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:10:22.822038
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:10:25.416620
# Unit test for function minSubArraySum