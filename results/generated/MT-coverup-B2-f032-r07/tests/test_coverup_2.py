# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import math

import pytest

from f032 import poly


def test_poly_evaluates_polynomial():
    # 2*x^2 + 3*x + 1 at x = 2 -> 8 + 6 + 1 = 15
    assert poly([1, 3, 2], 2.0) == pytest.approx(15.0)


def test_poly_empty_coefficients():
    # sum of empty list is 0 (int), line 6 executes with empty iterable
    assert poly([], 5.0) == 0


def test_poly_zero_x():
    # x = 0: only constant term survives (0**0 == 1.0 via math.pow)
    assert poly([7, 1, 1], 0.0) == pytest.approx(7.0)


def test_poly_negative_x():
    # x^2 - x at x = -2 -> 4 + 2 = 6
    assert poly([0, -1, 1], -2.0) == pytest.approx(6.0)


def test_poly_does_not_mutate_input():
    xs = [1, 2, 3]
    poly(xs, 1.5)
    assert xs == [1, 2, 3]
