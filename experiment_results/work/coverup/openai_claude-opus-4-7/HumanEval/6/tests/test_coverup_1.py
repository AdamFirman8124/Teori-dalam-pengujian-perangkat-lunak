# file: script_6.py:4-24
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}

from script_6 import parse_nested_parens


def test_parse_nested_parens_docstring_example():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]


def test_parse_nested_parens_single_group():
    assert parse_nested_parens('((()))') == [3]


def test_parse_nested_parens_empty_string():
    assert parse_nested_parens('') == []


def test_parse_nested_parens_only_spaces():
    assert parse_nested_parens('   ') == []


def test_parse_nested_parens_multiple_spaces_between_groups():
    assert parse_nested_parens('()   (())  ((()))') == [1, 2, 3]


def test_parse_nested_parens_flat_group():
    assert parse_nested_parens('()') == [1]


def test_parse_nested_parens_leading_and_trailing_spaces():
    assert parse_nested_parens('  (()) ()  ') == [2, 1]


def test_parse_nested_parens_deep_nesting():
    assert parse_nested_parens('((((()))))') == [5]


def test_parse_nested_parens_mixed_depths():
    assert parse_nested_parens('() (()) ((())) (((())))') == [1, 2, 3, 4]
