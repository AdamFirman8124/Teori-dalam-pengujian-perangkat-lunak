# file: project/f108/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}

import pytest

from f108 import count_nums


def test_count_nums_empty_array():
    """An empty array should yield a count of 0."""
    assert count_nums([]) == 0


def test_count_nums_positive_numbers():
    """All positive numbers have positive digit sums and are counted."""
    assert count_nums([1, 1, 2]) == 3


def test_count_nums_negative_single_digit():
    """A single-digit negative number has a negative digit sum (-1) and is not counted."""
    assert count_nums([-1]) == 0


def test_count_nums_negative_multi_digit():
    """A multi-digit negative number like -12 has digit sum -1 + 2 = 1 > 0, so it is counted."""
    assert count_nums([-12]) == 1


def test_count_nums_mixed_signs():
    """Mix of positives, negatives, and zero: only positive digit sums count."""
    # -1 -> -1 (not counted), 11 -> 2 (counted), -11 -> -1 + 1 = 0 (not counted)
    assert count_nums([-1, 11, -11]) == 1
    # 0 -> 0 (not counted), 1 -> 1 (counted)
    assert count_nums([0, 1]) == 1
    # -12 -> 1 (counted), 5 -> 5 (counted)
    assert count_nums([-12, 5]) == 2


def test_count_nums_all_non_positive_sums():
    """Numbers whose digit sums are zero or negative are never counted."""
    # -1 -> -1, -11 -> 0, 0 -> 0
    assert count_nums([-1, -11, 0]) == 0
