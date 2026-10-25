# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

from f011 import string_xor


def test_string_xor_returns_zero_for_matching_bits():
    assert string_xor("10101", "10101") == "00000"


def test_string_xor_returns_one_for_different_bits():
    assert string_xor("10101", "01010") == "11111"
