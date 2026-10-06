# file: script_26.py:4-12
# asked: {"lines": [10, 11, 12], "branches": []}
# gained: {"lines": [10, 11, 12], "branches": []}

import pytest
from script_26 import remove_duplicates


def test_remove_duplicates_with_duplicates():
    """Test removing elements that occur more than once."""
    result = remove_duplicates([1, 2, 3, 2, 4])
    assert result == [1, 3, 4]


def test_remove_duplicates_no_duplicates():
    """Test with list containing no duplicates."""
    result = remove_duplicates([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


def test_remove_duplicates_all_duplicates():
    """Test with list where all elements appear more than once."""
    result = remove_duplicates([1, 1, 2, 2, 3, 3])
    assert result == []


def test_remove_duplicates_empty_list():
    """Test with empty list."""
    result = remove_duplicates([])
    assert result == []


def test_remove_duplicates_single_element():
    """Test with single element list."""
    result = remove_duplicates([5])
    assert result == [5]


def test_remove_duplicates_preserves_order():
    """Test that order is preserved for remaining elements."""
    result = remove_duplicates([5, 1, 3, 1, 2, 3, 4])
    assert result == [5, 2, 4]


def test_remove_duplicates_triple_occurrence():
    """Test elements that occur three or more times."""
    result = remove_duplicates([1, 2, 1, 3, 1, 2])
    assert result == [3]
