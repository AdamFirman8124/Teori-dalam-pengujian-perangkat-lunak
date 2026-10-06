# file: script_37.py:1-18
# asked: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[14, 15], [14, 16], [16, 17], [16, 18]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[14, 15], [14, 16], [16, 17], [16, 18]]}

import pytest
from script_37 import sort_even


def test_sort_even_basic():
    """Test basic functionality with mixed values"""
    result = sort_even([5, 6, 3, 4])
    assert result == [3, 6, 5, 4]


def test_sort_even_simple():
    """Test simple case"""
    result = sort_even([1, 2, 3])
    assert result == [1, 2, 3]


def test_sort_even_even_length():
    """Test with even-length list"""
    result = sort_even([8, 1, 6, 2, 4, 3])
    assert result == [4, 1, 6, 2, 8, 3]


def test_sort_even_odd_length():
    """Test with odd-length list where evens > odds"""
    result = sort_even([9, 2, 7, 4, 5])
    assert result == [5, 2, 7, 4, 9]


def test_sort_even_single_element():
    """Test with single element (odd length, evens > odds)"""
    result = sort_even([42])
    assert result == [42]


def test_sort_even_empty():
    """Test with empty list"""
    result = sort_even([])
    assert result == []


def test_sort_even_two_elements():
    """Test with two elements (even length)"""
    result = sort_even([10, 5])
    assert result == [10, 5]
