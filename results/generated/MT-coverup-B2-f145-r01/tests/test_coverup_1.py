# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

from f145 import order_by_points


def test_order_by_points_empty_list():
    """Covers line 9 (sorted call) with an empty input list."""
    assert order_by_points([]) == []


def test_order_by_points_mixed_signs():
    """Covers all lines: line 5 false branch (positives) and true branch (negatives),
    lines 6-8 (digit extraction, sign application, sum) and line 9 (sort)."""
    # digits_sum: 1->1, 11->2, -1->-1, -11->0, -12->1
    # keys 1 and -12 tie; stable sort keeps original relative order (1 before -12)
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]


def test_order_by_points_all_negative():
    """Covers the true branch of line 5 for every element."""
    # digits_sum: -3->-3, -12->1, -1->-1
    assert order_by_points([-3, -12, -1]) == [-3, -1, -12]


def test_order_by_points_all_positive():
    """Covers the false branch of line 5 for every element."""
    # digits_sum: 32->5, 2->2, 14->5
    assert order_by_points([32, 2, 14]) == [2, 32, 14]


def test_order_by_points_stability_on_ties():
    """Equal digit sums preserve original order (sorted is stable)."""
    # digits_sum: 12->3, 3->3, 21->3
    assert order_by_points([12, 3, 21]) == [12, 3, 21]


def test_order_by_points_zero_and_single_digits():
    """Covers zero and single-digit positive/negative handling."""
    # digits_sum: 0->0, 9->9, -9->-9
    assert order_by_points([0, 9, -9]) == [-9, 0, 9]


def test_order_by_points_does_not_mutate_input():
    """Verifies the function returns a new sorted list without mutating the input."""
    nums = [3, -1, 2]
    result = order_by_points(nums)
    assert result == [-1, 2, 3]
    assert nums == [3, -1, 2]
    assert result is not nums
