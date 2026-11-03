# file: project/f010/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f010 import is_palindrome


def test_is_palindrome_true_cases():
    """Cover line 3 with inputs where string == reversed string (True branch)."""
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("racecar") is True
    assert is_palindrome("abba") is True


def test_is_palindrome_false_cases():
    """Cover line 3 with inputs where string != reversed string (False branch)."""
    assert is_palindrome("hello") is False
    assert is_palindrome("ab") is False
    assert is_palindrome("race a car") is False
