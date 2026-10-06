# file: script_q1.py:2-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest
from script_q1 import search


def test_search_element_found_at_beginning():
    """Test when element is found at the first position"""
    assert search(1, [1, 2, 3, 4, 5]) == 0


def test_search_element_found_in_middle():
    """Test when element is found in the middle"""
    assert search(3, [1, 2, 3, 4, 5]) == 2


def test_search_element_found_at_end():
    """Test when element is found at the last position"""
    assert search(5, [1, 2, 3, 4, 5]) == 4


def test_search_element_smaller_than_first():
    """Test when element is smaller than all elements"""
    assert search(0, [1, 2, 3, 4, 5]) == 0


def test_search_element_larger_than_all():
    """Test when element is larger than all elements"""
    assert search(10, [1, 2, 3, 4, 5]) == 5


def test_search_empty_sequence():
    """Test with empty sequence"""
    assert search(5, []) == 0


def test_search_single_element_less_than():
    """Test with single element, search value less than element"""
    assert search(1, [5]) == 0


def test_search_single_element_greater_than():
    """Test with single element, search value greater than element"""
    assert search(10, [5]) == 1


def test_search_duplicate_elements():
    """Test with duplicate elements in sequence"""
    assert search(3, [1, 3, 3, 3, 5]) == 1
