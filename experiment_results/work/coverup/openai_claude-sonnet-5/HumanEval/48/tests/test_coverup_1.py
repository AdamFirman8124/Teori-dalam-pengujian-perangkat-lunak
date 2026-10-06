# file: script_48.py:1-16
# asked: {"lines": [13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}
# gained: {"lines": [13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}

import pytest
from script_48 import is_palindrome


def test_is_palindrome_empty_string():
    """Test empty string is a palindrome"""
    assert is_palindrome('') is True


def test_is_palindrome_single_character():
    """Test single character is a palindrome"""
    assert is_palindrome('a') is True


def test_is_palindrome_odd_length_palindrome():
    """Test odd length palindrome"""
    assert is_palindrome('aba') is True
    assert is_palindrome('racecar') is True


def test_is_palindrome_even_length_palindrome():
    """Test even length palindrome"""
    assert is_palindrome('aa') is True
    assert is_palindrome('abba') is True


def test_is_palindrome_not_palindrome():
    """Test non-palindrome strings"""
    assert is_palindrome('ab') is False
    assert is_palindrome('zbcd') is False
    assert is_palindrome('abc') is False
