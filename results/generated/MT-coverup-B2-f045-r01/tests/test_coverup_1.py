# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_executes_return_line():
    """Calling triangle_area executes line 3 (the return statement).

    The function is pure (no I/O, no global state), so no cleanup or
    monkeypatching is required; nothing is mutated by the call.
    """
    # Basic case: base 3, height 4 -> area 6.0
    result = triangle_area(3, 4)
    assert result == 6.0
    assert isinstance(result, float)

    # Zero base yields zero area
    assert triangle_area(0, 5) == 0.0

    # Float inputs
    assert triangle_area(2.5, 4.0) == 5.0

    # Fractional result: (1 * 1) / 2.0 == 0.5
    assert triangle_area(1, 1) == 0.5

    # Property check: area is exactly half of a * h
    a, h = 7, 13
    assert triangle_area(a, h) == pytest.approx(a * h / 2.0)
