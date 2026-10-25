# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

import pytest

from f145 import order_by_points


def _reference_digits_sum(n):
    neg = 1
    if n < 0:
        n, neg = -1 * n, -1
    digits = [int(i) for i in str(n)]
    digits[0] = digits[0] * neg
    return sum(digits)


def test_order_by_points_positive_numbers():
    nums = [30, 11, 2]
    result = order_by_points(nums)

    assert result == [11, 2, 30]
    assert sorted(result) == sorted(nums)
    assert [_reference_digits_sum(x) for x in result] == sorted(
        _reference_digits_sum(x) for x in nums
    )


def test_order_by_points_negative_numbers():
    nums = [-12, 5, -3]
    result = order_by_points(nums)

    # keys: -12 -> 1, 5 -> 5, -3 -> -3
    assert result == [-3, -12, 5]
    assert sorted(result) == sorted(nums)
    assert [_reference_digits_sum(x) for x in result] == sorted(
        _reference_digits_sum(x) for x in nums
    )


def test_order_by_points_single_negative():
    assert order_by_points([-7]) == [-7]


def test_order_by_points_zero_and_negative():
    assert order_by_points([0, -5]) == [-5, 0]


def test_order_by_points_empty_list():
    assert order_by_points([]) == []


def test_order_by_points_is_stable_for_equal_keys():
    nums = [21, 12]
    result = order_by_points(nums)

    assert result == [21, 12]
    assert _reference_digits_sum(21) == _reference_digits_sum(12)


def test_order_by_points_does_not_mutate_input():
    nums = [-12, 5, -3]
    original = list(nums)

    order_by_points(nums)

    assert nums == original
