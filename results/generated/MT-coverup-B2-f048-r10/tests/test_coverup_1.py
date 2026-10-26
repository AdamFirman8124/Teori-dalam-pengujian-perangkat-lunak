# file: project/f048/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

from f048 import is_palindrome


def test_is_palindrome_returns_true_for_palindrome():
    assert is_palindrome("racecar") is True


def test_is_palindrome_returns_false_for_non_palindrome():
    assert is_palindrome("python") is False
