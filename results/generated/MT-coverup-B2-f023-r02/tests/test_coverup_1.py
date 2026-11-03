# file: project/f023/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f023 import strlen


def test_strlen_returns_length_of_string():
    """Calling strlen must execute line 3 (return len(string)) and return the
    correct length for a non-empty string."""
    assert strlen("hello") == 5


def test_strlen_empty_string():
    """Edge case: empty string should return 0, still exercising line 3."""
    assert strlen("") == 0


def test_strlen_returns_int():
    """Postcondition: the result is an int equal to len of the input."""
    result = strlen("abc")
    assert isinstance(result, int)
    assert result == len("abc")
