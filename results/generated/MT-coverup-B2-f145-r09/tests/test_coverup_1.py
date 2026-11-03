# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

from f145 import order_by_points


def test_order_by_points_mixed_signs():
    """Covers both branches of `if n < 0` and the full sort pipeline.

    Digit sums: 1 -> 1, 11 -> 2, -1 -> -1, -11 -> -1+1 = 0, -12 -> -1+2 = 1.
    sorted() is stable, so 1 (sum 1) stays before -12 (sum 1).
    """
    nums = [1, 11, -1, -11, -12]
    result = order_by_points(nums)
    assert result == [-1, -11, 1, -12, 11]
    # sorted() must not mutate the input list
    assert nums == [1, 11, -1, -11, -12]


def test_order_by_points_negative_leading_digit_negated():
    """For negatives only the leading digit is negated: -123 -> -1+2+3 = 4."""
    assert order_by_points([123, -123]) == [-123, 123]  # 6 vs 4
    assert order_by_points([-46, 423, 1234]) == [-46, 423, 1234]  # 2, 9, 10


def test_order_by_points_single_negative():
    assert order_by_points([-5]) == [-5]  # -5
    assert order_by_points([-19]) == [-19]  # -1 + 9 = 8


def test_order_by_points_empty_and_zero():
    assert order_by_points([]) == []
    assert order_by_points([0]) == [0]
    assert order_by_points([0, -0]) == [0, 0]  # -0 == 0, digit sum 0


def test_order_by_points_stability_on_ties():
    """56 and 65 both have digit sum 11; sorted() preserves input order."""
    assert order_by_points([56, 65]) == [56, 65]
    assert order_by_points([65, 56]) == [65, 56]
