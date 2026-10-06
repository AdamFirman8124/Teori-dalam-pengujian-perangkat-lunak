# file: script_112.py:1-13
# asked: {"lines": [12, 13], "branches": []}
# gained: {"lines": [12, 13], "branches": []}

import pytest
from script_112 import reverse_delete


def test_reverse_delete_with_deletions_palindrome():
    """Test case where deletions result in a palindrome"""
    result = reverse_delete("abcdedcba", "ab")
    assert result == ('cdedc', True)


def test_reverse_delete_with_deletions_not_palindrome():
    """Test case where deletions result in non-palindrome"""
    result = reverse_delete("abcde", "ae")
    assert result == ('bcd', False)


def test_reverse_delete_single_char_deletion():
    """Test case with single character deletion"""
    result = reverse_delete("abcdef", "b")
    assert result == ('acdef', False)


def test_reverse_delete_empty_result():
    """Test case where all characters are deleted"""
    result = reverse_delete("aaa", "a")
    assert result == ('', True)


def test_reverse_delete_no_deletions_palindrome():
    """Test case where no deletions occur and string is palindrome"""
    result = reverse_delete("racecar", "xyz")
    assert result == ('racecar', True)


def test_reverse_delete_no_deletions_not_palindrome():
    """Test case where no deletions occur and string is not palindrome"""
    result = reverse_delete("hello", "xyz")
    assert result == ('hello', False)


def test_reverse_delete_all_deleted():
    """Test case where deletion set contains all characters"""
    result = reverse_delete("abc", "abc")
    assert result == ('', True)


def test_reverse_delete_single_char_result_palindrome():
    """Test case resulting in single character (always palindrome)"""
    result = reverse_delete("abcde", "abde")
    assert result == ('c', True)
