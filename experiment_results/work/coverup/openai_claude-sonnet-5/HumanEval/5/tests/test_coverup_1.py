# file: script_5.py:4-22
# asked: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}
# gained: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}

import pytest
from script_5 import intersperse


def test_intersperse_empty_list():
    """Test intersperse with an empty list."""
    result = intersperse([], 4)
    assert result == []


def test_intersperse_single_element():
    """Test intersperse with a single element list."""
    result = intersperse([1], 4)
    assert result == [1]


def test_intersperse_multiple_elements():
    """Test intersperse with multiple elements."""
    result = intersperse([1, 2, 3], 4)
    assert result == [1, 4, 2, 4, 3]


def test_intersperse_two_elements():
    """Test intersperse with two elements."""
    result = intersperse([5, 10], 0)
    assert result == [5, 0, 10]


def test_intersperse_negative_delimiter():
    """Test intersperse with negative delimiter."""
    result = intersperse([1, 2, 3, 4], -1)
    assert result == [1, -1, 2, -1, 3, -1, 4]
