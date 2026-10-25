# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

import pytest

from f011 import string_xor


def test_string_xor_equal_chars_return_zero():
    # Covers lines 7-8: i == j branch returning '0'
    assert string_xor("0000", "0000") == "0000"
    assert string_xor("11", "11") == "00"


def test_string_xor_different_chars_return_one():
    # Covers lines 9-10: else branch returning '1'
    assert string_xor("0101", "1010") == "1111"
    assert string_xor("1", "0") == "1"


def test_string_xor_mixed():
    # Covers both branches in a single call
    assert string_xor("1100", "1010") == "0110"


def test_string_xor_empty_inputs():
    # Covers line 12 with an empty zip (no iterations)
    assert string_xor("", "") == ""


def test_string_xor_truncates_to_shorter_input():
    # zip stops at the shorter string:
    # '1' vs '1' -> '0', '0' vs '1' -> '1'
    assert string_xor("1010", "11") == "01"


def test_string_xor_result_type():
    result = string_xor("01", "10")
    assert isinstance(result, str)
    assert set(result) <= {"0", "1"}
