# file: project/f145/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

"""Tests for f145.order_by_points.

Lines 3-9 (the entire body of order_by_points, including the nested
digits_sum and both outcomes of the `if n < 0` branch) are exercised here.

No cleanup/monkeypatching is required: the function is pure (it does not
mutate its input, touch globals, files, or any other external state), so
these tests cannot pollute state.
"""

from f145 import order_by_points


def test_order_by_points_mixed_positive_and_negative():
    # Covers: nested def (line 3), digits_sum body (lines 4-8) for BOTH
    # outcomes of the `if n < 0` branch (line 5), and `return sorted(...)`
    # (line 9).
    # Keys: 1 -> 1, 11 -> 2, -1 -> -1, -11 -> 0, 12 -> 3
    nums = [1, 11, -1, -11, 12]
    result = order_by_points(nums)
    assert result == [-1, -11, 1, 11, 12]
    assert result is not nums              # a new sorted list is returned
    assert nums == [1, 11, -1, -11, 12]    # input list is not mutated


def test_order_by_points_only_first_digit_negated_for_negatives():
    # For -123 the key is -(1) + 2 + 3 = 4 (only the first digit is
    # negated), while 5 has key 5; hence -123 sorts before 5 even though
    # its absolute digit sum (6) is larger.
    assert order_by_points([5, -123]) == [-123, 5]


def test_order_by_points_stable_on_equal_keys():
    # 56 and 65 both have digit sum 11; sorted() is stable, so their
    # original relative order must be preserved.
    assert order_by_points([56, 65, 12]) == [12, 56, 65]


def test_order_by_points_zero_and_negative_two_digit():
    # Keys: 0 -> 0, -10 -> -(1) + 0 = -1
    assert order_by_points([0, -10]) == [-10, 0]


def test_order_by_points_empty_list():
    assert order_by_points([]) == []
