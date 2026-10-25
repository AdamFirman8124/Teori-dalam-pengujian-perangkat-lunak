# file: project/f010/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f010 import is_palindrome


def test_is_palindrome_with_palindrome():
    assert is_palindrome("racecar") is True


def test_is_palindrome_with_non_palindrome():
    assert is_palindrome("hello") is False


def test_is_palindrome_with_empty_string():
    assert is_palindrome("") is True


def test_is_palindrome_with_single_character():
    assert is_palindrome("a") is True


def test_is_palindrome_is_case_sensitive():
    assert is_palindrome("Racecar") is False


def test_is_palindrome_with_numeric_string():
    assert is_palindrome("12321") is True
    assert is_palindrome("12345") is False
