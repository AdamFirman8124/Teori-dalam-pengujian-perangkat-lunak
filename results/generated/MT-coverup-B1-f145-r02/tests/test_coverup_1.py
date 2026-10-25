# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

from f145 import order_by_points


def test_order_by_points_mixed_signs():
    nums = [12, -12, 100, -10, 0, 3]
    # digits_sum: 12->3, -12->-1+2=1, 100->1, -10->-1+0=-1, 0->0, 3->3
    result = order_by_points(nums)
    assert result == [-10, 0, -12, 100, 12, 3]
    # postcondition: returns new sorted list, input not mutated
    assert nums == [12, -12, 100, -10, 0, 3]
    assert result is not nums


def test_order_by_points_negative_and_positive_branches():
    # digits_sum: -99->-9+9=0, -10->-1+0=-1, 10->1+0=1, 99->9+9=18
    assert order_by_points([-99, -10, 10, 99]) == [-10, -99, 10, 99]
    # minimal both-branch case: 5->5, -5->-5
    assert order_by_points([5, -5]) == [-5, 5]
    # stability check: 12->3, 3->3, 21->3 keep original order; 100->1 first
    assert order_by_points([12, 100, 3, 21]) == [100, 12, 3, 21]
