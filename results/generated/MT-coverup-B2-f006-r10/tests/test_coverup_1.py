# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

from f006 import parse_nested_parens


def test_parse_nested_parens_multiple_groups():
    """Covers the full happy path: the '(' branch, the max-depth update,
    the ')' (else) branch, the return of max_depth, and the list
    comprehension over split tokens."""
    result = parse_nested_parens("(()()) ((())) () ((())()())")
    assert result == [2, 3, 1, 3]


def test_parse_nested_parens_single_group():
    """Single groups, including a group whose maximum is reached and
    then unwound."""
    assert parse_nested_parens("((()))") == [3]
    assert parse_nested_parens("()") == [1]
    assert parse_nested_parens("(()") == [2]


def test_parse_nested_parens_filters_empty_tokens():
    """Leading/trailing/duplicate spaces produce empty tokens that the
    comprehension's `if x` filter must drop (covers the filter branch)."""
    assert parse_nested_parens("  (()())  ") == [2]
    assert parse_nested_parens("(() ) (())") == [2, 0, 2]


def test_parse_nested_parens_empty_input():
    """An empty or all-space string yields an empty result list."""
    assert parse_nested_parens("") == []
    assert parse_nested_parens("   ") == []


def test_parse_nested_parens_closing_paren_first():
    """A group starting with ')' exercises the else branch before any
    '(' is ever seen."""
    assert parse_nested_parens(")(") == [0]
