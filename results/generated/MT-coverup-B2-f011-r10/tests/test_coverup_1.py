# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

from f011 import string_xor


def test_string_xor_equal_chars_returns_zero():
    assert string_xor("0101", "0101") == "0000"
    assert string_xor("aaaa", "aaaa") == "0000"


def test_string_xor_different_chars_returns_one():
    assert string_xor("0101", "1010") == "1111"
    assert string_xor("aaaa", "bbbb") == "1111"


def test_string_xor_mixed_chars():
    assert string_xor("0110", "1010") == "1100"
    assert string_xor("abc", "abd") == "001"


def test_string_xor_empty_strings():
    assert string_xor("", "") == ""


def test_string_xor_different_lengths_truncates_to_shorter():
    assert string_xor("111", "1") == "0"
    assert string_xor("1", "111") == "0"
    assert string_xor("10", "1111") == "01"
