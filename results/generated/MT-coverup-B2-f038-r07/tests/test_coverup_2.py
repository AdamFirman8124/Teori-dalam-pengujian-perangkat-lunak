# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

"""Tests for f038.decode_cyclic (executes line 12: the return statement).

The functions under test are pure (no I/O, no globals, no side effects),
so no monkeypatching or cleanup is required to avoid state pollution.
"""

import pytest

from f038 import decode_cyclic, encode_cyclic


def test_decode_cyclic_roundtrip_length_multiple_of_three():
    # encode_cyclic rotates each 3-char group left by one; decoding applies
    # the rotation twice more, restoring the original string.
    s = "abcdef"
    encoded = encode_cyclic(s)
    assert encoded == "bcaefd"
    assert decode_cyclic(encoded) == s


def test_decode_cyclic_roundtrip_length_not_multiple_of_three():
    # Trailing groups of length 1 or 2 are left untouched by encode_cyclic,
    # so the round-trip still holds for other lengths.
    s = "abcdefgh"
    encoded = encode_cyclic(s)
    assert encoded == "bcaefdgh"
    assert decode_cyclic(encoded) == s


def test_decode_cyclic_direct_value():
    # Decoding is equivalent to a right-rotation of each full 3-char group:
    # "abc" -> "cab", "def" -> "fde".
    assert decode_cyclic("abcdef") == "cabfde"


def test_decode_cyclic_short_and_empty_strings():
    # Edge cases: empty string and strings shorter than one full group.
    assert decode_cyclic("") == ""
    assert decode_cyclic("a") == "a"
    assert decode_cyclic("ab") == "ab"
