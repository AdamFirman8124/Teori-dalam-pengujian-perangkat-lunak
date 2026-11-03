# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import math

import pytest

from f032 import poly


def test_poly_evaluates_polynomial_with_terms():
    """Covers line 6 (the return statement) including the comprehension loop
    body executing at least once (loop-taken branch)."""
    # 1*2^0 + 2*2^1 + 3*2^2 = 1 + 4 + 12 = 17
    result = poly([1, 2, 3], 2.0)
    assert result == pytest.approx(17.0)

    # 3*x^0 - 2*x^1 + 1*x^2 with x = 4.0 -> 3 - 8 + 16 = 11
    result = poly([3, -2, 1], 4.0)
    expected = 3 * math.pow(4.0, 0) + (-2) * math.pow(4.0, 1) + 1 * math.pow(4.0, 2)
    assert result == pytest.approx(expected)


def test_poly_empty_coefficient_list():
    """Covers the comprehension loop's immediate-exit branch (empty xs),
    while still executing line 6."""
    result = poly([], 5.0)
    assert result == 0


def test_poly_single_coefficient():
    """Covers the loop running exactly one iteration (both loop arcs:
    enter body and exhaust loop)."""
    result = poly([7], 10.0)
    assert result == pytest.approx(7.0)
