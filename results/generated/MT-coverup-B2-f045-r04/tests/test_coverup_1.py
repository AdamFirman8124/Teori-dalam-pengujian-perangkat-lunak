# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_executes_return_line():
    """Call triangle_area so that line 3 (the return statement) executes,
    and verify the computed area is correct."""
    # Integer inputs
    assert triangle_area(3, 4) == pytest.approx(6.0)
    assert triangle_area(10, 5) == pytest.approx(25.0)

    # Float inputs
    assert triangle_area(2.5, 4.0) == pytest.approx(5.0)
    assert triangle_area(1.5, 0.5) == pytest.approx(0.375)

    # Zero and negative inputs
    assert triangle_area(0, 7) == pytest.approx(0.0)
    assert triangle_area(-3, 6) == pytest.approx(-9.0)

    # Result is always a float because of the division by 2.0
    assert isinstance(triangle_area(3, 4), float)
    assert isinstance(triangle_area(3, 4), float)  # consistent return type


def test_triangle_area_matches_formula():
    """Verify the return value exactly matches a * h / 2.0 for various inputs."""
    for a, h in [(1, 1), (5, 3), (100, 0.01), (-7.25, 2)]:
        assert triangle_area(a, h) == pytest.approx(a * h / 2.0)
