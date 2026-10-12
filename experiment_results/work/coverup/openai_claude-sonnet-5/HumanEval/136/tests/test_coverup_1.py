# file: script_136.py:1-15
# asked: {"lines": [13, 14, 15], "branches": []}
# gained: {"lines": [13, 14, 15], "branches": []}

import pytest
from script_136 import largest_smallest_integers


def test_empty_list():
    """Test with empty list"""
    result = largest_smallest_integers([])
    assert result == (None, None)


def test_only_zero():
    """Test with only zero"""
    result = largest_smallest_integers([0])
    assert result == (None, None)


def test_only_positive():
    """Test with only positive integers"""
    result = largest_smallest_integers([2, 4, 1, 3, 5, 7])
    assert result == (None, 1)


def test_only_negative():
    """Test with only negative integers"""
    result = largest_smallest_integers([-2, -4, -1, -3, -5, -7])
    assert result == (-1, None)


def test_mixed_positive_and_negative():
    """Test with both positive and negative integers"""
    result = largest_smallest_integers([-5, -3, -1, 1, 3, 5])
    assert result == (-1, 1)


def test_mixed_with_zero():
    """Test with positive, negative, and zero"""
    result = largest_smallest_integers([-10, -5, 0, 5, 10])
    assert result == (-5, 5)


def test_single_negative():
    """Test with single negative integer"""
    result = largest_smallest_integers([-7])
    assert result == (-7, None)


def test_single_positive():
    """Test with single positive integer"""
    result = largest_smallest_integers([7])
    assert result == (None, 7)


def test_multiple_zeros():
    """Test with multiple zeros"""
    result = largest_smallest_integers([0, 0, 0])
    assert result == (None, None)


def test_large_numbers():
    """Test with large numbers"""
    result = largest_smallest_integers([-1000, -500, 500, 1000])
    assert result == (-500, 500)
