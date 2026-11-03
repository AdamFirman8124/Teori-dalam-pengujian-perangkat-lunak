# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

import pytest

from f006 import parse_nested_parens


def test_multiple_groups_covers_all_lines():
    """Exercises lines 6-18: multiple groups with varying nesting depths.

    Verifies the inner parse_paren_group closure (lines 6-16) and the
    list comprehension with the `if x` filter (line 18).
    """
    result = parse_nested_parens("(()()) ((())) () ((())()())")
    assert result == [2, 3, 1, 3]


def test_single_group():
    """A single group still goes through the full parse path."""
    result = parse_nested_parens("((()))")
    assert result == [3]


def test_empty_string_returns_empty_list():
    """''.split(' ') yields [''], which the `if x` filter drops (line 18)."""
    result = parse_nested_parens("")
    assert result == []


def test_only_spaces_returns_empty_list():
    """All tokens are empty after split, so the filter removes them all."""
    result = parse_nested_parens("   ")
    assert result == []


def test_consecutive_spaces_are_filtered():
    """Extra spaces produce empty tokens that must be skipped."""
    result = parse_nested_parens("(()())  ((()))")
    assert result == [2, 3]


def test_deep_nesting():
    """Deeply nested group exercises the max() update on line 12 repeatedly."""
    result = parse_nested_parens("((((()))))")
    assert result == [5]


def test_unbalanced_group_still_returns_max_depth():
    """The else branch (line 14) decrements depth even for unbalanced input."""
    result = parse_nested_parens("(()")
    assert result == [2]


def test_result_is_a_list_of_ints():
    """Postcondition: return type is List[int] as annotated."""
    result = parse_nested_parens("() (())")
    assert isinstance(result, list)
    assert all(isinstance(d, int) for d in result)
    assert result == [1, 2]
