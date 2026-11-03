# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import math

from f032 import poly


def test_poly_evaluates_polynomial():
    # poly([c0, c1, c2, ...], x) == c0*x^0 + c1*x^1 + c2*x^2 + ...
    # For xs = [1, 3, 2] and x = 2: 1*1 + 3*2 + 2*4 = 15
    assert poly([1, 3, 2], 2) == 15


def test_poly_with_negative_x():
    # For xs = [1, 2] and x = -3: 1 + 2*(-3) = -5
    assert poly([1, 2], -3) == -5


def test_poly_at_zero():
    # At x = 0, every term with i > 0 vanishes; result is c0.
    assert poly([7, 5, 9], 0) == 7


def test_poly_empty_coefficients():
    # Sum of an empty list is 0.
    assert poly([], 4.2) == 0


def test_poly_matches_math_pow_semantics():
    xs = [0.5, -1.5, 2.0]
    x = 1.5
    expected = sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
    assert poly(xs, x) == expected
