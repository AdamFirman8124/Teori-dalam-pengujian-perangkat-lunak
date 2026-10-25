# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

from f146 import specialFilter


def test_special_filter_counts_only_numbers_with_odd_first_and_last_digits():
    nums = [9, 10, 11, 12, 13, 22, 31, 35, 97]

    result = specialFilter(nums)

    assert result == 5


def test_special_filter_returns_zero_for_empty_input():
    assert specialFilter([]) == 0
