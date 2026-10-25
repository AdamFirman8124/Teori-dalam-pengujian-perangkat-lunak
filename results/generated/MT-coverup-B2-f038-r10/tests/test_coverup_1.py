# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

import pytest

from f038 import encode_cyclic


def test_encode_cyclic_full_groups():
    # "abcdef" -> groups ["abc", "def"] -> ["bca", "efd"] -> "bcaefd"
    assert encode_cyclic("abcdef") == "bcaefd"


def test_encode_cyclic_partial_group():
    # "abcde" -> groups ["abc", "de"] -> ["bca", "de"] -> "bcade"
    assert encode_cyclic("abcde") == "bcade"
    # single char group stays unchanged
    assert encode_cyclic("a") == "a"
    # two char group stays unchanged
    assert encode_cyclic("ab") == "ab"


def test_encode_cyclic_empty_string():
    assert encode_cyclic("") == ""


def test_encode_cyclic_roundtrip():
    # decode via two more encodes (cyclic shift of 3 positions)
    s = "abcdefgh"
    assert encode_cyclic(encode_cyclic(encode_cyclic(s))) == s
