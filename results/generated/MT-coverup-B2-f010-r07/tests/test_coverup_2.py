# file: project/f010/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f010 import is_palindrome


def test_is_palindrome_true_cases():
    assert is_palindrome("racecar") is True
    assert is_palindrome("madam") is True
    assert is_palindrome("a") is True
    assert is_palindrome("") is True
    assert is_palindrome("aa") is True
    assert is_palindrome("aba") is True


def test_is_palindrome_false_cases():
    assert is_palindrome("hello") is False
    assert is_palindrome("ab") is False
    assert is_palindrome("racecars") is False
    assert is_palindrome("Racecar") is False
