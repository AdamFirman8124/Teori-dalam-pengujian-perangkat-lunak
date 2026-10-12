# file: script_10.py:6-26
# asked: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}
# gained: {"lines": [18, 19, 21, 23, 24, 26], "branches": [[18, 19], [18, 21], [23, 24], [23, 26]]}

import pytest
from script_10 import make_palindrome, is_palindrome


def test_make_palindrome_empty_string():
    """Test with empty string - covers lines 18-19."""
    assert make_palindrome('') == ''


def test_make_palindrome_single_character():
    """Test with single character - already a palindrome."""
    assert make_palindrome('a') == 'a'


def test_make_palindrome_cat():
    """Test with 'cat' - covers lines 21, 23-24, 26."""
    result = make_palindrome('cat')
    assert result == 'catac'
    assert is_palindrome(result)
    assert result.startswith('cat')


def test_make_palindrome_cata():
    """Test with 'cata' - string ending in palindrome."""
    result = make_palindrome('cata')
    assert result == 'catac'
    assert is_palindrome(result)
    assert result.startswith('cata')


def test_make_palindrome_already_palindrome():
    """Test with string that is already a palindrome."""
    result = make_palindrome('racecar')
    assert result == 'racecar'
    assert is_palindrome(result)


def test_make_palindrome_two_characters():
    """Test with two different characters."""
    result = make_palindrome('ab')
    assert result == 'aba'
    assert is_palindrome(result)
    assert result.startswith('ab')


def test_make_palindrome_xyz():
    """Test with 'xyz' - no palindromic suffix."""
    result = make_palindrome('xyz')
    assert result == 'xyzyx'
    assert is_palindrome(result)
    assert result.startswith('xyz')
