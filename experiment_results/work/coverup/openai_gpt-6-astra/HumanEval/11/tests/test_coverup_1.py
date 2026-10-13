# file: script_11.py:4-16
# asked: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}

from script_11 import string_xor


def test_string_xor_returns_zero_for_matching_bits():
    assert string_xor("0", "0") == "0"
    assert string_xor("1", "1") == "0"


def test_string_xor_returns_one_for_different_bits():
    assert string_xor("0", "1") == "1"
    assert string_xor("1", "0") == "1"


def test_string_xor_processes_each_pair_of_bits():
    assert string_xor("010", "110") == "100"
