# file: script_90.py:1-13
# asked: {"lines": [12, 13], "branches": []}
# gained: {"lines": [12, 13], "branches": []}

import pytest
from script_90 import next_smallest


def test_next_smallest_with_duplicates():
    """Test that returns 2nd smallest when list has duplicates"""
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2


def test_next_smallest_empty_list():
    """Test that returns None for empty list"""
    assert next_smallest([]) is None


def test_next_smallest_all_duplicates():
    """Test that returns None when all elements are the same"""
    assert next_smallest([1, 1]) is None
    assert next_smallest([5, 5, 5, 5]) is None


def test_next_smallest_single_element():
    """Test that returns None for single element"""
    assert next_smallest([1]) is None


def test_next_smallest_two_distinct_elements():
    """Test that returns 2nd element when exactly two distinct elements"""
    assert next_smallest([1, 2]) == 2
    assert next_smallest([10, 5]) == 10


def test_next_smallest_multiple_duplicates_with_distinct():
    """Test with multiple duplicates but multiple distinct values"""
    assert next_smallest([3, 1, 2, 1, 3, 2]) == 2
    assert next_smallest([5, 5, 1, 1, 3, 3]) == 3


def test_next_smallest_negative_numbers():
    """Test with negative numbers"""
    assert next_smallest([-5, -1, -3, -2]) == -3
    assert next_smallest([-10, -10, -5]) == -5


def test_next_smallest_mixed_positive_negative():
    """Test with mixed positive and negative numbers"""
    assert next_smallest([-1, 0, 1, 2]) == 0
    assert next_smallest([5, -5, 10, -10]) == -5
