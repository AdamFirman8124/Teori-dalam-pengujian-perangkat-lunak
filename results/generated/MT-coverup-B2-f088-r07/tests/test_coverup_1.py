# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f088 import sort_array


def test_sort_array_empty_returns_empty_list():
    """Covers the len(array) == 0 branch of the conditional expression."""
    assert sort_array([]) == []


def test_sort_array_even_sum_sorted_descending():
    """Covers the non-empty branch with (array[0]+array[-1]) % 2 == 0 -> reverse=True."""
    # 1 + 3 = 4 (even) -> descending order
    assert sort_array([1, 2, 3]) == [3, 2, 1]


def test_sort_array_odd_sum_sorted_ascending():
    """Covers the non-empty branch with (array[0]+array[-1]) % 2 != 0 -> reverse=False."""
    # 2 + 3 = 5 (odd) -> ascending order
    assert sort_array([2, 1, 3]) == [1, 2, 3]


def test_sort_array_single_element_even_sum():
    """Single element: array[0] + array[-1] is even (2*x), reverse=True is a no-op."""
    assert sort_array([5]) == [5]


def test_sort_array_negative_numbers_odd_sum():
    """Negative values: -1 + 0 = -1, and -1 % 2 == 1 (odd) -> ascending order."""
    assert sort_array([-1, 0]) == [-1, 0]


def test_sort_array_does_not_mutate_input():
    """Postcondition: the input list is left unchanged (function is pure)."""
    original = [3, 1, 2]
    snapshot = list(original)
    sort_array(original)
    assert original == snapshot
