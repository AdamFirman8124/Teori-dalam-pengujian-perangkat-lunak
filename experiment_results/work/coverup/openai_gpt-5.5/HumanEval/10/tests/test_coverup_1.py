# file: script_10.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from script_10 import is_palindrome


def test_is_palindrome_returns_true_for_palindromes():
    assert is_palindrome("racecar") is True
    assert is_palindrome("") is True


def test_is_palindrome_returns_false_for_non_palindromes():
    assert is_palindrome("python") is False
