# file: script_135.py:1-17
# asked: {"lines": [11, 12, 13, 14, 15, 16, 17], "branches": [[13, 14], [13, 17], [14, 15], [14, 16]]}
# gained: {"lines": [11, 12, 13, 14, 15, 16, 17], "branches": [[13, 14], [13, 17], [14, 15], [14, 16]]}

import pytest
from script_135 import can_arrange


def test_can_arrange_with_violation():
    """Test when there is an element smaller than its predecessor."""
    assert can_arrange([1, 2, 4, 3, 5]) == 3


def test_can_arrange_no_violation():
    """Test when all elements are in ascending order."""
    assert can_arrange([1, 2, 3]) == -1


def test_can_arrange_multiple_violations():
    """Test when there are multiple violations, should return the largest index."""
    assert can_arrange([1, 3, 2, 5, 4]) == 4


def test_can_arrange_first_violation():
    """Test when the violation is at index 1."""
    assert can_arrange([2, 1, 3, 4]) == 1


def test_can_arrange_all_descending():
    """Test when all elements are in descending order."""
    assert can_arrange([5, 4, 3, 2, 1]) == 4


def test_can_arrange_single_element():
    """Test with a single element array."""
    assert can_arrange([1]) == -1


def test_can_arrange_two_elements_ascending():
    """Test with two elements in ascending order."""
    assert can_arrange([1, 2]) == -1


def test_can_arrange_two_elements_descending():
    """Test with two elements in descending order."""
    assert can_arrange([2, 1]) == 1


def test_can_arrange_empty_array():
    """Test with an empty array."""
    assert can_arrange([]) == -1
