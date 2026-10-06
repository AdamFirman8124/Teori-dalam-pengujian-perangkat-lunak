# file: script_70.py:1-17
# asked: {"lines": [12, 13, 14, 15, 16, 17], "branches": [[13, 14], [13, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17], "branches": [[13, 14], [13, 17]]}

import pytest
from script_70 import strange_sort_list


def test_strange_sort_list_empty():
    """Test with empty list."""
    assert strange_sort_list([]) == []


def test_strange_sort_list_single_element():
    """Test with single element."""
    assert strange_sort_list([5]) == [5]


def test_strange_sort_list_two_elements():
    """Test with two elements."""
    assert strange_sort_list([1, 2]) == [1, 2]


def test_strange_sort_list_ascending():
    """Test with ascending order list."""
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]


def test_strange_sort_list_descending():
    """Test with descending order list."""
    assert strange_sort_list([4, 3, 2, 1]) == [1, 4, 2, 3]


def test_strange_sort_list_duplicates():
    """Test with all same elements."""
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]


def test_strange_sort_list_mixed():
    """Test with mixed positive and negative numbers."""
    assert strange_sort_list([3, -1, 0, 5, -2]) == [-2, 5, -1, 3, 0]


def test_strange_sort_list_odd_length():
    """Test with odd length list."""
    assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]


def test_strange_sort_list_negative_numbers():
    """Test with negative numbers."""
    assert strange_sort_list([-5, -1, -3]) == [-5, -1, -3]
