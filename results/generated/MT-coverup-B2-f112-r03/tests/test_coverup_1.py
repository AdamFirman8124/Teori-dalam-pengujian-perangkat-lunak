# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f112 import reverse_delete


def test_reverse_delete_filters_non_palindrome():
    assert reverse_delete("abcde", "ae") == ("bcd", False)


def test_reverse_delete_filters_to_palindrome():
    assert reverse_delete("abcdedcba", "ab") == ("cdedc", True)


def test_reverse_delete_no_deletion_palindrome():
    assert reverse_delete("aba", "c") == ("aba", True)


def test_reverse_delete_all_deleted_empty_is_palindrome():
    assert reverse_delete("aaa", "a") == ("", True)


def test_reverse_delete_empty_input():
    assert reverse_delete("", "abc") == ("", True)
