# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

from f006 import parse_nested_parens


def test_single_group():
    # "(()())" reaches depth 2, not 3
    result = parse_nested_parens("(()())")
    assert result == [2]


def test_multiple_groups():
    result = parse_nested_parens("(()()) ((())) () ((())()())")
    assert result == [2, 3, 1, 3]


def test_empty_string_returns_empty_list():
    assert parse_nested_parens("") == []


def test_extra_spaces_are_ignored():
    # split(' ') can produce empty strings; they must be filtered out
    result = parse_nested_parens("  (())   ()  ")
    assert result == [2, 1]


def test_nested_increasing_depth():
    result = parse_nested_parens("(((())))")
    assert result == [4]


def test_no_parens_at_all():
    assert parse_nested_parens("   ") == []
