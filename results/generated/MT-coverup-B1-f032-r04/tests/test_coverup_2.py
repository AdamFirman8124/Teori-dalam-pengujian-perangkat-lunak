# file: project/f032/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f032 import poly


def test_poly_evaluates_polynomial():
    assert poly([2, 3, 4], 2.0) == pytest.approx(24.0)


def test_poly_with_no_coefficients_returns_zero():
    assert poly([], 5.0) == 0
