# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_executes_return_line():
    """Execute line 3 (the return statement) and verify the computed area."""
    # Integer inputs: 3 * 4 / 2.0 == 6.0
    result = triangle_area(3, 4)
    assert result == 6.0
    assert isinstance(result, float)

    # Float inputs: 2.5 * 1.2 / 2.0 == 1.5
    result = triangle_area(2.5, 1.2)
    assert result == pytest.approx(1.5)

    # Zero height yields zero area
    assert triangle_area(10, 0) == 0.0

    # Fractional result: 1 * 1 / 2.0 == 0.5
    assert triangle_area(1, 1) == 0.5
