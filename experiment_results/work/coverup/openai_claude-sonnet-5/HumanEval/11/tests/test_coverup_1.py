# file: script_11.py:4-16
# asked: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}

import pytest
from script_11 import string_xor


def test_string_xor_basic():
    """Test basic XOR operation from docstring."""
    assert string_xor('010', '110') == '100'


def test_string_xor_all_zeros():
    """Test XOR with all zeros - executes line 11-12 (equal case)."""
    assert string_xor('000', '000') == '000'


def test_string_xor_all_ones():
    """Test XOR with all ones - executes line 11-12 (equal case)."""
    assert string_xor('111', '111') == '000'


def test_string_xor_different_bits():
    """Test XOR with different bits - executes line 14 (different case)."""
    assert string_xor('0', '1') == '1'
    assert string_xor('1', '0') == '1'


def test_string_xor_mixed():
    """Test XOR with mixed equal and different bits - executes all branches."""
    assert string_xor('0011', '0101') == '0110'


def test_string_xor_empty():
    """Test XOR with empty strings."""
    assert string_xor('', '') == ''


def test_string_xor_single_bit_same():
    """Test single bit XOR when bits are same - executes line 11-12."""
    assert string_xor('0', '0') == '0'
    assert string_xor('1', '1') == '0'


def test_string_xor_single_bit_different():
    """Test single bit XOR when bits are different - executes line 14."""
    assert string_xor('0', '1') == '1'
    assert string_xor('1', '0') == '1'


def test_string_xor_longer_strings():
    """Test XOR with longer strings to ensure join and zip work correctly."""
    assert string_xor('10101010', '01010101') == '11111111'
    assert string_xor('11110000', '11110000') == '00000000'
