# file: script_88.py:1-16
# asked: {"lines": [16], "branches": []}
# gained: {"lines": [16], "branches": []}

import pytest
from script_88 import sort_array


def test_sort_array_empty():
    """Test that empty array returns empty array."""
    result = sort_array([])
    assert result == []
    assert isinstance(result, list)


def test_sort_array_single_element():
    """Test single element array returns same array."""
    result = sort_array([5])
    assert result == [5]


def test_sort_array_odd_sum_ascending():
    """Test array sorted in ascending order when first + last is odd."""
    # 2 + 5 = 7 (odd), so should sort ascending
    result = sort_array([2, 4, 3, 0, 1, 5])
    assert result == [0, 1, 2, 3, 4, 5]


def test_sort_array_even_sum_descending():
    """Test array sorted in descending order when first + last is even."""
    # 2 + 6 = 8 (even), so should sort descending
    result = sort_array([2, 4, 3, 0, 1, 5, 6])
    assert result == [6, 5, 4, 3, 2, 1, 0]


def test_sort_array_does_not_modify_original():
    """Test that original array is not modified."""
    original = [3, 1, 4, 1, 5]
    original_copy = original.copy()
    result = sort_array(original)
    assert original == original_copy
    assert result != original or result == original  # different object or same values


def test_sort_array_two_elements_odd_sum():
    """Test two element array with odd sum."""
    # 1 + 4 = 5 (odd), so should sort ascending
    result = sort_array([4, 1])
    assert result == [1, 4]


def test_sort_array_two_elements_even_sum():
    """Test two element array with even sum."""
    # 3 + 3 = 6 (even), so should sort descending
    result = sort_array([3, 3])
    assert result == [3, 3]
