# file: project/f048/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f048 import is_palindrome


def test_is_palindrome_true():
    """A palindrome should return True (covers loop, comparison, and return True)."""
    assert is_palindrome("racecar") is True
    assert is_palindrome("abba") is True


def test_is_palindrome_false():
    """A non-palindrome should return False (covers the early return False branch)."""
    assert is_palindrome("hello") is False
    assert is_palindrome("racecars") is False


def test_is_palindrome_empty_string():
    """An empty string is a palindrome (loop body never executes, returns True)."""
    assert is_palindrome("") is True


def test_is_palindrome_single_char():
    """A single character is a palindrome."""
    assert is_palindrome("a") is True
