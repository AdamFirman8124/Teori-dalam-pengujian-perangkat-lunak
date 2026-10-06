# file: script_35.py:1-12
# asked: {"lines": [8, 9, 10, 11, 12], "branches": [[9, 10], [9, 12], [10, 9], [10, 11]]}
# gained: {"lines": [8, 9, 10, 11, 12], "branches": [[9, 10], [9, 12], [10, 9], [10, 11]]}

import pytest
from script_35 import max_element


def test_max_element_single_element():
    """Test with a single element list."""
    assert max_element([5]) == 5


def test_max_element_multiple_elements():
    """Test with multiple elements where max is not first."""
    assert max_element([1, 2, 3]) == 3


def test_max_element_max_at_beginning():
    """Test with maximum element at the beginning."""
    assert max_element([10, 5, 3, 1]) == 10


def test_max_element_max_in_middle():
    """Test with maximum element in the middle."""
    assert max_element([1, 5, 10, 3, 2]) == 10


def test_max_element_negative_numbers():
    """Test with negative numbers."""
    assert max_element([-5, -3, -10, -1]) == -1


def test_max_element_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123


def test_max_element_all_same():
    """Test with all elements being the same."""
    assert max_element([7, 7, 7, 7]) == 7


def test_max_element_two_elements():
    """Test with two elements."""
    assert max_element([3, 5]) == 5
    assert max_element([5, 3]) == 5
