# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

import pytest

from f038 import decode_cyclic, encode_cyclic


@pytest.mark.parametrize(
    "s",
    [
        "",              # empty string (no groups)
        "a",             # single partial group (len < 3 branch)
        "ab",            # partial group (len < 3 branch)
        "abc",           # exactly one full group (len == 3 branch)
        "abcd",          # one full group + one partial group
        "abcdef",        # two full groups
        "abcdefghi",     # three full groups
        "hello world",   # arbitrary text with mixed group sizes
        "xyzxyzxyz",     # repeated identical groups
    ],
)
def test_decode_cyclic_roundtrip(s):
    # decode_cyclic must invert encode_cyclic
    encoded = encode_cyclic(s)
    assert decode_cyclic(encoded) == s

    # decode_cyclic is defined as encode_cyclic applied twice
    assert decode_cyclic(s) == encode_cyclic(encode_cyclic(s))


def test_decode_cyclic_matches_double_encode_on_known_value():
    # "abc" -> encode -> "bca" -> encode -> "cab"
    assert decode_cyclic("abc") == "cab"
    # partial groups are left untouched by encode, hence by decode too
    assert decode_cyclic("ab") == "ab"
    assert decode_cyclic("") == ""
