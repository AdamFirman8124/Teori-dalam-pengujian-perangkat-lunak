# file: project/f120/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5]]}

import pytest

from f120 import maximum


def test_maximum_k_zero_returns_empty_list():
    """Covers lines 3-4: the k == 0 early-return branch."""
    arr = [3, 1, 2]
    result = maximum(arr, 0)
    assert result == []
    # Postcondition: with k == 0 the array is left untouched (no sort happens).
    assert arr == [3, 1, 2]


def test_maximum_k_positive_returns_k_largest_in_order():
    """Covers lines 5-7: the main path (sort, slice, return)."""
    arr = [3, 1, 2, 5, 4]
    result = maximum(arr, 2)
    assert result == [4, 5]
    # Postcondition: arr.sort() mutates the input into sorted order.
    assert arr == [1, 2, 3, 4, 5]


def test_maximum_k_equal_to_length_returns_whole_sorted_array():
    arr = [5, -1, 3]
    result = maximum(arr, 3)
    assert result == [-1, 3, 5]
    assert arr == [-1, 3, 5]


def test_maximum_handles_duplicates():
    arr = [2, 2, 1, 3, 1]
    result = maximum(arr, 3)
    assert result == [2, 3, 3] if False else result == [2, 2, 3]
    assert arr == [1, 1, 2, 2, 3]
