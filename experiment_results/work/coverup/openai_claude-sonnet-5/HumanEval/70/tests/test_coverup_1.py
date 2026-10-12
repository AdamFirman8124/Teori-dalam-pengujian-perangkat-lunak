# file: script_70.py:1-17
# asked: {"lines": [12, 13, 14, 15, 16, 17], "branches": [[13, 14], [13, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17], "branches": [[13, 14], [13, 17]]}

import pytest
from script_70 import strange_sort_list


def test_strange_sort_list_single_element():
    """Test with a single element list."""
    result = strange_sort_list([42])
    assert result == [42]


def test_strange_sort_list_two_elements():
    """Test with two elements."""
    result = strange_sort_list([3, 1])
    assert result == [1, 3]


def test_strange_sort_list_multiple_elements():
    """Test with multiple distinct elements."""
    result = strange_sort_list([1, 2, 3, 4])
    assert result == [1, 4, 2, 3]


def test_strange_sort_list_all_same():
    """Test with all identical elements."""
    result = strange_sort_list([5, 5, 5, 5])
    assert result == [5, 5, 5, 5]


def test_strange_sort_list_empty():
    """Test with empty list."""
    result = strange_sort_list([])
    assert result == []


def test_strange_sort_list_negative_numbers():
    """Test with negative numbers."""
    result = strange_sort_list([-1, -5, 0, 3])
    assert result == [-5, 3, -1, 0]


def test_strange_sort_list_unsorted():
    """Test with unsorted list."""
    result = strange_sort_list([5, 1, 4, 2, 3])
    assert result == [1, 5, 2, 4, 3]


def test_strange_sort_list_duplicates():
    """Test with duplicates."""
    result = strange_sort_list([3, 1, 3, 2])
    assert result == [1, 3, 2, 3]
