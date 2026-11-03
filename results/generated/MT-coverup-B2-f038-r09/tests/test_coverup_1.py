# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

import pytest

from f038 import encode_cyclic


def test_encode_cyclic_empty_string():
    """Covers line 4 (empty group list), line 6 (no groups), line 7 (join of nothing)."""
    assert encode_cyclic("") == ""


def test_encode_cyclic_short_group_left_unchanged():
    """Covers the False branch of line 6 (group with fewer than 3 elements)."""
    assert encode_cyclic("a") == "a"
    assert encode_cyclic("ab") == "ab"


def test_encode_cyclic_full_group_cycled():
    """Covers the True branch of line 6 (group of exactly 3 elements is cycled)."""
    assert encode_cyclic("abc") == "bca"


def test_encode_cyclic_mixed_group_sizes():
    """Covers both branches of line 6 within a single call, plus line 7 join."""
    assert encode_cyclic("abcd") == "bcad"      # ["abc", "d"] -> ["bca", "d"]
    assert encode_cyclic("abcde") == "bcade"    # ["abc", "de"] -> ["bca", "de"]
    assert encode_cyclic("abcdef") == "bcaefd"  # ["abc", "def"] -> ["bca", "efd"]


def test_encode_cyclic_has_order_three():
    """Each 3-element group is rotated by one position per call, so applying
    encode_cyclic three times must restore the original string for every
    group size (groups shorter than 3 are left unchanged)."""
    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "hello world"]:
        assert encode_cyclic(encode_cyclic(encode_cyclic(s))) == s
