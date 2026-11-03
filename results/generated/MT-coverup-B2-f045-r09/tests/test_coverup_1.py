# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_basic():
    assert triangle_area(4, 3) == 6.0


def test_triangle_area_floats():
    assert triangle_area(2.5, 4.0) == 5.0


def test_triangle_area_zero_base():
    assert triangle_area(0, 5) == 0.0


def test_triangle_area_negative_height():
    assert triangle_area(6, -2) == -6.0
