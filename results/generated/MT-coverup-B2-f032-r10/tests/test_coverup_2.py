# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import math

from f032 import poly


def test_poly_evaluates_polynomial():
    # 3 + 2x + x^2 at x = 2 -> 3 + 4 + 4 = 11
    result = poly([3, 2, 1], 2.0)
    assert result == 11.0
    assert isinstance(result, float)


def test_poly_empty_coefficients():
    assert poly([], 5.0) == 0


def test_poly_constant():
    assert poly([7], 100.0) == 7


def test_poly_uses_math_pow_for_fractional_exponent_base():
    # x = 0.5: 1 + 1*0.5 + 1*0.25 = 1.75
    result = poly([1, 1, 1], 0.5)
    assert math.isclose(result, 1.75)
