# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

from f011 import string_xor


def test_string_xor_returns_zero_for_matching_characters():
    assert string_xor("1010", "1010") == "0000"


def test_string_xor_returns_one_for_different_characters():
    assert string_xor("1010", "0101") == "1111"
