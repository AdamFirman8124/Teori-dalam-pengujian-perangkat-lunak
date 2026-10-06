# file: script_38.py:12-16
# asked: {"lines": [16], "branches": []}
# gained: {"lines": [16], "branches": []}

import pytest
from script_38 import decode_cyclic, encode_cyclic


def test_decode_cyclic_empty_string():
    """Test decode_cyclic with empty string."""
    assert decode_cyclic("") == ""


def test_decode_cyclic_single_char():
    """Test decode_cyclic with single character."""
    assert decode_cyclic("a") == "a"


def test_decode_cyclic_two_chars():
    """Test decode_cyclic with two characters."""
    assert decode_cyclic("ab") == "ab"


def test_decode_cyclic_three_chars():
    """Test decode_cyclic with exactly three characters."""
    encoded = encode_cyclic("abc")
    assert decode_cyclic(encoded) == "abc"


def test_decode_cyclic_six_chars():
    """Test decode_cyclic with six characters (two groups)."""
    encoded = encode_cyclic("abcdef")
    assert decode_cyclic(encoded) == "abcdef"


def test_decode_cyclic_not_divisible_by_three():
    """Test decode_cyclic with string length not divisible by 3."""
    encoded = encode_cyclic("abcde")
    assert decode_cyclic(encoded) == "abcde"


def test_decode_cyclic_long_string():
    """Test decode_cyclic with longer string."""
    original = "hello world"
    encoded = encode_cyclic(original)
    assert decode_cyclic(encoded) == original


def test_decode_cyclic_with_spaces():
    """Test decode_cyclic with spaces."""
    original = "a b c d e f"
    encoded = encode_cyclic(original)
    assert decode_cyclic(encoded) == original


def test_decode_cyclic_with_numbers():
    """Test decode_cyclic with numbers."""
    original = "123456789"
    encoded = encode_cyclic(original)
    assert decode_cyclic(encoded) == original
