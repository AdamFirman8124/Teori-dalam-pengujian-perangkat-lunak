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
    """Test with a longer list requiring sorting."""
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
    """Test with two elements."""
    result = sort_third([10, 20])
    assert result == [10, 20]


def test_sort_third_all_positions_divisible_by_three():
    """Test with three elements at indices 0, 3, 6."""
    result = sort_third([9, 1, 2, 3, 4, 5, 1])
    assert result == [1, 1, 2, 3, 4, 5, 9]


def test_sort_third_negative_numbers():
    """Test with negative numbers at indices 0, 3, 6."""
    result = sort_third([-5, 10, -3, 20, -1, 30, -10])
    # Indices 0, 3, 6 have values: -5, 20, -10
    # Sorted: -10, -5, 20
    assert result == [-10, 10, -3, -5, -1, 30, 20]


def test_sort_third_does_not_modify_original():
    """Test that the original list is not modified."""
    original = [5, 6, 3, 4, 8, 9, 2]
    original_copy = original.copy()
    result = sort_third(original)
    assert original == original_copy
    assert result == [2, 6, 3, 4, 8, 9, 5]


def test_sort_third_with_tuple():
    """Test with a tuple input to ensure line 10 executes."""
    result = sort_third((5, 6, 3, 4, 8, 9, 2))
    assert result == [2, 6, 3, 4, 8, 9, 5]
    assert isinstance(result, list)


def test_sort_third_with_duplicates():
    """Test with duplicate values at indices divisible by 3."""
    result = sort_third([5, 1, 2, 5, 3, 4, 5])
    assert result == [5, 1, 2, 5, 3, 4, 5]
