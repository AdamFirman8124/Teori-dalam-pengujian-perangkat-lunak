# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f112 import reverse_delete


def test_reverse_delete_removes_chars_and_checks_palindrome():
    # 'abcde' with 'b' removed -> 'acde', not a palindrome
    result = reverse_delete("abcde", "b")
    assert result == ("acde", False)


def test_reverse_delete_palindrome_true():
    # 'abcdedcba' with 'x' removed -> unchanged, palindrome
    result = reverse_delete("abcdedcba", "x")
    assert result == ("abcdedcba", True)


def test_reverse_delete_all_chars_removed():
    # every char removed -> empty string, which is a palindrome
    result = reverse_delete("abc", "abc")
    assert result == ("", True)


def test_reverse_delete_empty_string():
    result = reverse_delete("", "a")
    assert result == ("", True)
