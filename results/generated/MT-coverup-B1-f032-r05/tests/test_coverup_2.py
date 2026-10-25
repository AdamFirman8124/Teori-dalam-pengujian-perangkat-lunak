# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import math

import pytest

from f032 import poly


def test_poly_evaluates_polynomial():
    # 3*x^2 + 2*x + 1 at x = 2 -> 12 + 4 + 1 = 17
    assert poly([1, 2, 3], 2.0) == pytest.approx(17.0)


def test_poly_empty_coefficients():
    # sum of an empty list is 0 (int), covering the loop-not-taken branch
    assert poly([], 5.0) == 0


def test_poly_zero_x():
    # x = 0: only the constant term survives (0**0 == 1 in math.pow)
    assert poly([7, 3, 4], 0.0) == pytest.approx(7.0)


def test_poly_negative_x():
    # x^2 - x at x = -2 -> 4 + 2 = 6
    assert poly([0, -1, 1], -2.0) == pytest.approx(6.0)
