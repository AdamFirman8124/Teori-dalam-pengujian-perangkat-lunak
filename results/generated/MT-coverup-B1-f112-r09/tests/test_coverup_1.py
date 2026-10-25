# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f112 import reverse_delete


def test_reverse_delete_removes_chars_and_checks_palindrome():
    result, is_palindrome = reverse_delete("abcde", "ae")
    assert result == "bcd"
    assert is_palindrome is False


def test_reverse_delete_palindrome_true():
    result, is_palindrome = reverse_delete("abcdedcba", "x")
    assert result == "abcdedcba"
    assert is_palindrome is True


def test_reverse_delete_becomes_palindrome_after_deletion():
    result, is_palindrome = reverse_delete("abca", "a")
    assert result == "bc"
    assert is_palindrome is False


def test_reverse_delete_empty_result_is_palindrome():
    result, is_palindrome = reverse_delete("abc", "abc")
    assert result == ""
    assert is_palindrome is True
