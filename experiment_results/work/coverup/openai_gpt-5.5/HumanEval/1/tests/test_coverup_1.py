# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

from script_1 import separate_paren_groups


def test_separate_paren_groups_handles_nested_and_adjacent_groups():
    assert separate_paren_groups("(())()") == ["(())", "()"]


def test_separate_paren_groups_ignores_non_parenthesis_characters():
    assert separate_paren_groups("a(b)c(())d") == ["()", "(())"]


def test_separate_paren_groups_returns_empty_list_without_groups():
    assert separate_paren_groups("") == []
    assert separate_paren_groups("abc") == []
