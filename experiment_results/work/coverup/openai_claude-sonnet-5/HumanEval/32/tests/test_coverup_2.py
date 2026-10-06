# file: script_32.py:12-34
# asked: {"lines": [24, 25, 26, 27, 28, 29, 30, 31, 33, 34], "branches": [[25, 26], [25, 28], [28, 29], [28, 34], [30, 31], [30, 33]]}
# gained: {"lines": [24, 25, 26, 27, 28, 29, 30, 31, 33, 34], "branches": [[25, 26], [25, 28], [28, 29], [28, 34], [30, 31], [30, 33]]}

# -*- coding: utf-8 -*-
import pytest
from script_32 import find_zero, poly


def test_find_zero_simple_linear():
    """Test with simple linear polynomial f(x) = 1 + 2x, zero at x = -0.5"""
    result = find_zero([1, 2])
    assert abs(result - (-0.5)) < 1e-9
    assert abs(poly([1, 2], result)) < 1e-9


def test_find_zero_cubic():
    """Test with cubic polynomial (x-1)(x-2)(x-3) = -6 + 11x - 6x^2 + x^3"""
    result = find_zero([-6, 11, -6, 1])
    assert abs(result - 1.0) < 1e-9
    assert abs(poly([-6, 11, -6, 1], result)) < 1e-9


def test_find_zero_quadratic_positive_root():
    """Test with quadratic x^2 - 4 = 0, has roots at x = +/-2"""
    result = find_zero([-4, 0, 1])
    assert abs(poly([-4, 0, 1], result)) < 1e-9
    assert -2.1 < result < 2.1


def test_find_zero_requires_expansion():
    """Test case where initial [-1, 1] interval doesn't bracket the root"""
    # f(x) = -10 + x, zero at x = 10
    # poly(-1) = -11, poly(1) = -9, both negative, so need to expand
    result = find_zero([-10, 1])
    assert abs(result - 10.0) < 1e-9
    assert abs(poly([-10, 1], result)) < 1e-9


def test_find_zero_large_constant():
    """Test with f(x) = 100 - x, zero at x = 100, requires expansion"""
    result = find_zero([100, -1])
    assert abs(result - 100.0) < 1e-9
    assert abs(poly([100, -1], result)) < 1e-9


def test_find_zero_bisection_branch_else():
    """Test that exercises the else branch in bisection (line 33)"""
    # f(x) = -1 + 2x, zero at x = 0.5
    # This will test the else branch when poly(center) * poly(begin) <= 0
    result = find_zero([-1, 2])
    assert abs(result - 0.5) < 1e-9
    assert abs(poly([-1, 2], result)) < 1e-9


def test_find_zero_quartic():
    """Test with quartic polynomial"""
    # f(x) = -16 + x^4, zeros at x = +/-2
    result = find_zero([-16, 0, 0, 0, 1])
    assert abs(poly([-16, 0, 0, 0, 1], result)) < 1e-9


def test_find_zero_negative_expansion():
    """Test where root is far in negative direction"""
    # f(x) = 20 + 2x, zero at x = -10
    result = find_zero([20, 2])
    assert abs(result - (-10.0)) < 1e-9
    assert abs(poly([20, 2], result)) < 1e-9
