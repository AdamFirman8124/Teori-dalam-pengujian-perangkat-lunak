# file: script_6.py:4-24
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}

import script_6


def test_parse_nested_parens_covers_all_lines():
    result = script_6.parse_nested_parens('(()()) ((())) () ((())()())')
    assert result == [2, 3, 1, 3]


def test_parse_nested_parens_single_group():
    result = script_6.parse_nested_parens('((()))')
    assert result == [3]


def test_parse_nested_parens_simple_group():
    result = script_6.parse_nested_parens('()')
    assert result == [1]


def test_parse_nested_parens_empty_string():
    result = script_6.parse_nested_parens('')
    assert result == []


def test_parse_nested_parens_extra_spaces():
    result = script_6.parse_nested_parens('(()())  ()')
    assert result == [2, 1]
