# file: script_66.py:1-15
# asked: {"lines": [14, 15], "branches": [[14, 14], [14, 15]]}
# gained: {"lines": [14, 15], "branches": [[14, 14], [14, 15]]}

import pytest
from script_66 import digitSum


def test_digitSum_empty_string():
    """Test empty string returns 0 - covers line 14"""
    result = digitSum("")
    assert result == 0


def test_digitSum_non_empty_string():
    """Test non-empty string - covers line 15"""
    result = digitSum("abAB")
    assert result == 131


def test_digitSum_single_uppercase():
    """Test string with single uppercase letter"""
    result = digitSum("abcCd")
    assert result == 67


def test_digitSum_uppercase_at_end():
    """Test string with uppercase at the end"""
    result = digitSum("helloE")
    assert result == 69


def test_digitSum_multiple_uppercase():
    """Test string with multiple uppercase letters"""
    result = digitSum("woArBld")
    assert result == 131


def test_digitSum_multiple_same_uppercase():
    """Test string with multiple same uppercase letters"""
    result = digitSum("aAaaaXa")
    assert result == 153


def test_digitSum_only_lowercase():
    """Test string with only lowercase letters"""
    result = digitSum("abcdef")
    assert result == 0


def test_digitSum_only_uppercase():
    """Test string with only uppercase letters"""
    result = digitSum("ABC")
    assert result == ord('A') + ord('B') + ord('C')
    assert result == 198


def test_digitSum_with_numbers():
    """Test string with numbers"""
    result = digitSum("abc123DEF")
    assert result == ord('D') + ord('E') + ord('F')
    assert result == 207


def test_digitSum_with_special_characters():
    """Test string with special characters"""
    result = digitSum("a!B@C#")
    assert result == ord('B') + ord('C')
    assert result == 133
