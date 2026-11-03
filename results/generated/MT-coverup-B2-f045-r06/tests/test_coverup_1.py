# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_basic():
    """Line 3 (the return statement) executes; result is half of a*h."""
    result = triangle_area(3, 4)
    assert result == 6.0
    assert isinstance(result, float)


def test_triangle_area_float_inputs():
    result = triangle_area(2.5, 4.0)
    assert result == 5.0
    assert isinstance(result, float)


def test_triangle_area_zero_base():
    result = triangle_area(0, 5)
    assert result == 0.0


def test_triangle_area_fractional_result():
    # a * h odd ensures the division actually produces a fractional value
    result = triangle_area(3, 5)
    assert result == 7.5
    assert isinstance(result, float)


def test_triangle_area_symmetry():
    assert triangle_area(4, 6) == triangle_area(6, 4)
