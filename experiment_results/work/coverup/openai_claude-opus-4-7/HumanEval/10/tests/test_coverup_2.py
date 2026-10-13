# file: script_10.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from script_10 import is_palindrome


def test_is_palindrome_true():
    result = is_palindrome("racecar")
    assert result is True


def test_is_palindrome_false():
    result = is_palindrome("hello")
    assert result is False


def test_is_palindrome_empty_string():
    result = is_palindrome("")
    assert result is True


def test_is_palindrome_single_char():
    result = is_palindrome("a")
    assert result is True


def test_is_palindrome_even_length():
    result = is_palindrome("abba")
    assert result is True


def test_is_palindrome_case_sensitive():
    result = is_palindrome("Racecar")
    assert result is False
