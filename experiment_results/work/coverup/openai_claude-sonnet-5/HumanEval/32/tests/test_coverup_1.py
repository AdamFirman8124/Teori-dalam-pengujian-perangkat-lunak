# file: script_32.py:4-9
# asked: {"lines": [9], "branches": []}
# gained: {"lines": [9], "branches": []}

import pytest
import math
from script_32 import poly


def test_poly_empty_list():
    """Test poly with empty coefficient list"""
    result = poly([], 2.0)
    assert result == 0


def test_poly_single_coefficient():
    """Test poly with single coefficient (constant)"""
    result = poly([5], 3.0)
    assert result == 5


def test_poly_multiple_coefficients():
    """Test poly with multiple coefficients"""
    result = poly([1, 2, 3], 2.0)
    assert result == 1 + 2 * 2 + 3 * 4
    assert result == 17


def test_poly_at_zero():
    """Test poly evaluated at x=0"""
    result = poly([5, 10, 15], 0.0)
    assert result == 5


def test_poly_negative_x():
    """Test poly with negative x value"""
    result = poly([1, 1, 1], -1.0)
    assert result == 1 + 1 * (-1) + 1 * 1
    assert result == 1


def test_poly_negative_coefficients():
    """Test poly with negative coefficients"""
    result = poly([-1, -2, -3], 2.0)
    assert result == -1 + (-2) * 2 + (-3) * 4
    assert result == -17


def test_poly_fractional_x():
    """Test poly with fractional x value"""
    result = poly([1, 2, 4], 0.5)
    assert result == 1 + 2 * 0.5 + 4 * 0.25
    assert result == 3.0


def test_poly_large_polynomial():
    """Test poly with larger degree polynomial"""
    result = poly([1, 0, 0, 0, 1], 1.0)
    assert result == 2


def test_poly_zero_coefficients():
    """Test poly with zero coefficients"""
    result = poly([0, 0, 0], 5.0)
    assert result == 0
