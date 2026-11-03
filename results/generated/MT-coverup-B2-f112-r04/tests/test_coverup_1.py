# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f112 import reverse_delete


def test_removes_chars_not_palindrome():
    """Characters in c are deleted from s; result is not a palindrome."""
    result = reverse_delete("abcde", "ae")
    assert result == ("bcd", False)
    assert result[0] == "bcd"
    assert result[1] is False


def test_palindrome_after_deletion():
    """After deleting chars in c, the remaining string is a palindrome."""
    result = reverse_delete("abcdedcba", "ab")
    assert result == ("cdedc", True)
    assert result[0] == "cdedc"
    assert result[1] is True


def test_all_chars_removed_empty_string_is_palindrome():
    """Deleting every character yields the empty string, a palindrome."""
    result = reverse_delete("abc", "abc")
    assert result == ("", True)
    assert result[0] == ""
    assert result[1] is True


def test_no_chars_removed_not_palindrome():
    """When c shares no characters with s, s is unchanged."""
    result = reverse_delete("abc", "xyz")
    assert result == ("abc", False)
    assert result[0] == "abc"
    assert result[1] is False


def test_empty_s():
    """Empty input string yields empty result and True palindrome flag."""
    result = reverse_delete("", "abc")
    assert result == ("", True)


@pytest.mark.parametrize(
    "s,c,expected",
    [
        ("abcde", "ae", ("bcd", False)),
        ("abcdef", "b", ("acdef", False)),
        ("aba", "b", ("aa", True)),
        ("abba", "ab", ("", True)),
        ("madamimadam", "z", ("madamimadam", True)),
    ],
)
def test_reverse_delete_parametrized(s, c, expected):
    assert reverse_delete(s, c) == expected
