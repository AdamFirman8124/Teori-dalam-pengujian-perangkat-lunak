# file: script_6.py:4-24
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}

import pytest
from script_6 import parse_nested_parens


def test_single_group_simple():
    """Test a single group with simple nesting."""
    result = parse_nested_parens('(())')
    assert result == [2]


def test_single_group_deep():
    """Test a single group with deep nesting."""
    result = parse_nested_parens('((()))')
    assert result == [3]


def test_multiple_groups():
    """Test multiple groups separated by spaces."""
    result = parse_nested_parens('(()()) ((())) () ((())()())')
    assert result == [2, 3, 1, 3]


def test_single_paren():
    """Test single level parentheses."""
    result = parse_nested_parens('()')
    assert result == [1]


def test_complex_nested():
    """Test complex nested structure."""
    result = parse_nested_parens('(()(()))')
    assert result == [3]


def test_multiple_simple_groups():
    """Test multiple simple groups."""
    result = parse_nested_parens('() () ()')
    assert result == [1, 1, 1]


def test_empty_string():
    """Test empty string input."""
    result = parse_nested_parens('')
    assert result == []


def test_spaces_only():
    """Test string with only spaces."""
    result = parse_nested_parens('   ')
    assert result == []


def test_mixed_depths():
    """Test groups with varying depths."""
    result = parse_nested_parens('((((())))) (()) ((()))')
    assert result == [5, 2, 3]
