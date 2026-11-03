# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_executes_return_line():
    """Calling triangle_area executes line 3 (the return statement)."""
    # Integer inputs: area of a 3x4 triangle is 6.0
    result = triangle_area(3, 4)
    assert result == 6.0
    assert isinstance(result, float)

    # Zero base yields zero area
    assert triangle_area(0, 5) == 0.0

    # Float inputs: 2.5 * 2 / 2.0 == 2.5
    assert triangle_area(2.5, 2) == 2.5

    # Fractional result: 1 * 1 / 2.0 == 0.5
    assert triangle_area(1, 1) == 0.5
