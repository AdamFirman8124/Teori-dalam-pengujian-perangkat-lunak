# file: script_33.py:1-12
# asked: {"lines": [10, 11, 12], "branches": []}
# gained: {"lines": [10, 11, 12], "branches": []}

import pytest
from script_33 import sort_third


def test_sort_third_basic():
    """Test basic functionality with a simple list."""
    result = sort_third([1, 2, 3])
    assert result == [1, 2, 3]


def test_sort_third_longer_list():
    """Test with a longer list where sorting at indices divisible by 3 matters."""
    result = sort_third([5, 6, 3, 4, 8, 9, 2])
    assert result == [2, 6, 3, 4, 8, 9, 5]


def test_sort_third_empty_list():
    """Test with an empty list."""
    result = sort_third([])
    assert result == []


def test_sort_third_single_element():
    """Test with a single element list."""
    result = sort_third([42])
    assert result == [42]


def test_sort_third_two_elements():
    """Test with two elements (only index 0 is divisible by 3)."""
    result = sort_third([9, 5])
    assert result == [9, 5]


def test_sort_third_unsorted_at_divisible_indices():
    """Test where elements at indices 0, 3, 6 need sorting."""
    result = sort_third([9, 1, 2, 3, 4, 5, 6, 7, 8])
    assert result == [3, 1, 2, 6, 4, 5, 9, 7, 8]


def test_sort_third_negative_numbers():
    """Test with negative numbers."""
    result = sort_third([-5, 10, -3, 2, 8, -1, 7])
    assert result == [-5, 10, -3, 2, 8, -1, 7]


def test_sort_third_duplicate_values():
    """Test with duplicate values at divisible indices."""
    result = sort_third([5, 1, 2, 5, 4, 6, 5, 8, 9])
    assert result == [5, 1, 2, 5, 4, 6, 5, 8, 9]


def test_sort_third_tuple_input():
    """Test that function works with tuple input and returns a list."""
    result = sort_third((5, 6, 3, 4, 8, 9, 2))
    assert result == [2, 6, 3, 4, 8, 9, 5]
    assert isinstance(result, list)


def test_sort_third_does_not_modify_original():
    """Test that the original list is not modified."""
    original = [5, 6, 3, 4, 8, 9, 2]
    original_copy = original.copy()
    result = sort_third(original)
    assert original == original_copy
    assert result == [2, 6, 3, 4, 8, 9, 5]
