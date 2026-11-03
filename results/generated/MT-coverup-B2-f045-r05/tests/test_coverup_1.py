# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_basic():
    """Calling the function executes line 3 (the return statement)."""
    result = triangle_area(3, 4)
    assert result == 6.0
    assert isinstance(result, float)


def test_triangle_area_fractional():
    """Verify correct area computation with non-integer inputs."""
    result = triangle_area(2.5, 1.2)
    assert result == pytest.approx(1.5)


def test_triangle_area_zero_base():
    """A degenerate triangle (zero base) has zero area."""
    assert triangle_area(0, 5) == 0.0
