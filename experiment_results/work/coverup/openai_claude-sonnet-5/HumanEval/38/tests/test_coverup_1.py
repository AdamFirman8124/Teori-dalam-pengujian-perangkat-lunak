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
    """Test decode_cyclic with three characters that form one group."""
    encoded = encode_cyclic("abc")
    assert decode_cyclic(encoded) == "abc"


def test_decode_cyclic_multiple_groups():
    """Test decode_cyclic with string containing multiple groups of three."""
    original = "abcdef"
    encoded = encode_cyclic(original)
    assert decode_cyclic(encoded) == original


def test_decode_cyclic_with_remainder():
    """Test decode_cyclic with string that has remainder after grouping by 3."""
    original = "abcdefgh"
    encoded = encode_cyclic(original)
    assert decode_cyclic(encoded) == original


def test_decode_cyclic_long_string():
    """Test decode_cyclic with longer string."""
    original = "thequickbrownfoxjumpsoverthelazydog"
    encoded = encode_cyclic(original)
    assert decode_cyclic(encoded) == original
