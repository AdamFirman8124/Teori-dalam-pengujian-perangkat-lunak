# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

import pytest

from f006 import parse_nested_parens


def test_multiple_groups():
    """Covers lines 6-18: inner function, both branches, and list comprehension."""
    result = parse_nested_parens('(()()) ((())) () ((())()())')
    assert result == [2, 3, 1, 3]


def test_single_group():
    result = parse_nested_parens('((()))')
    assert result == [3]


def test_empty_string_returns_empty_list():
    """The `if x` filter branch drops empty tokens produced by splitting."""
    assert parse_nested_parens('') == []


def test_whitespace_string_returns_empty_list():
    """Multiple spaces yield empty tokens, all filtered out by `if x`."""
    assert parse_nested_parens('   ') == []


def test_group_with_only_closing_prefix():
    """Exercises the else branch (depth -= 1) where depth can go below zero
    for a group that starts with ')'; max_depth stays 0."""
    assert parse_nested_parens(')(') == [0]


def test_all_branches():
    """Mixed content so both the '(' branch and the else branch run,
    and max is updated multiple times."""
    assert parse_nested_parens('() (()) (((())))') == [1, 2, 4]
