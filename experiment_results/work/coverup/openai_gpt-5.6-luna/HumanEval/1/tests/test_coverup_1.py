# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

from script_1 import separate_paren_groups


def test_separate_paren_groups_handles_nested_and_adjacent_groups():
    paren_string = "prefix(())middle(()())suffix"

    result = separate_paren_groups(paren_string)

    assert result == ["(())", "(()())"]


def test_separate_paren_groups_returns_complete_groups_before_incomplete_group():
    paren_string = "text(complete)(unfinished"

    result = separate_paren_groups(paren_string)

    assert result == ["()"]


def test_separate_paren_groups_returns_empty_for_no_complete_groups():
    assert separate_paren_groups("") == []
    assert separate_paren_groups("plain text") == []
    assert separate_paren_groups("((unfinished") == []
