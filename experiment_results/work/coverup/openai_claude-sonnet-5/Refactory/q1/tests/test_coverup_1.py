# file: script_q1.py:2-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest
from script_q1 import search


def test_search_element_at_beginning():
    """Test when element is less than or equal to first element."""
    assert search(1, [1, 2, 3, 4]) == 0
    assert search(0, [1, 2, 3, 4]) == 0


def test_search_element_in_middle():
    """Test when element is in the middle of sequence."""
    assert search(3, [1, 2, 3, 4, 5]) == 2
    assert search(2, [1, 2, 3, 4, 5]) == 1


def test_search_element_at_end():
    """Test when element equals last element."""
    assert search(5, [1, 2, 3, 4, 5]) == 4


def test_search_element_greater_than_all():
    """Test when element is greater than all elements in sequence."""
    assert search(10, [1, 2, 3, 4, 5]) == 5


def test_search_empty_sequence():
    """Test with empty sequence."""
    assert search(1, []) == 0


def test_search_single_element_found():
    """Test with single element sequence where element is found."""
    assert search(1, [1]) == 0
    assert search(0, [1]) == 0


def test_search_single_element_not_found():
    """Test with single element sequence where element is greater."""
    assert search(5, [1]) == 1
