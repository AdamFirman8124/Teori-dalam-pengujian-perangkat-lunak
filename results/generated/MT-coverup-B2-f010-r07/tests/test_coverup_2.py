# file: project/f010/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f010.is_palindrome.

The function under test is pure (no I/O, no global state), so no
monkeypatching or cleanup is required; each test simply calls the
function and asserts on its return value.
"""

from f010 import is_palindrome


def test_is_palindrome_true():
    """A symmetric string must be reported as a palindrome (executes line 3)."""
    assert is_palindrome("racecar") is True


def test_is_palindrome_false():
    """A non-symmetric string must be reported as not a palindrome."""
    assert is_palindrome("hello") is False


def test_is_palindrome_empty_string():
    """The empty string is trivially a palindrome."""
    assert is_palindrome("") is True


def test_is_palindrome_single_character():
    """A single character is trivially a palindrome."""
    assert is_palindrome("x") is True


def test_is_palindrome_even_length():
    """Even-length palindromes are detected."""
    assert is_palindrome("abba") is True


def test_is_palindrome_case_sensitive():
    """Comparison is case-sensitive, so mixed case is not a palindrome."""
    assert is_palindrome("Abba") is False
