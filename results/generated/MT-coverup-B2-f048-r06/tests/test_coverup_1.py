# file: project/f048/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

from f048 import is_palindrome


def test_empty_string_is_palindrome():
    assert is_palindrome("") is True


def test_single_char_is_palindrome():
    assert is_palindrome("a") is True


def test_odd_length_palindrome():
    assert is_palindrome("racecar") is True


def test_even_length_palindrome():
    assert is_palindrome("abba") is True


def test_non_palindrome_returns_false():
    assert is_palindrome("hello") is False


def test_two_char_non_palindrome_returns_false():
    assert is_palindrome("ab") is False
