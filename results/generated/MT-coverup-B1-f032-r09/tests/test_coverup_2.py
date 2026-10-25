# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f032 import poly


def test_poly_evaluates_all_coefficients():
    coefficients = [1, 2, 3]
    original = coefficients.copy()

    assert poly(coefficients, 2.0) == 17.0
    assert coefficients == original


def test_poly_with_no_coefficients_returns_zero():
    assert poly([], 2.0) == 0
