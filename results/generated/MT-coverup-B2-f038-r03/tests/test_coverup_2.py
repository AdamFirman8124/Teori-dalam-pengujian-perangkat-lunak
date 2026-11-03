# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

import pytest

from f038 import decode_cyclic, encode_cyclic


@pytest.mark.parametrize(
    "s",
    [
        "",
        "a",
        "ab",
        "abc",
        "abcd",
        "abcde",
        "abcdef",
        "abcdefghi",
        "The quick brown fox",
    ],
)
def test_decode_inverts_encode(s):
    """decode_cyclic must undo encode_cyclic for inputs of every length,
    since complete 3-char groups undergo a triple left-rotation (identity)
    and incomplete trailing groups are left untouched by encode_cyclic."""
    encoded = encode_cyclic(s)
    assert decode_cyclic(encoded) == s


def test_decode_known_single_group():
    # "bca" is encode_cyclic("abc"). Decoding applies the left-rotation
    # twice more ("bca" -> "cab" -> "abc"), restoring the original group.
    assert decode_cyclic("bca") == "abc"


def test_decode_known_multiple_groups():
    # Each complete 3-char group is effectively right-rotated by one
    # position: "abc" -> "cab" and "def" -> "fde".
    # Verified step by step:
    #   encode_cyclic("abcdef")       == "bcaefd"
    #   encode_cyclic("bcaefd")       == "cabfde"
    assert decode_cyclic("abcdef") == "cabfde"


def test_decode_empty_string():
    # Exercises the degenerate case where encode_cyclic produces no groups.
    assert decode_cyclic("") == ""
