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
    assert filter_integers([-1, -2, 3, 'test']) == [-1, -2, 3]


def test_filter_integers_zero():
    """Test with zero"""
    assert filter_integers([0, 'zero', 0.0]) == [0]


def test_filter_integers_bool_values():
    """Test with boolean values (booleans are instances of int in Python)"""
    assert filter_integers([True, False, 1, 2]) == [True, False, 1, 2]


def test_filter_integers_complex_mixed():
    """Test with complex mix of types"""
    assert filter_integers([1, 2.5, 'three', [4], {'five': 5}, 6, None, 7]) == [1, 6, 7]
