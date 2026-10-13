# file: script_6.py:4-24
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 20, 22, 24], "branches": [[15, 16], [15, 22], [16, 17], [16, 20]]}

import script_6


def test_parse_nested_parens_returns_maximum_depth_for_each_group():
    result = script_6.parse_nested_parens("(()()) ((())) () ((())()())")

    assert result == [2, 3, 1, 3]


def test_parse_nested_parens_ignores_empty_groups_between_spaces():
    result = script_6.parse_nested_parens("  ()   (()) ")

    assert result == [1, 2]


def test_parse_nested_parens_returns_empty_list_for_empty_input():
    result = script_6.parse_nested_parens("")

    assert result == []
