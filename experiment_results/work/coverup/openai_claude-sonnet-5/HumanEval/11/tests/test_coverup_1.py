# file: script_11.py:4-16
# asked: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}

import pytest
from script_11 import string_xor


def test_string_xor_basic():
    """Test basic XOR operation."""
    assert string_xor('010', '110') == '100'


def test_string_xor_all_zeros():
    """Test XOR with all zeros."""
    assert string_xor('000', '000') == '000'


def test_string_xor_all_ones():
    """Test XOR with all ones."""
    assert string_xor('111', '111') == '000'


def test_string_xor_different_bits():
    """Test XOR with different bits."""
    assert string_xor('101', '010') == '111'


def test_string_xor_single_bit():
    """Test XOR with single bit."""
    assert string_xor('0', '1') == '1'
    assert string_xor('1', '0') == '1'
    assert string_xor('0', '0') == '0'
    assert string_xor('1', '1') == '0'


def test_string_xor_empty():
    """Test XOR with empty strings."""
    assert string_xor('', '') == ''


def test_string_xor_longer_strings():
    """Test XOR with longer strings."""
    assert string_xor('10101010', '01010101') == '11111111'
    assert string_xor('11110000', '10101010') == '01011010'
