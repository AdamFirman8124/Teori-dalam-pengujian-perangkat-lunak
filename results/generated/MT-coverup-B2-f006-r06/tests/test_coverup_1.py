# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

import pytest

from f006 import parse_nested_parens


def test_single_group_basic():
    """Covers parse_paren_group definition, loop, '(' branch and return."""
    assert parse_nested_parens("()") == [1]


def test_multiple_groups_various_depths():
    """Covers the list comprehension over several groups and both '(' and else branches."""
    result = parse_nested_parens("(()()) ((())) () ((())()())")
    assert result == [2, 3, 1, 3]


def test_deep_nesting():
    """Deeper nesting exercises max_depth update repeatedly."""
    assert parse_nested_parens("(((())))") == [4]


def test_multiple_spaces_filter_empty_tokens():
    """Consecutive spaces produce empty tokens filtered out by 'if x' (true branch of filter)."""
    assert parse_nested_parens("()  (())   ((()))") == [1, 2, 3]


def test_leading_and_trailing_spaces():
    """Leading/trailing spaces yield empty tokens that are skipped."""
    assert parse_nested_parens("  () (())  ") == [1, 2]


def test_empty_string_returns_empty_list():
    """Empty input: split yields [''], filter drops it (false branch of 'if x')."""
    assert parse_nested_parens("") == []


def test_whitespace_only_string():
    """Whitespace-only input also exercises the false branch of the comprehension filter."""
    assert parse_nested_parens("   ") == []
