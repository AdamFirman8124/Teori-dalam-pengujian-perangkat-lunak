# file: script_58.py:1-14
# asked: {"lines": [9, 10, 11, 12, 13, 14], "branches": [[10, 11], [10, 14], [11, 10], [11, 12], [12, 11], [12, 13]]}
# gained: {"lines": [9, 10, 11, 12, 13, 14], "branches": [[10, 11], [10, 14], [11, 10], [11, 12], [12, 11], [12, 13]]}

import pytest
from script_58 import common


def test_common_with_multiple_common_elements():
    """Test common elements are found and sorted correctly."""
    result = common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    assert result == [1, 5, 653]


def test_common_with_subset():
    """Test when all elements of l2 are in l1."""
    result = common([5, 3, 2, 8], [3, 2])
    assert result == [2, 3]


def test_common_single_element():
    """Test with single common element."""
    result = common([1, 2, 3], [3, 4, 5])
    assert result == [3]


def test_common_all_elements():
    """Test when all elements are common."""
    result = common([1, 2, 3], [3, 2, 1])
    assert result == [1, 2, 3]


def test_common_duplicates_in_both_lists():
    """Test that duplicates are handled correctly - result should be unique."""
    result = common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4])
    assert result == [2, 3]


def test_common_with_negative_numbers():
    """Test with negative numbers."""
    result = common([-1, -2, 3, 4], [-2, -3, 3])
    assert result == [-2, 3]


def test_common_with_zero():
    """Test with zero in the lists."""
    result = common([0, 1, 2], [0, 3, 4])
    assert result == [0]
