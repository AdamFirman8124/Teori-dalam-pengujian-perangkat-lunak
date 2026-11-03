# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

import pytest

from f006 import parse_nested_parens


def test_multiple_groups_standard():
    """Covers the '(' branch (lines 10-12), the else branch (line 14),
    the return of max_depth (line 16) and the list comprehension (line 18)."""
    result = parse_nested_parens("(()()) ((())) () ((())()())")
    assert result == [2, 3, 1, 3]


def test_single_group_max_depth_increment():
    """Ensures max_depth is updated when depth increases mid-group."""
    assert parse_nested_parens("((()))") == [3]
    assert parse_nested_parens("()") == [1]


def test_empty_string_returns_empty_list():
    """Covers the 'if x' filter in the comprehension (line 18) with no groups."""
    assert parse_nested_parens("") == []


def test_extra_spaces_are_filtered_out():
    """Empty tokens produced by consecutive spaces are skipped (line 18 filter)."""
    assert parse_nested_parens("  (())   ()  ") == [2, 1]


def test_unbalanced_group_covers_else_branch():
    """A leading ')' exercises the else branch (line 14) with depth going
    negative; max_depth must remain 0 since it is only raised on '('."""
    assert parse_nested_parens(")(") == [0]
    assert parse_nested_parens("())") == [1]


def test_mixed_input_combines_all_branches():
    """Combines balanced, unbalanced and empty tokens in one call.

    "(() ) ()" splits into ["(()", ")", "()"]:
      "(()" -> depths 1,2,1 -> max 2
      ")"   -> depth -1     -> max 0 (else branch, never raised)
      "()"  -> depths 1,0   -> max 1
    """
    assert parse_nested_parens("(() ) ()") == [2, 0, 1]
