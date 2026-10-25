# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

from f006 import parse_nested_parens


def test_single_group():
    assert parse_nested_parens("(()())") == [2]


def test_multiple_groups():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]


def test_empty_string_returns_empty_list():
    assert parse_nested_parens("") == []


def test_extra_spaces_are_ignored():
    assert parse_nested_parens("  (())  ()  ") == [2, 1]


def test_groups_with_increasing_depth():
    assert parse_nested_parens("() (()) ((()))") == [1, 2, 3]


def test_deeply_nested_single_group():
    assert parse_nested_parens("(((())))") == [4]


def test_result_contains_integers():
    result = parse_nested_parens("(()) ()")
    assert result == [2, 1]
    assert all(isinstance(depth, int) for depth in result)
