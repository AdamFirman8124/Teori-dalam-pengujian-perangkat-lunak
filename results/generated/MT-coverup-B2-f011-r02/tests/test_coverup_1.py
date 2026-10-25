# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

from f011 import string_xor


def test_string_xor_equal_bits_return_zero():
    assert string_xor("0", "0") == "0"
    assert string_xor("1", "1") == "0"
    assert string_xor("0000", "0000") == "0000"
    assert string_xor("1111", "1111") == "0000"


def test_string_xor_different_bits_return_one():
    assert string_xor("0", "1") == "1"
    assert string_xor("1", "0") == "1"
    assert string_xor("0000", "1111") == "1111"
    assert string_xor("1111", "0000") == "1111"


def test_string_xor_mixed():
    assert string_xor("010", "110") == "100"
    assert string_xor("0101", "1010") == "1111"
    assert string_xor("1100", "1010") == "0110"


def test_string_xor_empty():
    assert string_xor("", "") == ""
    assert string_xor("", "101") == ""
    assert string_xor("101", "") == ""


def test_string_xor_truncates_to_shortest():
    assert string_xor("1", "10") == "0"
    assert string_xor("10", "1") == "0"
    assert string_xor("0101", "11") == "10"
