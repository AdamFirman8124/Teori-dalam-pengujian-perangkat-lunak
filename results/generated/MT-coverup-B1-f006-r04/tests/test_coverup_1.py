# file: project/f006/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

from f006 import parse_nested_parens


def test_parse_nested_parens_single_group():
    assert parse_nested_parens("()") == [1]
    assert parse_nested_parens("(())") == [2]
    assert parse_nested_parens("((()))") == [3]


def test_parse_nested_parens_multiple_groups():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert parse_nested_parens("() (()) ((()))") == [1, 2, 3]


def test_parse_nested_parens_empty_and_spacing_filters():
    assert parse_nested_parens("") == []
    assert parse_nested_parens("   ") == []
    # double space creates empty strings that are filtered by `if x`
    assert parse_nested_parens("()  (())") == [1, 2]
    assert parse_nested_parens(" () ") == [1]
    assert parse_nested_parens("() ()") == [1, 1]
