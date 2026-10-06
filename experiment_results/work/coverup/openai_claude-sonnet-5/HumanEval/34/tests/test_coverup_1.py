# file: script_34.py:1-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest
from script_34 import unique


def test_unique_with_duplicates():
    """Test unique function with a list containing duplicates."""
    result = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    assert result == [0, 2, 3, 5, 9, 123]


def test_unique_empty_list():
    """Test unique function with an empty list."""
    result = unique([])
    assert result == []


def test_unique_single_element():
    """Test unique function with a single element."""
    result = unique([42])
    assert result == [42]


def test_unique_all_same_elements():
    """Test unique function with all identical elements."""
    result = unique([7, 7, 7, 7])
    assert result == [7]


def test_unique_already_unique():
    """Test unique function with already unique elements."""
    result = unique([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


def test_unique_negative_numbers():
    """Test unique function with negative numbers."""
    result = unique([-5, -3, -5, 0, 3, -3])
    assert result == [-5, -3, 0, 3]


def test_unique_unsorted_input():
    """Test unique function with unsorted input."""
    result = unique([9, 1, 8, 2, 7, 3])
    assert result == [1, 2, 3, 7, 8, 9]
