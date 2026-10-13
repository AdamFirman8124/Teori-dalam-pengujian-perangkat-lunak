# file: script_6.py:4-24
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}

import pytest
from script_6 import parse_nested_parens


def test_parse_nested_parens_single_group_simple():
    """Test single group with simple nesting"""
    result = parse_nested_parens('()')
    assert result == [1]


def test_parse_nested_parens_single_group_double_nesting():
    """Test single group with two levels of nesting"""
    result = parse_nested_parens('(())')
    assert result == [2]


def test_parse_nested_parens_single_group_triple_nesting():
    """Test single group with three levels of nesting"""
    result = parse_nested_parens('((()))')
    assert result == [3]


def test_parse_nested_parens_multiple_groups():
    """Test multiple groups separated by spaces"""
    result = parse_nested_parens('(()()) ((())) () ((())()())')
    assert result == [2, 3, 1, 3]


def test_parse_nested_parens_single_group_complex():
    """Test single group with complex structure"""
    result = parse_nested_parens('(()())')
    assert result == [2]


def test_parse_nested_parens_two_groups():
    """Test two groups"""
    result = parse_nested_parens('(()) ()')
    assert result == [2, 1]


def test_parse_nested_parens_empty_string():
    """Test empty string"""
    result = parse_nested_parens('')
    assert result == []


def test_parse_nested_parens_multiple_spaces():
    """Test multiple spaces between groups"""
    result = parse_nested_parens('(())  ()')
    assert result == [2, 1]


def test_parse_nested_parens_deep_nesting():
    """Test deep nesting level"""
    result = parse_nested_parens('((((()))))')
    assert result == [5]


def test_parse_nested_parens_multiple_groups_various_depths():
    """Test multiple groups with various depths"""
    result = parse_nested_parens('() (()) ((()))')
    assert result == [1, 2, 3]
