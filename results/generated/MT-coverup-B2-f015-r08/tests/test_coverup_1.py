# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f015 import string_sequence


def test_string_sequence_zero():
    """n = 0 should produce just '0'."""
    result = string_sequence(0)
    assert result == "0"


def test_string_sequence_positive():
    """n = 5 should produce numbers 0 through 5 joined by spaces."""
    result = string_sequence(5)
    assert result == "0 1 2 3 4 5"


def test_string_sequence_one():
    """n = 1 should produce '0 1'."""
    result = string_sequence(1)
    assert result == "0 1"


def test_string_sequence_negative():
    """Negative n yields an empty range, so the result is an empty string."""
    result = string_sequence(-1)
    assert result == ""


def test_string_sequence_type():
    """The result must always be a string."""
    assert isinstance(string_sequence(3), str)
