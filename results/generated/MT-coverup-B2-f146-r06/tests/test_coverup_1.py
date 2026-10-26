# file: project/f146/__init__.py:1-12
# asked: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

from f146 import specialFilter


def test_empty_list():
    assert specialFilter([]) == 0


def test_all_numbers_le_10_ignored():
    assert specialFilter([0, 1, 5, 10, -3, 10, 9]) == 0


def test_first_digit_even_not_counted():
    # 22, 20, 42, 68: num > 10 True, first digit even -> inner if False
    assert specialFilter([22, 20, 42, 68, 200]) == 0


def test_first_odd_last_even_not_counted():
    # first digit odd True, last digit even False -> inner if False
    assert specialFilter([12, 14, 16, 32, 38, 50, 100]) == 0


def test_both_ends_odd_counted():
    assert specialFilter([11, 13, 15, 31, 33, 55, 77, 99, 111, 135]) == 10


def test_mixed_only_counts_gt10_with_odd_first_and_last():
    # 5 (<=10 ignored), 11 (count), 22 (first even, no count),
    # 12 (last even, no count), 15 (count), 10 (ignored), 33 (count), 42 (no count)
    assert specialFilter([5, 11, 22, 12, 15, 10, 33, 42]) == 3
