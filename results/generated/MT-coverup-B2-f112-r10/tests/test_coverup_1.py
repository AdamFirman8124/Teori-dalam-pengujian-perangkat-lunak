# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f112 import reverse_delete


def test_reverse_delete_removes_chars_non_palindrome():
    """Characters listed in c are deleted; result string and palindrome flag returned."""
    result, is_palindrome = reverse_delete("abcde", "ae")
    assert result == "bcd"
    assert is_palindrome is False


def test_reverse_delete_result_is_palindrome():
    """When the filtered string reads the same forwards and backwards, flag is True."""
    result, is_palindrome = reverse_delete("abcdedcba", "ab")
    assert result == "cdedc"
    assert is_palindrome is True


def test_reverse_delete_all_chars_removed_empty_palindrome():
    """Removing every character yields the empty string, which is a palindrome."""
    result, is_palindrome = reverse_delete("abc", "abc")
    assert result == ""
    assert is_palindrome is True


def test_reverse_delete_no_chars_to_remove():
    """When c shares no characters with s, s is unchanged and flagged non-palindrome."""
    result, is_palindrome = reverse_delete("abba", "xyz")
    assert result == "abba"
    assert is_palindrome is True
