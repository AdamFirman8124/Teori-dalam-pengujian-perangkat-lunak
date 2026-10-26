# file: project/f001/__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

from f001 import separate_paren_groups


def test_empty_string():
    assert separate_paren_groups("") == []


def test_single_group():
    assert separate_paren_groups("()") == ["()"]


def test_multiple_groups():
    assert separate_paren_groups("()()") == ["()", "()"]
    assert separate_paren_groups("(()) ()") == ["(())", "()"]


def test_nested_group_depth_nonzero_branch():
    # inner ')' leaves depth != 0 so lines 18-20 take False branch once
    assert separate_paren_groups("(())") == ["(())"]
    assert separate_paren_groups("((()))") == ["((()))"]
    assert separate_paren_groups("(()())") == ["(()())"]


def test_ignores_non_paren_characters():
    # covers c != '(' and c != ')' branches (spaces / letters)
    assert separate_paren_groups(" ( ) ") == ["()"]
    assert separate_paren_groups("a(b)c") == ["()"]
    assert separate_paren_groups("   ") == []
    assert separate_paren_groups("(()()) ((())) ()") == ["(()())", "((()))", "()"]
