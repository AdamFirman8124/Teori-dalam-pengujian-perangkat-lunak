# file: script_11.py:4-16
# asked: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}

from script_11 import string_xor


def test_string_xor_equal_bits_return_zero():
    assert string_xor("000", "000") == "000"


def test_string_xor_unequal_bits_return_one():
    assert string_xor("010", "110") == "100"
