# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

import script_1


def test_separate_paren_groups_extracts_nested_and_separate_groups():
    paren_string = "(()()) ((())) ()"
    result = script_1.separate_paren_groups(paren_string)

    assert result == ["(()())", "((()))", "()"]


def test_separate_paren_groups_ignores_non_parenthesis_characters_and_empty_input():
    assert script_1.separate_paren_groups("abc (()) def () xyz") == ["(())", "()"]
    assert script_1.separate_paren_groups("no parentheses here") == []
    assert script_1.separate_paren_groups("") == []
