# file: script_45.py:1-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest
from script_45 import triangle_area


def test_triangle_area_positive_values():
    """Test triangle_area with positive values."""
    assert triangle_area(5, 3) == 7.5


def test_triangle_area_different_values():
    """Test triangle_area with different positive values."""
    assert triangle_area(10, 4) == 20.0


def test_triangle_area_unit_values():
    """Test triangle_area with unit values."""
    assert triangle_area(1, 1) == 0.5


def test_triangle_area_zero_base():
    """Test triangle_area with zero base."""
    assert triangle_area(0, 5) == 0.0


def test_triangle_area_zero_height():
    """Test triangle_area with zero height."""
    assert triangle_area(5, 0) == 0.0


def test_triangle_area_floats():
    """Test triangle_area with float values."""
    assert triangle_area(3.5, 2.0) == 3.5


def test_triangle_area_large_values():
    """Test triangle_area with large values."""
    assert triangle_area(100, 50) == 2500.0
