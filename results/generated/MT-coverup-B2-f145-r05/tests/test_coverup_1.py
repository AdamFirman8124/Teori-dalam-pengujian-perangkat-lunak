# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

from f145 import order_by_points


def test_order_by_points_mixed_signs():
    """Covers both branches of the `if n < 0` check (lines 4-8).

    digits_sum: 1 -> 1, 11 -> 2, -1 -> -1, -11 -> 0, -12 -> 1
    (only the leading digit of a negative number is negated).
    Ties (1 and -12 both key 1) keep input order due to stable sort.
    """
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]


def test_order_by_points_negative_multi_digit():
    """Negative branch: leading digit negated, remaining digits positive."""
    # -19 -> -1 + 9 = 8 ; -91 -> -9 + 1 = -8
    assert order_by_points([-19, -91]) == [-91, -19]
    # -345 -> -3 + 4 + 5 = 6 ; -12 -> -1 + 2 = 1 ; -1 -> -1
    assert order_by_points([-345, -12, -1]) == [-1, -12, -345]


def test_order_by_points_positive_only():
    """Positive branch only: 1234 -> 10, 423 -> 9, 56 -> 11."""
    assert order_by_points([1234, 423, 56]) == [423, 1234, 56]


def test_order_by_points_empty():
    """Empty input: lines 3 and 9 execute, digits_sum is never invoked."""
    assert order_by_points([]) == []


def test_order_by_points_single_and_zero():
    """Single elements, including zero (n < 0 is False for 0)."""
    assert order_by_points([0]) == [0]
    assert order_by_points([5]) == [5]
    assert order_by_points([-7]) == [-7]


def test_order_by_points_stable_for_ties():
    """All keys equal (3); stable sort must preserve the input order."""
    assert order_by_points([21, 12, 3]) == [21, 12, 3]


def test_order_by_points_does_not_mutate_input():
    """sorted() must return a new list, leaving the input untouched."""
    nums = [3, -1, 2]
    result = order_by_points(nums)
    assert nums == [3, -1, 2]
    assert result == [-1, 2, 3]
    assert result is not nums
