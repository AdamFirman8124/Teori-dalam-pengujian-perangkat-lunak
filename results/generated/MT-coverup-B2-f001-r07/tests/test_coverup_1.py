# file: project/f001/__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

from f001 import separate_paren_groups


def test_single_group():
    result = separate_paren_groups("()")
    assert result == ["()"]


def test_multiple_groups():
    result = separate_paren_groups("() () ()")
    assert result == ["()", "()", "()"]


def test_nested_groups():
    result = separate_paren_groups("(()) ((()))")
    assert result == ["(())", "((()))"]


def test_mixed_depth_and_separators():
    result = separate_paren_groups("(()()) ((())) ()")
    assert result == ["(()())", "((()))", "()"]


def test_empty_string_returns_empty_list():
    result = separate_paren_groups("")
    assert result == []


def test_only_separators_returns_empty_list():
    result = separate_paren_groups("   ")
    assert result == []


def test_non_paren_characters_are_ignored():
    result = separate_paren_groups("( ) (a)")
    assert result == ["()", "()"]


def test_result_is_fresh_list_each_call():
    first = separate_paren_groups("()")
    second = separate_paren_groups("()")
    assert first == ["()"]
    assert second == ["()"]
    assert first is not second
