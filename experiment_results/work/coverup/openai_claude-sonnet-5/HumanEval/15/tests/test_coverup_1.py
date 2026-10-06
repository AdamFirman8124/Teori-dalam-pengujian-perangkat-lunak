# file: script_15.py:1-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest
from script_15 import string_sequence


def test_string_sequence_zero():
    """Test string_sequence with n=0"""
    assert string_sequence(0) == '0'


def test_string_sequence_positive():
    """Test string_sequence with positive n"""
    assert string_sequence(5) == '0 1 2 3 4 5'


def test_string_sequence_one():
    """Test string_sequence with n=1"""
    assert string_sequence(1) == '0 1'


def test_string_sequence_large():
    """Test string_sequence with larger n"""
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
