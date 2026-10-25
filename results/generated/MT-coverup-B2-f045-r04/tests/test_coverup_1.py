# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_executes_return_line():
    result = triangle_area(3, 4)
    assert result == 6.0
    assert isinstance(result, float)


def test_triangle_area_float_values():
    result = triangle_area(2.5, 4.0)
    assert result == 5.0


def test_triangle_area_zero_base():
    result = triangle_area(0, 10)
    assert result == 0.0
