# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

import pytest

from f038 import decode_cyclic, encode_cyclic


def test_decode_cyclic_roundtrip():
    s = "abcdefghi"
    encoded = encode_cyclic(s)
    assert decode_cyclic(encoded) == s


def test_decode_cyclic_known_value():
    # encode_cyclic rotates each group of 3 left by one: "abc" -> "bca".
    # Applying it twice rotates left by two (i.e. right by one), so decoding
    # "abc" yields "cab".
    assert decode_cyclic("abc") == "cab"


def test_decode_cyclic_idempotent_inverse():
    # decode(encode(x)) == x and decode(decode(encode(encode(x)))) == x
    s = "abcdef"
    once = decode_cyclic(encode_cyclic(s))
    twice = decode_cyclic(decode_cyclic(encode_cyclic(encode_cyclic(s))))
    assert once == s
    assert twice == s
