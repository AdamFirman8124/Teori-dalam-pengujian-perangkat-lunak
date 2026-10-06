# file: script_6.py:4-24
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}

import pytest
from script_6 import parse_nested_parens


def test_single_group_simple():
    result = parse_nested_parens('()')
    assert result == [1]


def test_single_group_nested():
    result = parse_nested_parens('(()())')
    assert result == [2]


def test_single_group_deeply_nested():
    result = parse_nested_parens('((()))')
    assert result == [3]


def test_multiple_groups():
    result = parse_nested_parens('(()()) ((())) () ((())()())')
    assert result == [2, 3, 1, 3]


def test_empty_string():
    result = parse_nested_parens('')
    assert result == []


def test_multiple_spaces():
    result = parse_nested_parens('(()) () ((()))')
    assert result == [2, 1, 3]


def test_single_parenthesis():
    result = parse_nested_parens('()')
    assert result == [1]


def test_complex_nesting():
    result = parse_nested_parens('(((())))') 
    assert result == [4]


def test_mixed_complexity():
    result = parse_nested_parens('() (()) ((()))')
    assert result == [1, 2, 3]
