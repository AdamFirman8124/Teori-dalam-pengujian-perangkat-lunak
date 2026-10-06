# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

import pytest
from script_1 import separate_paren_groups


def test_separate_paren_groups_single_group():
    """Test with a single balanced parentheses group."""
    result = separate_paren_groups("(())")
    assert result == ["(())"]


def test_separate_paren_groups_multiple_groups():
    """Test with multiple balanced parentheses groups."""
    result = separate_paren_groups("()()()")
    assert result == ["()", "()", "()"]


def test_separate_paren_groups_nested():
    """Test with nested parentheses."""
    result = separate_paren_groups("((()))")
    assert result == ["((()))"]


def test_separate_paren_groups_mixed():
    """Test with mixed nested and sequential groups."""
    result = separate_paren_groups("((()))(())")
    assert result == ["((()))", "(())"]


def test_separate_paren_groups_with_spaces():
    """Test with spaces between groups."""
    result = separate_paren_groups("( ) (( )) (( )( ))")
    assert result == ["()", "(())", "(()())"]


def test_separate_paren_groups_complex():
    """Test with complex nested structure."""
    result = separate_paren_groups("(()())(())")
    assert result == ["(()())", "(())"]


def test_separate_paren_groups_empty_string():
    """Test with empty string."""
    result = separate_paren_groups("")
    assert result == []


def test_separate_paren_groups_deeply_nested():
    """Test with deeply nested parentheses."""
    result = separate_paren_groups("((((()))))")
    assert result == ["((((()))))"]
