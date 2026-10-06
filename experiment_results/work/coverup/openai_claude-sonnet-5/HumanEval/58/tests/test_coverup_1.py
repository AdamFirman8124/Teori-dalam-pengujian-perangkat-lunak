# file: script_58.py:1-14
# asked: {"lines": [9, 10, 11, 12, 13, 14], "branches": [[10, 11], [10, 14], [11, 10], [11, 12], [12, 11], [12, 13]]}
# gained: {"lines": [9, 10, 11, 12, 13, 14], "branches": [[10, 11], [10, 14], [11, 10], [11, 12], [12, 11], [12, 13]]}

import pytest
from script_58 import common


def test_common_with_multiple_common_elements():
    """Test when lists have multiple common elements."""
    result = common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    assert result == [1, 5, 653]
    assert isinstance(result, list)
    assert result == sorted(result)


def test_common_with_subset():
    """Test when one list is a subset of another."""
    result = common([5, 3, 2, 8], [3, 2])
    assert result == [2, 3]
    assert isinstance(result, list)


def test_common_single_element():
    """Test when lists have a single common element."""
    result = common([1, 2, 3], [3, 4, 5])
    assert result == [3]


def test_common_all_elements_same():
    """Test when all elements are common."""
    result = common([1, 2, 3], [1, 2, 3])
    assert result == [1, 2, 3]


def test_common_duplicates_in_input():
    """Test that duplicates in input lists are handled correctly."""
    result = common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4])
    assert result == [2, 3]
    assert len(result) == len(set(result))


def test_common_unsorted_input():
    """Test with unsorted input lists."""
    result = common([5, 1, 3, 2], [2, 5, 4, 1])
    assert result == [1, 2, 5]
    assert result == sorted(result)


def test_common_negative_numbers():
    """Test with negative numbers."""
    result = common([-1, -2, 3, 4], [-2, -1, 5])
    assert result == [-2, -1]


def test_common_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    result = common([0, -5, 10, 3], [10, 0, -5])
    assert result == [-5, 0, 10]
