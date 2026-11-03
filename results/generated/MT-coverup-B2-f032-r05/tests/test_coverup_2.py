# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import math

import pytest

from f032 import poly


def test_poly_basic():
    """poly([1, 2, 3], 2) == 1*2^0 + 2*2^1 + 3*2^2 == 17."""
    result = poly([1, 2, 3], 2.0)
    assert math.isclose(result, 17.0)


def test_poly_empty_list():
    """An empty coefficient list yields 0 (sum of empty list)."""
    assert poly([], 5.0) == 0


def test_poly_single_coefficient():
    """A single coefficient c evaluates to c * x^0 == c."""
    assert math.isclose(poly([7.5], 100.0), 7.5)


def test_poly_negative_and_fractional():
    """Handles negative x and fractional coefficients correctly."""
    xs = [1.5, -2.0, 0.5]
    x = -2.0
    expected = 1.5 * math.pow(-2.0, 0) + (-2.0) * math.pow(-2.0, 1) + 0.5 * math.pow(-2.0, 2)
    assert math.isclose(poly(xs, x), expected)


def test_poly_zero_x():
    """With x == 0, only the constant term survives."""
    assert math.isclose(poly([3.0, 4.0, 5.0], 0.0), 3.0)
