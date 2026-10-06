# file: script_9.py:4-21
# asked: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}
# gained: {"lines": [10, 11, 13, 14, 15, 17, 19, 21], "branches": [[13, 14], [13, 21], [14, 15], [14, 17]]}

import pytest
from script_9 import rolling_max


def test_rolling_max_single_element():
    """Test with a single element list"""
    result = rolling_max([5])
    assert result == [5]


def test_rolling_max_ascending():
    """Test with ascending numbers"""
    result = rolling_max([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


def test_rolling_max_descending():
    """Test with descending numbers"""
    result = rolling_max([5, 4, 3, 2, 1])
    assert result == [5, 5, 5, 5, 5]


def test_rolling_max_mixed():
    """Test with mixed numbers"""
    result = rolling_max([1, 2, 3, 2, 3, 4, 2])
    assert result == [1, 2, 3, 3, 3, 4, 4]


def test_rolling_max_with_negatives():
    """Test with negative numbers"""
    result = rolling_max([-5, -2, -8, -1])
    assert result == [-5, -2, -2, -1]


def test_rolling_max_empty_list():
    """Test with empty list"""
    result = rolling_max([])
    assert result == []


def test_rolling_max_all_same():
    """Test with all same numbers"""
    result = rolling_max([3, 3, 3, 3])
    assert result == [3, 3, 3, 3]
