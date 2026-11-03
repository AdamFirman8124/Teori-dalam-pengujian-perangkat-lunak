# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

import pytest

from f145 import order_by_points


def test_order_by_points_mixed_signs():
    """Covers both branches of the inner digits_sum (n < 0 true and false).

    Digit sums: 1 -> 1, 11 -> 2, -1 -> -1, -11 -> 0, -12 -> (-1 + 2) = 1.
    """
    nums = [1, 11, -1, -11, -12]
    result = order_by_points(nums)
    assert result == [-1, -11, 1, -12, 11]


def test_order_by_points_negative_multi_digit():
    """First digit of a negative number is negated: -123 -> -1 + 2 + 3 = 4."""
    nums = [123, -123]
    result = order_by_points(nums)
    assert result == [-123, 123]  # 4 < 6


def test_order_by_points_zero_and_singles():
    """Covers n == 0 and single-digit inputs on both branches."""
    assert order_by_points([0, -1, 1]) == [-1, 0, 1]
    assert order_by_points([7]) == [7]
    assert order_by_points([-7]) == [-7]


def test_order_by_points_empty_list():
    assert order_by_points([]) == []


def test_order_by_points_stable_for_ties():
    """Equal digit sums keep original relative order (sorted is stable)."""
    assert order_by_points([12, 21]) == [12, 21]   # both digit sum 3
    assert order_by_points([21, 12]) == [21, 12]
    assert order_by_points([-56, 10]) == [-56, 10]  # -5 + 6 == 1 == 1 + 0


def test_order_by_points_does_not_mutate_input():
    """sorted() must return a new list; the input stays untouched."""
    nums = [3, -30, 12]
    snapshot = list(nums)
    result = order_by_points(nums)
    assert nums == snapshot
    assert result is not nums
    assert result == [-30, 3, 12]  # keys: 3, -3, 3 -> -30 first, then 3, 12
