# file: script_105.py:1-41
# asked: {"lines": [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": [[36, 37], [36, 41]]}
# gained: {"lines": [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41], "branches": [[36, 37], [36, 41]]}

import pytest
from script_105 import by_length


def test_by_length_normal_case():
    """Test with normal array of integers between 1 and 9"""
    arr = [2, 1, 1, 4, 5, 8, 2, 3]
    result = by_length(arr)
    assert result == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]


def test_by_length_empty_array():
    """Test with empty array"""
    arr = []
    result = by_length(arr)
    assert result == []


def test_by_length_with_invalid_numbers():
    """Test with array containing numbers outside 1-9 range"""
    arr = [1, -1, 55]
    result = by_length(arr)
    assert result == ["One"]


def test_by_length_all_valid_digits():
    """Test with all digits from 1 to 9"""
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = by_length(arr)
    assert result == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]


def test_by_length_only_invalid_numbers():
    """Test with array containing only invalid numbers"""
    arr = [0, 10, -5, 100]
    result = by_length(arr)
    assert result == []


def test_by_length_mixed_valid_invalid():
    """Test with mixed valid and invalid numbers"""
    arr = [9, 0, 5, 10, 3, -1]
    result = by_length(arr)
    assert result == ["Nine", "Five", "Three"]


def test_by_length_single_valid():
    """Test with single valid number"""
    arr = [7]
    result = by_length(arr)
    assert result == ["Seven"]


def test_by_length_duplicates():
    """Test with duplicate valid numbers"""
    arr = [5, 5, 5, 3, 3]
    result = by_length(arr)
    assert result == ["Five", "Five", "Five", "Three", "Three"]
