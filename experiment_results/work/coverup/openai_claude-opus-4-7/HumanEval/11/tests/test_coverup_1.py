# file: script_11.py:4-16
# asked: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}

import pytest

from script_11 import string_xor


def test_string_xor_equal_bits():
    # Exercises the `if i == j` branch (lines 11-12)
    assert string_xor("010", "010") == "000"
    assert string_xor("111", "111") == "000"
    assert string_xor("000", "000") == "000"


def test_string_xor_different_bits():
    # Exercises the `else` branch (lines 13-14)
    assert string_xor("010", "110") == "100"
    assert string_xor("000", "111") == "111"
    assert string_xor("101", "010") == "111"


def test_string_xor_mixed_bits():
    # Exercises both branches within a single call (line 16 join)
    assert string_xor("0110", "1100") == "1010"
    assert string_xor("1010", "0101") == "1111"
    assert string_xor("1100", "1100") == "0000"


def test_string_xor_empty():
    # zip over empty inputs -> empty result
    assert string_xor("", "") == ""


def test_string_xor_unequal_lengths():
    # zip truncates to the shorter string
    assert string_xor("0101", "11") == "10"
    assert string_xor("1", "0101") == "1"


def test_string_xor_postconditions():
    a, b = "10110", "01101"
    result = string_xor(a, b)
    # Result length matches the shorter input
    assert len(result) == min(len(a), len(b))
    # Result contains only '0' and '1'
    assert set(result) <= {"0", "1"}
    # XOR is symmetric
    assert string_xor(a, b) == string_xor(b, a)
    # XOR with self is all zeros
    assert string_xor(a, a) == "0" * len(a)
