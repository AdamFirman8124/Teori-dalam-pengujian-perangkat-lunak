# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

import pytest

from f038 import encode_cyclic, decode_cyclic


def test_encode_cyclic_single_full_group():
    """A group of exactly 3 chars is cycled: first char moves to the end."""
    assert encode_cyclic("abc") == "bca"


def test_encode_cyclic_multiple_full_groups():
    """Every full group of 3 is cycled independently."""
    assert encode_cyclic("abcdef") == "bcaefd"
    assert encode_cyclic("abcdefghi") == "bcaefdhig"


def test_encode_cyclic_partial_group_unchanged():
    """Groups with fewer than 3 chars are left unchanged (else-branch of line 6)."""
    assert encode_cyclic("a") == "a"
    assert encode_cyclic("ab") == "ab"
    assert encode_cyclic("abcde") == "bcade"  # "abc" -> "bca", "de" unchanged


def test_encode_cyclic_mixed_group_sizes():
    """Mixed full and partial groups: full ones cycle, partial ones don't."""
    assert encode_cyclic("abcdefgh") == "bcaefdgh"  # "abc"->"bca", "def"->"efd", "gh" unchanged


def test_encode_cyclic_empty_string():
    """Empty string yields empty string (loop body never runs, join of nothing)."""
    assert encode_cyclic("") == ""


def test_encode_cyclic_roundtrip_with_decode():
    """decode_cyclic(encode_cyclic(s)) must restore the original string."""
    for s in ["", "a", "ab", "abc", "abcd", "hello world", "xyzzy!"]:
        assert decode_cyclic(encode_cyclic(s)) == s
