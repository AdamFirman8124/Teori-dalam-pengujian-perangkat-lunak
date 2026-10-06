# file: script_10.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest
from script_10 import is_palindrome


def test_is_palindrome_with_palindrome():
    """Test that a palindrome string returns True"""
    assert is_palindrome("racecar") is True


def test_is_palindrome_with_non_palindrome():
    """Test that a non-palindrome string returns False"""
    assert is_palindrome("hello") is False


def test_is_palindrome_with_empty_string():
    """Test that an empty string returns True (empty string is a palindrome)"""
    assert is_palindrome("") is True


def test_is_palindrome_with_single_character():
    """Test that a single character returns True"""
    assert is_palindrome("a") is True


def test_is_palindrome_with_even_length_palindrome():
    """Test that an even-length palindrome returns True"""
    assert is_palindrome("abba") is True


def test_is_palindrome_with_mixed_case():
    """Test palindrome check is case-sensitive"""
    assert is_palindrome("Aa") is False
