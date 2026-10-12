# file: script_42.py:1-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest
from script_42 import incr_list


def test_incr_list_basic():
    """Test incrementing a basic list."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]


def test_incr_list_longer():
    """Test incrementing a longer list."""
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]


def test_incr_list_empty():
    """Test incrementing an empty list."""
    assert incr_list([]) == []


def test_incr_list_single_element():
    """Test incrementing a single element list."""
    assert incr_list([0]) == [1]


def test_incr_list_negative_numbers():
    """Test incrementing negative numbers."""
    assert incr_list([-5, -1, 0, 1]) == [-4, 0, 1, 2]
