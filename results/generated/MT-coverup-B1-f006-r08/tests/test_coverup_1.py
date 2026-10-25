# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

from f006 import parse_nested_parens


def test_empty_string_returns_empty_list():
    assert parse_nested_parens("") == []


def test_spaces_only_returns_empty_list():
    assert parse_nested_parens(" ") == []
    assert parse_nested_parens("   ") == []


def test_single_groups():
    assert parse_nested_parens("()") == [1]
    assert parse_nested_parens("(())") == [2]
    assert parse_nested_parens("((()))") == [3]


def test_multiple_groups():
    assert parse_nested_parens("(()()) ((())) () ((()()()))") == [2, 3, 1, 3]


def test_ignores_empty_tokens_from_extra_spaces():
    assert parse_nested_parens("(()())  ((()))") == [2, 3]
    assert parse_nested_parens(" () ") == [1]
