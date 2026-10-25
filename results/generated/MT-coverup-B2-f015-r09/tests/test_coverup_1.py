# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f015 import string_sequence


def test_string_sequence_zero():
    """n = 0 must execute line 3 and return just '0'."""
    result = string_sequence(0)
    assert result == "0"


def test_string_sequence_positive():
    """n = 5 must return numbers 0 through 5 space-separated."""
    result = string_sequence(5)
    assert result == "0 1 2 3 4 5"
    assert len(result.split()) == 6


def test_string_sequence_returns_string():
    """Postcondition: result is a str of space-separated ints."""
    result = string_sequence(3)
    assert isinstance(result, str)
    assert result == "0 1 2 3"
    assert all(part.isdigit() for part in result.split())
