# file: project/f045/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f045 import triangle_area


def test_triangle_area_executes_return_line():
    """Calling triangle_area executes line 3 (the return statement).

    Postcondition: the returned value equals a * h / 2.0.
    """
    result = triangle_area(3, 4)
    assert result == 3 * 4 / 2.0
    assert result == 6.0
    assert isinstance(result, float)


def test_triangle_area_zero_base():
    """Edge case: zero base still executes line 3 and yields 0.0."""
    result = triangle_area(0, 5)
    assert result == 0.0


def test_triangle_area_float_inputs():
    """Float inputs also execute line 3 and produce the correct area."""
    result = triangle_area(2.5, 4.0)
    assert result == pytest.approx(5.0)
