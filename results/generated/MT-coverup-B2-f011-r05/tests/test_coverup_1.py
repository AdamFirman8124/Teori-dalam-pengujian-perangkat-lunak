# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

import pytest

from f011 import string_xor


def test_string_xor_equal_chars_produce_zero():
    # Exercises the `if i == j:` branch of the nested xor() function.
    assert string_xor("000", "000") == "000"


def test_string_xor_different_chars_produce_one():
    # Exercises the `else:` branch of the nested xor() function.
    assert string_xor("0", "1") == "1"
    assert string_xor("1", "0") == "1"


def test_string_xor_mixed():
    # Exercises the generator expression, zip() pairing, and ''.join() on line 12,
    # hitting both branches of xor() in a single call.
    assert string_xor("0100", "1100") == "1000"
    assert string_xor("1111", "0000") == "1111"
    assert string_xor("10", "01") == "11"


def test_string_xor_empty_strings():
    # zip() of two empty strings yields nothing, so ''.join() returns ''.
    assert string_xor("", "") == ""


def test_string_xor_unequal_lengths():
    # zip() stops at the shorter string; only paired positions are processed.
    assert string_xor("1010", "11") == "01"
    assert string_xor("1", "0000") == "1"
