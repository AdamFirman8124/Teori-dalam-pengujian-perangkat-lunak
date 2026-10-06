# file: script_116.py:1-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

import pytest
from script_116 import sort_array


def test_sort_array_basic():
    """Test basic sorting with positive integers."""
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]


def test_sort_array_negative_numbers():
    """Test sorting with negative integers."""
    assert sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]


def test_sort_array_with_zero():
    """Test sorting with zero included."""
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]


def test_sort_array_empty():
    """Test sorting an empty array."""
    assert sort_array([]) == []


def test_sort_array_single_element():
    """Test sorting a single element array."""
    assert sort_array([5]) == [5]


def test_sort_array_all_same_bit_count():
    """Test sorting when all numbers have same number of ones in binary."""
    assert sort_array([1, 2, 4, 8]) == [1, 2, 4, 8]


def test_sort_array_mixed_positive_negative():
    """Test sorting with both positive and negative numbers."""
    assert sort_array([1, -1, 2, -2]) == [-2, -1, 1, 2]


def test_sort_array_large_numbers():
    """Test sorting with larger numbers."""
    assert sort_array([15, 7, 31, 1]) == [1, 7, 15, 31]
