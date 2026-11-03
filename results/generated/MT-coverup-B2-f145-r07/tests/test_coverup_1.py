# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

import pytest

from f145 import order_by_points


def test_order_by_points_mixed_signs_covers_both_branches():
    """Calling with positive and negative values executes every line of
    digits_sum, including both branches of ``if n < 0``."""
    nums = [1, 11, -1, -11, -12]
    # keys: 1 -> 1, 11 -> 2, -1 -> -1, -11 -> (-1 + 1) = 0, -12 -> (-1 + 2) = 1
    result = order_by_points(nums)
    assert result == [-1, -11, 1, -12, 11]
    # sorted() must not mutate its input (no state pollution)
    assert nums == [1, 11, -1, -11, -12]


def test_order_by_points_stable_sort_with_tied_keys():
    nums = [1234, 423, 463, 145, 2, 423, 423]
    # keys: 1234 -> 10, 423 -> 9, 463 -> 13, 145 -> 10, 2 -> 2
    # ties (423s, and 1234/145) keep their original relative order
    result = order_by_points(nums)
    assert result == [2, 423, 423, 423, 1234, 145, 463]
    assert nums == [1234, 423, 463, 145, 2, 423, 423]


def test_order_by_points_empty_list():
    assert order_by_points([]) == []


def test_order_by_points_all_negative_and_positive_mix():
    nums = [1, -11, -32, 43, 54, -6, -7]
    # keys: 1 -> 1, -11 -> 0, -32 -> (-3 + 2) = -1, 43 -> 7,
    #       54 -> 9, -6 -> -6, -7 -> -7
    result = order_by_points(nums)
    assert result == [-7, -6, -32, -11, 1, 43, 54]
    assert nums == [1, -11, -32, 43, 54, -6, -7]


def test_order_by_points_single_negative_element():
    # single negative value: first (only) digit is negated
    assert order_by_points([-5]) == [-5]
