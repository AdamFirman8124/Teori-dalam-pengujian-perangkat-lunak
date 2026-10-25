

# Generated at 2026-10-25 04:00:01.427535
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

# Generated at 2026-10-25 04:00:07.452112
# Unit test for function minSubArraySum
def test_minSubArraySum():assert module_0.minSubArraySum([3, -4, 2, -3, -1, 7, -5]) == -6

# Generated at 2026-10-25 04:00:08.887628
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

# Generated at 2026-10-25 04:00:13.912965
# Unit test for function minSubArraySum
def test_minSubArraySum():assert module_0.minSubArraySum([3, -4, 2, -3, -1, 7, -5]) == -6

# Generated at 2026-10-25 04:00:15.354090
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

# Generated at 2026-10-25 04:00:20.159392
# Unit test for function minSubArraySum
def test_minSubArraySum():assert module_0.minSubArraySum([3, -4, 2, -3, -1, 7, -5]) == -6

# Generated at 2026-10-25 04:00:22.199958
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

# Generated at 2026-10-25 04:00:24.853611
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:00:27.386173
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:00:29.933008
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:00:32.352472
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:00:34.767044
# Unit test for function minSubArraySum