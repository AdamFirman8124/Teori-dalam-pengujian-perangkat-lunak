# file: project/f001/__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

from f001 import separate_paren_groups


def test_empty_string():
    assert separate_paren_groups("") == []


def test_single_group():
    assert separate_paren_groups("()") == ["()"]


def test_nested_group_depth_not_zero_on_inner_close():
    assert separate_paren_groups("(())") == ["(())"]
    assert separate_paren_groups("((()))") == ["((()))"]


def test_multiple_separate_groups():
    assert separate_paren_groups("()()") == ["()", "()"]
    assert separate_paren_groups("(())()((()))") == ["(())", "()", "((()))"]


def test_non_paren_characters_are_ignored():
    assert separate_paren_groups("abc") == []
    assert separate_paren_groups("() ()") == ["()", "()"]
    assert separate_paren_groups("((())) (()())") == ["((()))", "(()())"]


def test_unclosed_group_is_not_returned():
    assert separate_paren_groups("(") == []
    assert separate_paren_groups("(()") == []
    assert separate_paren_groups("()((") == ["()"]
