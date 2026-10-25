# file: project/f050/__init__.py:6-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest

from f050 import decode_shift


def test_decode_shift_basic():
    # 'f' shifted back by 5 becomes 'a'
    assert decode_shift("f") == "a"


def test_decode_shift_full_alphabet():
    # Decoding the alphabet shifts each letter back by 5, wrapping around
    assert decode_shift("abcdefghijklmnopqrstuvwxyz") == "vwxyzabcdefghijklmnopqrstu"


def test_decode_shift_wraparound():
    # Letters at the start of the alphabet wrap around to the end
    assert decode_shift("abcde") == "vwxyz"


def test_decode_shift_empty_string():
    # Empty input yields empty output (list comprehension still executes line 8)
    assert decode_shift("") == ""


def test_decode_shift_roundtrip():
    # Decoding an encoded string recovers the original
    from f050 import encode_shift

    original = "helloworld"
    assert decode_shift(encode_shift(original)) == original
