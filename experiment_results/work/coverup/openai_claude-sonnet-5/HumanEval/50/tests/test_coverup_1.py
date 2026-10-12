# file: script_50.py:1-5
# asked: {"lines": [5], "branches": []}
# gained: {"lines": [5], "branches": []}

import pytest
from script_50 import encode_shift


def test_encode_shift_empty_string():
    """Test encoding an empty string."""
    assert encode_shift("") == ""


def test_encode_shift_single_character():
    """Test encoding a single character."""
    assert encode_shift("a") == "f"
    assert encode_shift("z") == "e"


def test_encode_shift_multiple_characters():
    """Test encoding multiple characters."""
    assert encode_shift("abc") == "fgh"
    assert encode_shift("xyz") == "cde"


def test_encode_shift_wraps_around():
    """Test that encoding wraps around the alphabet."""
    assert encode_shift("vwxyz") == "abcde"


def test_encode_shift_full_alphabet():
    """Test encoding the full alphabet."""
    assert encode_shift("abcdefghijklmnopqrstuvwxyz") == "fghijklmnopqrstuvwxyzabcde"
