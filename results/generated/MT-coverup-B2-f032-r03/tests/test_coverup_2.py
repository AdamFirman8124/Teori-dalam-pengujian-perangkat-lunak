# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f032 import poly


def test_poly_basic_evaluation():
    # 1 + 2*x + 3*x**2 at x=2 => 1 + 4 + 12 = 17
    assert poly([1, 2, 3], 2.0) == 17.0


def test_poly_empty_list_returns_zero():
    assert poly([], 5.0) == 0


def test_poly_single_and_zero_coeffs():
    assert poly([7], 100.0) == 7.0
    assert poly([0, 0, 0], 3.0) == 0.0
    assert poly([1, 0, 2], 3.0) == 1.0 + 0.0 + 18.0
