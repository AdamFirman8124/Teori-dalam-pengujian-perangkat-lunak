# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

import pytest

from f011 import string_xor


def test_string_xor_equal_chars_return_zero():
    # Covers line 7-8: i == j branch returning '0'
    assert string_xor("0", "0") == "0"
    assert string_xor("1", "1") == "0"


def test_string_xor_different_chars_return_one():
    # Covers line 9-10: else branch returning '1'
    assert string_xor("0", "1") == "1"
    assert string_xor("1", "0") == "1"


def test_string_xor_mixed_string():
    # Covers line 12: generator join over zip, exercising both branches
    assert string_xor("0101", "0011") == "0110"
    assert string_xor("1111", "1111") == "0000"
    assert string_xor("0000", "1111") == "1111"


def test_string_xor_shorter_input_truncates():
    # zip stops at the shorter string; verifies postcondition for unequal lengths
    assert string_xor("1010", "11") == "01"
