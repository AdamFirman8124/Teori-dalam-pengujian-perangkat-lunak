# file: project/f010/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f010.is_palindrome.

The function under test is pure (no I/O, no global state), so no
monkeypatching or teardown is required; each test simply calls the
function and asserts on its return value, which guarantees that
line 3 (`return string == string[::-1]`) is executed.
"""

from f010 import is_palindrome


def test_is_palindrome_true():
    """An odd-length palindrome returns True."""
    assert is_palindrome("racecar") is True


def test_is_palindrome_even_length_true():
    """An even-length palindrome returns True."""
    assert is_palindrome("abba") is True


def test_is_palindrome_false():
    """A non-palindrome returns False."""
    assert is_palindrome("hello") is False


def test_is_palindrome_empty_string():
    """The empty string is trivially a palindrome."""
    assert is_palindrome("") is True


def test_is_palindrome_single_character():
    """A single character is trivially a palindrome."""
    assert is_palindrome("x") is True


def test_is_palindrome_case_sensitive():
    """Comparison is case-sensitive, so mixed case is not a palindrome."""
    assert is_palindrome("Abba") is False
