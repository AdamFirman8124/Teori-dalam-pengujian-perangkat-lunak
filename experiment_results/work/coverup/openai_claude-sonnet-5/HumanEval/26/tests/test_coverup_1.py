# file: script_26.py:4-12
# asked: {"lines": [10, 11, 12], "branches": []}
# gained: {"lines": [10, 11, 12], "branches": []}

from typing import List
import pytest
from script_26 import remove_duplicates


def test_remove_duplicates_with_duplicates():
    """Test that elements occurring more than once are removed."""
    result = remove_duplicates([1, 2, 3, 2, 4])
    assert result == [1, 3, 4]


def test_remove_duplicates_no_duplicates():
    """Test with a list that has no duplicates."""
    result = remove_duplicates([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


def test_remove_duplicates_all_duplicates():
    """Test with a list where all elements appear more than once."""
    result = remove_duplicates([1, 1, 2, 2, 3, 3])
    assert result == []


def test_remove_duplicates_empty_list():
    """Test with an empty list."""
    result = remove_duplicates([])
    assert result == []


def test_remove_duplicates_single_element():
    """Test with a single element."""
    result = remove_duplicates([1])
    assert result == [1]


def test_remove_duplicates_triple_occurrence():
    """Test with elements occurring three times."""
    result = remove_duplicates([1, 2, 1, 3, 1])
    assert result == [2, 3]


def test_remove_duplicates_preserves_order():
    """Test that the order of remaining elements is preserved."""
    result = remove_duplicates([5, 1, 3, 1, 2, 3, 4])
    assert result == [5, 2, 4]
