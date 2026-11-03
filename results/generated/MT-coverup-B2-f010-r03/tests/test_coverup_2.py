# file: project/f010/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f010 import is_palindrome


def test_is_palindrome_true():
    """A palindrome string must be recognized as such (executes line 3)."""
    assert is_palindrome("racecar") is True


def test_is_palindrome_false():
    """A non-palindrome string must not be recognized as a palindrome."""
    assert is_palindrome("hello") is False


def test_is_palindrome_empty_string():
    """The empty string is trivially a palindrome."""
    assert is_palindrome("") is True


def test_is_palindrome_single_char():
    """A single character is always a palindrome."""
    assert is_palindrome("x") is True


def test_is_palindrome_case_sensitive():
    """Comparison is exact, so case differences make it a non-palindrome."""
    assert is_palindrome("Racecar") is False
