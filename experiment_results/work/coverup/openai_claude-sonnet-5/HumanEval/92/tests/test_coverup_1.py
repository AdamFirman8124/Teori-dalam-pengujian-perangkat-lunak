# file: script_92.py:1-24
# asked: {"lines": [20, 21, 22, 23, 24], "branches": [[20, 21], [20, 24], [21, 22], [21, 23]]}
# gained: {"lines": [20, 21, 22, 23, 24], "branches": [[20, 21], [20, 24], [21, 22], [21, 23]]}

import pytest
from script_92 import any_int


def test_any_int_sum_matches_x_plus_y_equals_z():
    """Test when x + y equals z with all integers"""
    assert any_int(5, 2, 7) == True


def test_any_int_sum_matches_x_plus_z_equals_y():
    """Test when x + z equals y with all integers"""
    assert any_int(3, -2, 1) == True


def test_any_int_sum_matches_y_plus_z_equals_x():
    """Test when y + z equals x with all integers"""
    assert any_int(10, 3, 7) == True


def test_any_int_no_sum_matches():
    """Test when no combination sums correctly"""
    assert any_int(3, 2, 2) == False


def test_any_int_with_floats():
    """Test when inputs contain floats"""
    assert any_int(3.6, -2.2, 2) == False


def test_any_int_with_one_float():
    """Test when only one input is a float"""
    assert any_int(5.0, 2, 7) == False


def test_any_int_with_boolean():
    """Test when inputs contain boolean (edge case)"""
    # Note: In Python, bool is a subclass of int, so True/False are considered integers
    assert any_int(True, False, 1) == True


def test_any_int_negative_integers():
    """Test with negative integers that sum correctly"""
    assert any_int(-5, -2, -7) == True


def test_any_int_zero_sum():
    """Test with zero in the sum"""
    assert any_int(0, 5, 5) == True  # 5 + 5 = 10, not 0; but 0 + 5 = 5, so this is True
    assert any_int(5, -5, 0) == True  # 5 + (-5) = 0, so this is True


def test_any_int_no_valid_sum_with_zero():
    """Test with zero where no sum matches"""
    assert any_int(0, 3, 5) == False  # 0+3=3 (not 5), 0+5=5 (not 3), 3+5=8 (not 0)


def test_any_int_all_zeros():
    """Test with all zeros"""
    assert any_int(0, 0, 0) == True
