# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

import script_1


def test_separate_paren_groups_handles_nested_and_multiple_groups():
    paren_string = "prefix((inner))(outer)suffix"

    result = script_1.separate_paren_groups(paren_string)

    assert result == ["(())", "()"]


def test_separate_paren_groups_returns_empty_for_input_without_parentheses():
    result = script_1.separate_paren_groups("plain text")

    assert result == []
