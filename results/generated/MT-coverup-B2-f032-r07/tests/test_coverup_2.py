# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f032 import poly


def test_poly_basic():
    """poly([1, 2, 3], 2) == 1 + 2*2 + 3*4 == 17 (executes line 6)."""
    assert poly([1, 2, 3], 2.0) == pytest.approx(17.0)


def test_poly_empty_coefficients():
    """An empty coefficient list yields the empty sum, 0."""
    assert poly([], 5.0) == 0


def test_poly_constant():
    """A single coefficient is a constant polynomial, independent of x."""
    assert poly([7], 100.0) == pytest.approx(7.0)


def test_poly_negative_and_zero_coefficients():
    """Negative and zero coefficients are handled correctly."""
    # -1 + 0*x + 2*x^2 at x = 3 -> -1 + 0 + 18 = 17
    assert poly([-1, 0, 2], 3.0) == pytest.approx(17.0)


def test_poly_at_zero():
    """Any polynomial evaluated at x = 0 equals its constant term."""
    assert poly([4, 5, 6], 0.0) == pytest.approx(4.0)
