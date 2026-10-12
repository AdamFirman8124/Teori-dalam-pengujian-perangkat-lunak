# file: script_48.py:1-16
# asked: {"lines": [13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}
# gained: {"lines": [13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}

import pytest
from script_48 import is_palindrome


def test_is_palindrome_empty_string():
    """Test that empty string is a palindrome"""
    result = is_palindrome('')
    assert result is True


def test_is_palindrome_single_character():
    """Test that single character is a palindrome"""
    result = is_palindrome('a')
    assert result is True


def test_is_palindrome_odd_length():
    """Test palindrome with odd length"""
    result = is_palindrome('aba')
    assert result is True
    result = is_palindrome('racecar')
    assert result is True


def test_is_palindrome_even_length():
    """Test palindrome with even length"""
    result = is_palindrome('aa')
    assert result is True
    result = is_palindrome('abba')
    assert result is True


def test_is_palindrome_all_same_characters():
    """Test palindrome with all same characters"""
    result = is_palindrome('aaaaa')
    assert result is True


def test_is_palindrome_not_palindrome():
    """Test strings that are not palindromes"""
    result = is_palindrome('zbcd')
    assert result is False
    result = is_palindrome('ab')
    assert result is False
    result = is_palindrome('abc')
    assert result is False
