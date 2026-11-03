# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

from f145 import order_by_points


def test_order_by_points_positive_numbers():
    """Covers lines 3-9 via the `n < 0` False branch of digits_sum."""
    # digit sums: 1 -> 1, 2 -> 2, 11 -> 2 (stable sort keeps 11 before 2)
    assert order_by_points([1, 2, 11]) == [1, 2, 11]
    # digit sums: 56 -> 11, 65 -> 11, 12 -> 3
    assert order_by_points([56, 65, 12]) == [12, 56, 65]


def test_order_by_points_negative_numbers():
    """Covers the `n < 0` True branch on line 5."""
    # digit sums: 1 -> 1, 11 -> 2, -1 -> -1, -11 -> 0, -12 -> 1
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    # digit sums: -45 -> 1, 123 -> 6, 0 -> 0
    assert order_by_points([-45, 123, 0]) == [0, -45, 123]


def test_order_by_points_empty_list():
    """Covers line 9 with an empty input."""
    assert order_by_points([]) == []


def test_order_by_points_does_not_mutate_input():
    """Postcondition: the input list is left untouched (function is pure)."""
    nums = [3, -1, 2]
    result = order_by_points(nums)
    assert nums == [3, -1, 2]
    assert result == [-1, 2, 3]
