# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

from f006 import parse_nested_parens


def test_parse_single_parenthesis_group():
    assert parse_nested_parens("(()())") == [2]


def test_parse_multiple_groups_and_ignore_extra_spaces():
    assert parse_nested_parens("  () (()) ((())) ((())()())  ") == [1, 2, 3, 3]


def test_parse_empty_string():
    assert parse_nested_parens("") == []
