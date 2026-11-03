# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f088 import sort_array


def test_sort_array_empty():
    """Empty input should return an empty list (covers the len == 0 branch)."""
    assert sort_array([]) == []


def test_sort_array_even_sum_reversed():
    """When first + last is even, the array must be sorted in descending order."""
    result = sort_array([2, 4, 1, 6])
    # first + last = 2 + 6 = 8 (even) -> reverse=True
    assert result == [6, 4, 2, 1]
    assert sorted(result, reverse=True) == result


def test_sort_array_odd_sum_ascending():
    """When first + last is odd, the array must be sorted in ascending order."""
    result = sort_array([3, 1, 2])
    # first + last = 3 + 2 = 5 (odd) -> reverse=False
    assert result == [1, 2, 3]
    assert sorted(result) == result


def test_sort_array_single_element():
    """A single element yields itself regardless of parity branch taken."""
    assert sort_array([7]) == [7]


def test_sort_array_even_sum_with_duplicates():
    """Even sum branch with duplicates and negatives still sorts descending."""
    result = sort_array([-4, 0, 8, 4])
    # first + last = -4 + 4 = 0 (even) -> reverse=True
    assert result == [8, 4, 0, -4]
