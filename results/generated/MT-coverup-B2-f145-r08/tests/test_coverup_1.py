# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

from f145 import order_by_points


def test_order_by_points_with_nonnegative_numbers():
    nums = [123, 5, 10, 99, 20, 0]

    result = order_by_points(nums)

    assert result == [0, 10, 20, 5, 123, 99]
    assert nums == [123, 5, 10, 99, 20, 0]


def test_order_by_points_with_negative_numbers():
    nums = [-123, -5, -10, -99]

    result = order_by_points(nums)

    assert result == [-5, -10, -99, -123]
    assert nums == [-123, -5, -10, -99]
