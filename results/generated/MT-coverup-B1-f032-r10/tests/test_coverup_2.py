# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f032 import poly


def test_poly_evaluates_coefficients():
    assert poly([1, 2, 3], 2) == 17


def test_poly_with_empty_coefficients():
    assert poly([], 5) == 0
