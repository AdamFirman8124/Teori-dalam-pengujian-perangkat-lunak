# file: project/f050/__init__.py:6-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

from f050 import decode_shift, encode_shift


def test_decode_shift_executes_line_8():
    """Calling decode_shift with a non-empty string executes line 8 and
    covers both branches of the comprehension loop (enter + exhaust)."""
    # 'h'->'c', 'e'->'z', 'l'->'g', 'l'->'g', 'o'->'j'
    assert decode_shift("hello") == "czggj"


def test_decode_shift_wraparound():
    """Characters near the start of the alphabet wrap around modulo 26."""
    assert decode_shift("abc") == "vwx"
    assert decode_shift("fghij") == "abcde"


def test_decode_shift_empty_string():
    """Line 8 also executes for an empty input (join over empty list)."""
    assert decode_shift("") == ""


def test_decode_shift_roundtrip_with_encode():
    """decode_shift must invert encode_shift exactly for lowercase letters.

    Note: the cipher only maps 'a'-'z' correctly (any other character is
    shifted modulo 26 relative to 'a'), so the roundtrip input must be
    restricted to lowercase letters.
    """
    original = "helloworld"
    assert encode_shift(original) == "mjqqtbtwqi"
    assert decode_shift(encode_shift(original)) == original
