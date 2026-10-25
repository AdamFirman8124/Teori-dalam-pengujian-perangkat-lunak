# file: project/f010/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f010 import is_palindrome


def test_is_palindrome_simple_true():
    assert is_palindrome("racecar") is True


def test_is_palindrome_simple_false():
    assert is_palindrome("hello") is False


def test_is_palindrome_empty_string():
    assert is_palindrome("") is True


def test_is_palindrome_single_char():
    assert is_palindrome("a") is True


def test_is_palindrome_even_length():
    assert is_palindrome("abba") is True
    assert is_palindrome("abca") is False


def test_is_palindrome_case_sensitive():
    assert is_palindrome("Racecar") is False
    assert is_palindrome("aa") is True
