# file: project/f048/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f048 import is_palindrome


def test_is_palindrome_true():
    """A palindrome returns True: exercises the loop (line 3), the
    comparison (line 4) and the final return True (line 6)."""
    assert is_palindrome("racecar") is True
    assert is_palindrome("abba") is True
    assert is_palindrome("ab") is False  # even-length non-palindrome


def test_is_palindrome_false():
    """A non-palindrome returns False: exercises the early return False
    branch (line 5)."""
    assert is_palindrome("hello") is False
    assert is_palindrome("abca") is False


def test_is_palindrome_empty():
    """The empty string is a palindrome: the loop body never runs and
    control falls through to return True (line 6)."""
    assert is_palindrome("") is True


def test_is_palindrome_single_char():
    """A single character is a palindrome: one loop iteration whose
    comparison trivially succeeds."""
    assert is_palindrome("x") is True
