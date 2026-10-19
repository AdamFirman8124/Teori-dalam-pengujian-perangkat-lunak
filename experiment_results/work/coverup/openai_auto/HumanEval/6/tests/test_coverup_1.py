# file: script_6.py:4-24
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}

import pytest

from script_6 import parse_nested_parens


def test_parse_nested_parens_multiple_groups():
    result = parse_nested_parens('(()()) ((())) () ((())()())')
    assert result == [2, 3, 1, 3]


def test_parse_nested_parens_single_group():
    assert parse_nested_parens('((()))') == [3]


def test_parse_nested_parens_ends_with_close_paren_branch():
    # exercises the else-branch (depth -= 1) on line 20
    assert parse_nested_parens('()') == [1]


def test_parse_nested_parens_empty_string_filters_empty_splits():
    # exercises the `if x` filter on line 24 with empty tokens
    assert parse_nested_parens('  ()  ') == [1]
    assert parse_nested_parens('') == []


def test_parse_nested_parens_returns_new_list_no_state_pollution():
    # verify purity: calling twice yields same result (no shared state)
    first = parse_nested_parens('(()) ()')
    second = parse_nested_parens('(()) ()')
    assert first == second == [2, 1]
