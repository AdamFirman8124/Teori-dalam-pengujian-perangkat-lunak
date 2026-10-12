# file: script_22.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

import pytest
from script_22 import filter_integers


def test_filter_integers_empty_list():
    """Test with empty list"""
    assert filter_integers([]) == []


def test_filter_integers_only_integers():
    """Test with only integers"""
    assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_filter_integers_mixed_types():
    """Test with mixed types including strings, floats, dicts, lists"""
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]


def test_filter_integers_no_integers():
    """Test with no integers"""
    assert filter_integers(['a', 'b', 3.14, [], {}, None]) == []


def test_filter_integers_negative_integers():
    """Test with negative integers"""
    assert filter_integers([-1, -2, 'test', 0, 5.5]) == [-1, -2, 0]


def test_filter_integers_booleans():
    """Test with booleans (bool is subclass of int in Python)"""
    assert filter_integers([True, False, 1, 2]) == [True, False, 1, 2]


def test_filter_integers_nested_structures():
    """Test with nested structures"""
    assert filter_integers([[1, 2], (3, 4), 5, 'string']) == [5]
