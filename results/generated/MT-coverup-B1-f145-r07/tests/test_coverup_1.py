# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

from f145 import order_by_points


def test_order_by_points_handles_positive_negative_and_zero():
    nums = [12, -12, 0, -5, 21]
    original = nums.copy()

    result = order_by_points(nums)

    assert result == [-5, 0, -12, 12, 21]
    assert nums == original
    assert result is not nums
