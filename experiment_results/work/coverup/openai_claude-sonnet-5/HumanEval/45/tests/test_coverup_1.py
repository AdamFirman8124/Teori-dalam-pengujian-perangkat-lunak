# file: script_45.py:1-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest
from script_45 import triangle_area


def test_triangle_area_positive():
    """Test triangle area calculation with positive values."""
    assert triangle_area(5, 3) == 7.5


def test_triangle_area_unit_values():
    """Test triangle area calculation with unit values."""
    assert triangle_area(1, 1) == 0.5


def test_triangle_area_zero_base():
    """Test triangle area calculation with zero base."""
    assert triangle_area(0, 5) == 0.0


def test_triangle_area_zero_height():
    """Test triangle area calculation with zero height."""
    assert triangle_area(5, 0) == 0.0


def test_triangle_area_large_values():
    """Test triangle area calculation with large values."""
    assert triangle_area(100, 50) == 2500.0


def test_triangle_area_fractional_values():
    """Test triangle area calculation with fractional values."""
    assert triangle_area(2.5, 4.0) == 5.0
