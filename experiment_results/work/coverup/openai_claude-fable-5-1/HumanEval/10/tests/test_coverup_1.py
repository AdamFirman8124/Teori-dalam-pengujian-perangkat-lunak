# file: script_10.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from script_10 import is_palindrome


def test_is_palindrome_true():
    assert is_palindrome("racecar") is True
    assert is_palindrome("") is True
    assert is_palindrome("a") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False
    assert is_palindrome("Python") is False
