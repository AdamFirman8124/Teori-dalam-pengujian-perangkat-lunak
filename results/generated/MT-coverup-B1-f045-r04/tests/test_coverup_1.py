# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_basic():
    assert triangle_area(3, 4) == 6.0


def test_triangle_area_floats():
    assert triangle_area(2.5, 1.2) == pytest.approx(1.5)


def test_triangle_area_zero():
    assert triangle_area(0, 5) == 0.0
