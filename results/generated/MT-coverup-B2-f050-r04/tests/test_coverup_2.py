# file: project/f050/__init__.py:6-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

"""Tests for f050.decode_shift (line 8: the list-comprehension return statement)."""

from f050 import decode_shift, encode_shift


def test_decode_shift_empty_string():
    """Empty input still executes the join/comprehension on line 8."""
    assert decode_shift("") == ""


def test_decode_shift_single_character():
    """Single lowercase character is shifted back by 5."""
    assert decode_shift("a") == "v"
    assert decode_shift("h") == "c"


def test_decode_shift_wraparound():
    """Characters near the start of the alphabet wrap around to 'z'."""
    assert decode_shift("e") == "z"
    assert decode_shift("f") == "a"


def test_decode_shift_word():
    """A multi-character string decodes correctly."""
    assert decode_shift("hello") == "czggj"


def test_decode_shift_full_alphabet():
    """Every letter of the alphabet maps to the letter 5 positions earlier."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    expected = "vwxyzabcdefghijklmnopqrstu"
    assert decode_shift(alphabet) == expected


def test_decode_shift_roundtrip_with_encode():
    """decode_shift inverts encode_shift for lowercase-letter strings.

    Note: the shift functions are only invertible on lowercase letters
    (non-letter characters like spaces are not preserved), so only
    lowercase-letter inputs are used here.
    """
    for s in ("", "a", "hello", "xyz", "q", "abcdefghijklmnopqrstuvwxyz"):
        assert decode_shift(encode_shift(s)) == s
