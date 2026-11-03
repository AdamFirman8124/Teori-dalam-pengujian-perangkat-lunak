# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f032 import poly


def test_poly_basic():
    """Evaluate 1 + 2x + 3x^2 at x=2 -> 1 + 4 + 12 = 17."""
    result = poly([1, 2, 3], 2.0)
    assert result == pytest.approx(17.0)


def test_poly_single_coefficient():
    """A single coefficient yields coeff * x^0 = coeff."""
    assert poly([7], 100.0) == pytest.approx(7.0)


def test_poly_zero_x():
    """At x=0 only the constant term survives."""
    assert poly([3, 4, 5], 0.0) == pytest.approx(3.0)


def test_poly_negative_x():
    """Negative base exercises even and odd powers."""
    # 1 + 0*x + 1*x^2 at x=-2 -> 1 + 0 + 4 = 5
    assert poly([1, 0, 1], -2.0) == pytest.approx(5.0)


def test_poly_empty_coefficients():
    """Empty coefficient list sums to 0."""
    assert poly([], 5.0) == 0


def test_poly_fractional_x():
    """Fractional base: 2 + 1*0.5 = 2.5."""
    assert poly([2, 1], 0.5) == pytest.approx(2.5)


def test_poly_matches_manual_computation():
    """Result matches an independently computed polynomial evaluation."""
    coeffs = [1.5, -2.0, 0.25, 3.0]
    x = 1.5
    expected = sum(c * (x ** i) for i, c in enumerate(coeffs))
    assert poly(coeffs, x) == pytest.approx(expected)
