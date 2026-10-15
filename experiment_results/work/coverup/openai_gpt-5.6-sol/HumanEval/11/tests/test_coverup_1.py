# file: script_11.py:4-16
# asked: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}

from script_11 import string_xor


def test_string_xor_executes_equal_and_different_bit_branches():
    assert string_xor("010", "110") == "100"


def test_string_xor_zips_only_to_shortest_input():
    assert string_xor("1011", "10") == "00"
