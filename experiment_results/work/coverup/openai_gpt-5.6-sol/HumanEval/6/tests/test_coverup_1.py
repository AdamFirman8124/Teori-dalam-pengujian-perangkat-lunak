# file: script_6.py:4-24
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}

import pytest

from script_6 import parse_nested_parens


def test_parse_nested_parens_returns_maximum_depth_for_each_group():
    paren_string = "(()()) ((())) () ((())()())"

    result = parse_nested_parens(paren_string)

    assert result == [2, 3, 1, 3]


def test_parse_nested_parens_ignores_empty_groups_between_spaces():
    result = parse_nested_parens("  ()   (())     ")

    assert result == [1, 2]
    assert parse_nested_parens("") == []
