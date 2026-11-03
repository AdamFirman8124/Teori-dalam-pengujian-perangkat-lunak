# file: project/f048/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f048 import is_palindrome


def test_is_palindrome_true():
    """A palindrome must return True (exercises the final `return True` line)."""
    assert is_palindrome("racecar") is True
    assert is_palindrome("abba") is True
    assert is_palindrome("aba") is True


def test_is_palindrome_false():
    """A non-palindrome must return False (exercises the early `return False` line)."""
    assert is_palindrome("hello") is False
    assert is_palindrome("ab") is False
    assert is_palindrome("abca") is False


def test_is_palindrome_empty_string():
    """Empty string: loop body never runs, falls through to `return True`."""
    assert is_palindrome("") is True


def test_is_palindrome_single_char():
    """Single character: loop runs once, comparison passes, returns True."""
    assert is_palindrome("x") is True


def test_is_palindrome_mismatch_on_first_char():
    """Mismatch detected on the very first iteration (i == 0)."""
    assert is_palindrome("ab") is False


def test_is_palindrome_mismatch_on_last_iteration():
    """Mismatch detected on the final iteration of the loop."""
    assert is_palindrome("aab") is False


def test_is_palindrome_mismatch_on_inner_char():
    """String whose first and last chars match but an inner char mismatches its mirror."""
    assert is_palindrome("abcda") is False
