# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

import pytest

from f120 import maximum


def test_maximum_k_zero_returns_empty_list():
    """Covers lines 3-4: the k == 0 branch returns an empty list."""
    arr = [3, 1, 2]
    result = maximum(arr, 0)
    assert result == []
    # No sorting should have happened for k == 0.
    assert arr == [3, 1, 2]


def test_maximum_returns_top_k_sorted_ascending():
    """Covers lines 3, 5, 6, 7: k > 0 sorts in place and returns last k elements."""
    arr = [5, -1, 3, 2, 8]
    result = maximum(arr, 3)
    assert result == [3, 5, 8]
    # arr.sort() mutates the input list in place.
    assert arr == [-1, 2, 3, 5, 8]


def test_maximum_k_equals_length_returns_fully_sorted():
    """Covers lines 5-7 with k == len(arr): the whole sorted list is returned."""
    arr = [2, 1, 3]
    result = maximum(arr, 3)
    assert result == [1, 2, 3]
    assert arr == [1, 2, 3]


def test_maximum_k_greater_than_length_returns_fully_sorted():
    """Covers lines 5-7 with k > len(arr): slicing clamps to the whole list."""
    arr = [2, 1]
    result = maximum(arr, 5)
    assert result == [1, 2]
    assert arr == [1, 2]


def test_maximum_with_duplicates_and_single_element():
    """Covers lines 5-7 with duplicates and a single-element list."""
    arr = [4, 4, 1, 4]
    result = maximum(arr, 2)
    assert result == [4, 4]
    assert arr == [1, 4, 4, 4]

    single = [7]
    assert maximum(single, 1) == [7]
    assert single == [7]
