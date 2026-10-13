# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

from script_1 import separate_paren_groups

def test_single_group():
    assert separate_paren_groups("()") == ["()"]

def test_multiple_groups():
    assert separate_paren_groups("()()") == ["()", "()"]

def test_nested_group():
    assert separate_paren_groups("(())") == ["(())"]

def test_nested_then_sibling():
    assert separate_paren_groups("(())(())") == ["(())", "(())"]

def test_empty_string():
    assert separate_paren_groups("") == []

def test_no_parens():
    assert separate_paren_groups("   ") == []

def test_whitespace_between_groups():
    assert separate_paren_groups("() ()") == ["()", "()"]

def test_non_paren_characters_ignored():
    assert separate_paren_groups("(ab)") == ["()"]

def test_deep_nesting():
    assert separate_paren_groups("((()))") == ["((()))"]

def test_nested_with_inner_characters():
    assert separate_paren_groups("(a(b)c)") == ["(())"]
