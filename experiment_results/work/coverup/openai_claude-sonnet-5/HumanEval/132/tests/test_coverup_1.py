# file: script_132.py:1-29
# asked: {"lines": [14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], "branches": [[16, 17], [16, 21], [17, 18], [17, 20], [25, 26], [25, 29], [26, 25], [26, 27]]}
# gained: {"lines": [14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], "branches": [[16, 17], [16, 21], [17, 18], [17, 20], [25, 26], [25, 29], [26, 25], [26, 27]]}

import pytest
from script_132 import is_nested


def test_nested_basic():
    """Test basic nested brackets"""
    assert is_nested('[[]]') == True


def test_nested_complex():
    """Test complex nested structure"""
    assert is_nested('[[][]]') == True


def test_nested_with_trailing():
    """Test nested with incomplete trailing"""
    assert is_nested('[[]][[') == True


def test_not_nested_empty():
    """Test empty string"""
    assert is_nested('') == False


def test_not_nested_single_pair():
    """Test single pair of brackets"""
    assert is_nested('[]') == False


def test_not_nested_adjacent():
    """Test adjacent non-nested brackets"""
    assert is_nested('[][]') == False


def test_not_nested_unbalanced():
    """Test unbalanced brackets"""
    assert is_nested('[]]]]]]][[[[[]') == False


def test_nested_triple():
    """Test triple nesting"""
    assert is_nested('[[[]]]') == True


def test_nested_multiple_pairs():
    """Test multiple nested pairs"""
    assert is_nested('[[]][[]]') == True


def test_single_opening_bracket():
    """Test single opening bracket"""
    assert is_nested('[') == False


def test_single_closing_bracket():
    """Test single closing bracket"""
    assert is_nested(']') == False


def test_closing_then_opening():
    """Test closing bracket before opening"""
    assert is_nested('][') == False


def test_nested_at_end():
    """Test nested structure at the end"""
    assert is_nested('[][[]]') == True
