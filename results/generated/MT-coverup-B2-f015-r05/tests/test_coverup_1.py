# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f015 import string_sequence


def test_string_sequence_zero():
    """string_sequence(0) must return just '0' (single element, no separator)."""
    result = string_sequence(0)
    assert result == '0'
    assert result.split() == [str(x) for x in range(0 + 1)]


def test_string_sequence_positive():
    """string_sequence(5) must return the numbers 0..5 joined by single spaces."""
    result = string_sequence(5)
    assert result == '0 1 2 3 4 5'
    assert result.split() == [str(x) for x in range(5 + 1)]
    assert len(result.split()) == 6


def test_string_sequence_negative():
    """string_sequence(-1) must return an empty string, since range(0) is empty."""
    result = string_sequence(-1)
    assert result == ''
    assert result.split() == []
