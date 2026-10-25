# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

from f011 import string_xor


def test_string_xor_equal_characters_returns_zero():
    assert string_xor("000", "000") == "000"
    assert string_xor("111", "111") == "000"
    assert string_xor("abc", "abc") == "000"


def test_string_xor_different_characters_returns_one():
    assert string_xor("010", "101") == "111"
    assert string_xor("000", "111") == "111"
    assert string_xor("a", "b") == "1"


def test_string_xor_mixed_characters():
    assert string_xor("0101", "0011") == "0110"
    assert string_xor("1100", "1010") == "0110"


def test_string_xor_empty_and_unequal_lengths():
    assert string_xor("", "") == ""
    assert string_xor("01", "010") == "00"
    assert string_xor("010", "01") == "00"
