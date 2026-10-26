# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

from f146 import specialFilter


def test_special_filter_empty_list_returns_zero():
    assert specialFilter([]) == 0


def test_special_filter_all_values_at_or_below_ten_are_skipped():
    nums = [1, 9, 10, 0, -15, -33]
    assert specialFilter(nums) == 0


def test_special_filter_counts_numbers_with_odd_first_and_last_digits():
    nums = [15, 33, 1421, 1, 22, 13]
    assert specialFilter(nums) == 4


def test_special_filter_rejects_even_first_or_last_digit():
    nums = [21, 12, 100, 24, 46, 20]
    assert specialFilter(nums) == 0


def test_special_filter_mixed_input_counts_only_matching_numbers():
    nums = [11, 12, 21, 22, 99, 100, 101, 111, 1001, 10]
    assert specialFilter(nums) == 5


def test_special_filter_does_not_mutate_input():
    nums = [15, 22, 33]
    original = list(nums)
    specialFilter(nums)
    assert nums == original


def test_special_filter_accepts_tuple_input():
    assert specialFilter((15, 22, 33)) == 2
