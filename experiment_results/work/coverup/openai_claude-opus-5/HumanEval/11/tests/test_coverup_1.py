# file: script_11.py:4-16
# asked: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}
# gained: {"lines": [10, 11, 12, 14, 16], "branches": [[11, 12], [11, 14]]}

import pytest
from script_11 import string_xor


def test_string_xor_basic():
    """Test basic XOR operation from docstring"""
    assert string_xor('010', '110') == '100'


def test_string_xor_all_same():
    """Test when both strings are identical - exercises line 11-12"""
    assert string_xor('111', '111') == '000'
    assert string_xor('000', '000') == '000'
    assert string_xor('101', '101') == '000'


def test_string_xor_all_different():
    """Test when all bits are different - exercises line 14"""
    assert string_xor('000', '111') == '111'
    assert string_xor('111', '000') == '111'
    assert string_xor('101', '010') == '111'


def test_string_xor_mixed():
    """Test mixed cases - exercises both branches"""
    assert string_xor('1010', '1100') == '0110'
    assert string_xor('0011', '0101') == '0110'


def test_string_xor_single_bit():
    """Test single bit operations"""
    assert string_xor('0', '0') == '0'
    assert string_xor('1', '1') == '0'
    assert string_xor('0', '1') == '1'
    assert string_xor('1', '0') == '1'


def test_string_xor_empty():
    """Test empty strings"""
    assert string_xor('', '') == ''
