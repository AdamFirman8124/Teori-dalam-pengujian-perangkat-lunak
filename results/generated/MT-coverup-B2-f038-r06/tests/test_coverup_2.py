# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

import pytest

from f038 import decode_cyclic, encode_cyclic


@pytest.mark.parametrize(
    "s",
    [
        "",                # empty string (no groups at all)
        "a",               # single character -> partial group branch
        "ab",              # two characters -> partial group branch
        "abc",             # exactly one full group
        "abcd",            # one full group + partial group
        "abcdef",          # two full groups
        "abcdefghi",       # three full groups
        "Hello, World!",   # mixed content with trailing partial group
        "xyzxyzxyz",       # repeated identical groups
    ],
)
def test_decode_cyclic_roundtrip(s):
    """decode_cyclic must invert encode_cyclic for any input."""
    encoded = encode_cyclic(s)
    assert decode_cyclic(encoded) == s


def test_decode_cyclic_known_value():
    """encode_cyclic('abcdef') == 'bcaefd'; decoding must restore 'abcdef'."""
    assert decode_cyclic("bcaefd") == "abcdef"


def test_decode_cyclic_is_double_encode():
    """decode_cyclic(s) is equivalent to applying encode_cyclic twice."""
    s = "abcdefgh"
    assert decode_cyclic(s) == encode_cyclic(encode_cyclic(s))


def test_decode_cyclic_inverse_of_encode():
    """Both directions of the round trip must hold."""
    s = "The quick brown fox jumps over the lazy dog"
    assert decode_cyclic(encode_cyclic(s)) == s
    assert encode_cyclic(decode_cyclic(s)) == s
