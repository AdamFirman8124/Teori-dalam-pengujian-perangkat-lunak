# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

import pytest
from script_1 import separate_paren_groups


def test_single_group():
    result = separate_paren_groups("()")
    assert result == ["()"]


def test_multiple_groups():
    result = separate_paren_groups("()()") 
    assert result == ["()", "()"]


def test_nested_groups():
    result = separate_paren_groups("((()))")
    assert result == ["((()))"]


def test_multiple_nested_groups():
    result = separate_paren_groups("((()))(())")
    assert result == ["((()))", "(())"]


def test_complex_nesting():
    result = separate_paren_groups("(()(()))")
    assert result == ["(()(()))"]


def test_multiple_complex_groups():
    result = separate_paren_groups("(()())((()))")
    assert result == ["(()())", "((()))"]


def test_empty_string():
    result = separate_paren_groups("")
    assert result == []


def test_spaces_between_groups():
    result = separate_paren_groups("() ()")
    assert result == ["()", "()"]


def test_deep_nesting():
    result = separate_paren_groups("(((())))")
    assert result == ["(((())))"]
