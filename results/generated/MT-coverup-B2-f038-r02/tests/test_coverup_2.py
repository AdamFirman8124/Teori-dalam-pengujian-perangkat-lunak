# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

import pytest

from f038 import decode_cyclic, encode_cyclic


def test_decode_cyclic_roundtrip():
    s = "abcdefghij"
    encoded = encode_cyclic(s)
    assert decode_cyclic(encoded) == s


def test_decode_cyclic_known_value():
    # encode_cyclic rotates each 3-char group left by 1; applying it twice
    # (as decode_cyclic does) rotates left by 2, i.e. right by 1.
    assert decode_cyclic("abc") == "cab"
    assert decode_cyclic("abcdef") == "cabfde"
    # groups shorter than 3 chars are left untouched by encode_cyclic
    assert decode_cyclic("ab") == "ab"
    assert decode_cyclic("") == ""


def test_decode_cyclic_is_inverse_of_encode():
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdefg", "xyzxyz"]:
        assert decode_cyclic(encode_cyclic(s)) == s
