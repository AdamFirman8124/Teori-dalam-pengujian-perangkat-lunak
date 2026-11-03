# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f088 import sort_array


def test_sort_array_empty():
    """Empty input returns an empty list (short-circuit branch)."""
    assert sort_array([]) == []


def test_sort_array_even_sum_descending():
    """When array[0] + array[-1] is even, result is sorted in descending order."""
    # 1 + 5 = 6 -> even -> reverse=True
    result = sort_array([1, 3, 2, 5])
    assert result == [5, 3, 2, 1]


def test_sort_array_odd_sum_ascending():
    """When array[0] + array[-1] is odd, result is sorted in ascending order."""
    # 2 + 5 = 7 -> odd -> reverse=False
    result = sort_array([2, 3, 1, 5])
    assert result == [1, 2, 3, 5]


def test_sort_array_single_element_even_sum():
    """Single element: first == last, sum is even -> reverse=True, single item unchanged."""
    assert sort_array([7]) == [7]
