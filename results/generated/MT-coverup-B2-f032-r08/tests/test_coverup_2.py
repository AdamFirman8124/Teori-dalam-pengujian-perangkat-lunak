# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f032 import poly


def test_poly_evaluates_all_coefficients():
    assert poly([1, 2, 3], 2.0) == 17.0


def test_poly_with_no_coefficients():
    assert poly([], 2.0) == 0
