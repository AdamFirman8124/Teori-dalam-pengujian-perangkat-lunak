# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f112 import reverse_delete


def test_reverse_delete_filters_chars_and_reports_non_palindrome():
    """Characters in c are removed; remaining string is not a palindrome."""
    result = reverse_delete("abcde", "ae")
    assert result == ("bcd", False)
    assert result[0] == "bcd"
    assert result[1] is False


def test_reverse_delete_filters_chars_and_reports_palindrome():
    """Characters in c are removed; remaining string is a palindrome."""
    result = reverse_delete("abcdedcba", "ab")
    assert result == ("cdedc", True)
    assert result[0] == "cdedc"
    assert result[1] is True


def test_reverse_delete_all_chars_removed_yields_empty_palindrome():
    """Removing every character yields the empty string, which is a palindrome."""
    result = reverse_delete("aaaa", "a")
    assert result == ("", True)
    assert result[0] == ""
    assert result[1] is True


def test_reverse_delete_no_chars_removed_non_palindrome():
    """When c shares no characters with s, s is unchanged and not a palindrome."""
    result = reverse_delete("abc", "xyz")
    assert result == ("abc", False)
    assert result[0] == "abc"
    assert result[1] is False
