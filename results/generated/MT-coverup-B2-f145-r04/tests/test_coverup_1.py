# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

from f145 import order_by_points


def test_order_by_points_positive_numbers():
    assert order_by_points([11, 1, 20]) == [1, 11, 20]
    assert order_by_points([]) == []
    assert order_by_points([5]) == [5]


def test_order_by_points_negative_numbers():
    # digits_sum(-11) == -1 + 1 == 0, digits_sum(1) == 1, digits_sum(11) == 2
    assert order_by_points([1, 11, -11]) == [-11, 1, 11]
    # digits_sum(-123) == -1 + 2 + 3 == 4
    assert order_by_points([-123, 4]) == [-123, 4]
    # digits_sum(-9) == -9, smallest of all
    assert order_by_points([9, -9, 0]) == [-9, 0, 9]


def test_order_by_points_mixed_and_stable():
    nums = [13, -13, 31, -31]
    # keys: 13 -> 4, -13 -> -1+3 == 2, 31 -> 4, -31 -> -3+1 == -2
    assert order_by_points(nums) == [-31, -13, 13, 31]
    # input list must not be mutated
    assert nums == [13, -13, 31, -31]
