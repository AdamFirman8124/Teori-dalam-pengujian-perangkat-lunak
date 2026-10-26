# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

import pytest

from f006 import parse_nested_parens


def test_single_group():
    # "(()())" reaches depth 2, never 3
    assert parse_nested_parens("(()())") == [2]


def test_multiple_groups():
    # "()" reaches depth 1, so its max depth is 1, not 0
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]


def test_empty_string_returns_empty_list():
    assert parse_nested_parens("") == []


def test_whitespace_only_returns_empty_list():
    # The 'if x' branch filters out empty tokens from split
    assert parse_nested_parens("   ") == []


def test_unbalanced_group_counts_closing_parens():
    # Depth goes negative; max_depth stays 0 since depth never exceeds it
    assert parse_nested_parens(")(") == [0]


def test_leading_trailing_spaces():
    # Extra spaces produce empty tokens that must be skipped
    assert parse_nested_parens("  (())  ()  ") == [2, 1]
