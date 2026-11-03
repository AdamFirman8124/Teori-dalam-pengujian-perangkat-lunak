# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f112 import reverse_delete


def test_reverse_delete_removes_chars_result_not_palindrome():
    """Characters in c are removed from s; remaining string is not a palindrome."""
    result = reverse_delete("abcde", "ae")
    assert result == ("bcd", False)
    assert result[0] == "bcd"
    assert result[1] is False


def test_reverse_delete_removes_chars_result_palindrome():
    """Characters in c are removed from s; remaining string is a palindrome."""
    result = reverse_delete("abcdedcba", "ab")
    assert result == ("cdedc", True)
    assert result[0] == "cdedc"
    assert result[1] is True


def test_reverse_delete_all_chars_removed_empty_string_is_palindrome():
    """When every character is removed, the empty string counts as a palindrome."""
    result = reverse_delete("abc", "abc")
    assert result == ("", True)
    assert result[0] == ""
    assert result[1] is True


def test_reverse_delete_no_chars_removed_not_palindrome():
    """When no character of s appears in c, s is returned unchanged."""
    result = reverse_delete("hello", "xyz")
    assert result == ("hello", False)
    assert result[0] == "hello"
    assert result[1] is False


def test_reverse_delete_empty_s():
    """An empty s yields an empty (palindromic) string."""
    result = reverse_delete("", "a")
    assert result == ("", True)
    assert result[0] == ""
    assert result[1] is True


def test_reverse_delete_duplicate_chars_in_c():
    """Duplicate characters in c are handled correctly (each removed once per occurrence)."""
    result = reverse_delete("aabbcc", "abc")
    assert result == ("", True)
    assert result[0] == ""
    assert result[1] is True
