# file: script_11.py:4-16
# asked: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}

from script_11 import string_xor


def test_string_xor_executes_equal_and_unequal_branches():
    assert string_xor("010", "110") == "100"


def test_string_xor_all_equal_bits_returns_zeroes():
    assert string_xor("10101", "10101") == "00000"


def test_string_xor_all_different_bits_returns_ones():
    assert string_xor("1010", "0101") == "1111"
