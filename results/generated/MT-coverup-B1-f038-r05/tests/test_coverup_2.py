# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

from f038 import decode_cyclic, encode_cyclic


def test_decode_cyclic_reverses_encode_cyclic():
    original = "abcdefgh"
    encoded = encode_cyclic(original)

    assert encoded == "bcaefdgh"
    assert decode_cyclic(encoded) == original
