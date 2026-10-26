# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

from f011 import string_xor


def test_string_xor_equal_bits_return_zero():
    assert string_xor("0", "0") == "0"
    assert string_xor("1", "1") == "0"
    assert string_xor("0101", "0101") == "0000"


def test_string_xor_different_bits_return_one():
    assert string_xor("0", "1") == "1"
    assert string_xor("1", "0") == "1"
    assert string_xor("0000", "1111") == "1111"


def test_string_xor_mixed_and_edge_cases():
    assert string_xor("010", "101") == "111"
    assert string_xor("0110", "0011") == "0101"
    assert string_xor("", "") == ""
    assert string_xor("01", "") == ""
