

# Generated at 2026-10-25 04:51:43.924557
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

# Generated at 2026-10-25 04:51:50.297382
# Unit test for function minSubArraySum
def test_minSubArraySum():assert module_0.minSubArraySum([3, -4, 2, -3, -1, 7, -5]) == -6

# Generated at 2026-10-25 04:51:51.649998
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

# Generated at 2026-10-25 04:51:57.765504
# Unit test for function minSubArraySum
def test_minSubArraySum():assert module_0.minSubArraySum([3, -4, 2, -3, -1, 7, -5]) == -6

# Generated at 2026-10-25 04:51:59.200174
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

# Generated at 2026-10-25 04:52:05.807134
# Unit test for function minSubArraySum
def test_minSubArraySum():assert module_0.minSubArraySum([3, -4, 2, -3, -1, 7, -5]) == -6

# Generated at 2026-10-25 04:52:07.154358
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

# Generated at 2026-10-25 04:52:12.643560
# Unit test for function minSubArraySum
def test_minSubArraySum():assert module_0.minSubArraySum([3, -4, 2, -3, -1, 7, -5]) == -6

# Generated at 2026-10-25 04:52:15.075616
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:52:17.996177
# Unit test for function minSubArraySum

# Generated at 2026-10-25 04:52:20.407735
# Unit test for function minSubArraySum