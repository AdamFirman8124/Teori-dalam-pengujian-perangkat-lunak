# file: script_37.py:1-18
# asked: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[14, 15], [14, 16], [16, 17], [16, 18]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[14, 15], [14, 16], [16, 17], [16, 18]]}

import pytest
from script_37 import sort_even


def test_sort_even_empty_list():
    """Test with empty list."""
    result = sort_even([])
    assert result == []


def test_sort_even_single_element():
    """Test with single element - triggers len(evens) > len(odds) branch."""
    result = sort_even([5])
    assert result == [5]


def test_sort_even_two_elements():
    """Test with two elements."""
    result = sort_even([5, 3])
    assert result == [5, 3]


def test_sort_even_three_elements():
    """Test with three elements - triggers len(evens) > len(odds) branch."""
    result = sort_even([1, 2, 3])
    assert result == [1, 2, 3]


def test_sort_even_four_elements():
    """Test with four elements - evens and odds same length."""
    result = sort_even([5, 6, 3, 4])
    assert result == [3, 6, 5, 4]


def test_sort_even_five_elements():
    """Test with five elements - triggers len(evens) > len(odds) branch."""
    result = sort_even([9, 1, 7, 2, 5])
    assert result == [5, 1, 7, 2, 9]


def test_sort_even_unsorted_evens():
    """Test that even indices are properly sorted."""
    result = sort_even([10, 100, 2, 200, 6, 300])
    assert result == [2, 100, 6, 200, 10, 300]


def test_sort_even_negative_numbers():
    """Test with negative numbers."""
    result = sort_even([-5, 10, -3, 20, -1])
    assert result == [-5, 10, -3, 20, -1]
