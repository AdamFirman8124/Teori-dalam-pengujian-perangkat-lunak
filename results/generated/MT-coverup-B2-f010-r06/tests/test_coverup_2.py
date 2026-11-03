# file: project/f010/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f010 import is_palindrome


def test_palindrome_returns_true():
    """A symmetric string must be reported as a palindrome (covers line 3, True branch)."""
    assert is_palindrome("racecar") is True


def test_non_palindrome_returns_false():
    """An asymmetric string must not be reported as a palindrome (covers line 3, False branch)."""
    assert is_palindrome("hello") is False


def test_empty_string_is_palindrome():
    """The empty string is trivially a palindrome."""
    assert is_palindrome("") is True


def test_single_character_is_palindrome():
    """A single character is trivially a palindrome."""
    assert is_palindrome("a") is True


def test_even_length_palindrome():
    """An even-length symmetric string is a palindrome."""
    assert is_palindrome("abba") is True


def test_even_length_non_palindrome():
    """An even-length asymmetric string is not a palindrome."""
    assert is_palindrome("ab") is False


def test_result_is_bool():
    """The function must return actual bool values, not arbitrary truthy/falsy objects."""
    assert isinstance(is_palindrome("aba"), bool)
    assert isinstance(is_palindrome("abc"), bool)
