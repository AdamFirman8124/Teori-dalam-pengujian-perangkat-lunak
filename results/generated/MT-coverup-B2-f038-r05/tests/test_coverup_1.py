# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

import pytest

from f038 import encode_cyclic


def test_encode_cyclic_full_groups():
    # Groups of exactly 3 get cycled: "abc" -> "bca", "def" -> "efd"
    assert encode_cyclic("abcdef") == "bcaefd"


def test_encode_cyclic_partial_last_group():
    # Last group shorter than 3 stays unchanged: "abc" -> "bca", "de" -> "de"
    assert encode_cyclic("abcde") == "bcade"


def test_encode_cyclic_single_partial_group():
    # Only one group, shorter than 3, unchanged
    assert encode_cyclic("ab") == "ab"


def test_encode_cyclic_empty_string():
    # Empty string produces no groups and returns empty string
    assert encode_cyclic("") == ""


def test_encode_cyclic_exact_multiple_of_three():
    # Length exactly divisible by 3: all groups cycled
    assert encode_cyclic("xyz") == "yzx"


def test_encode_cyclic_single_char():
    assert encode_cyclic("a") == "a"


def test_encode_cyclic_roundtrip_with_decode():
    # Decoding (inverse cycling) recovers the original string
    def decode_cyclic(s: str) -> str:
        groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
        groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
        return "".join(groups)

    for s in ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "hello world"]:
        assert decode_cyclic(encode_cyclic(s)) == s
