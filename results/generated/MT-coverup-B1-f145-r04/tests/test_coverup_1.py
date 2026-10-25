# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

from f145 import order_by_points


def test_order_by_points_covers_positive_and_negative_numbers():
    nums = [12, -12, 1, -1, 0]
    original = nums.copy()

    result = order_by_points(nums)

    assert result == [-1, 0, -12, 1, 12]
    assert nums == original
