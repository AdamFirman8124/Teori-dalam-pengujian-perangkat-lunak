# file: project/f062/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f062 import derivative


def test_derivative_basic_executes_line_3():
    """Covers line 3: the list comprehension runs with multiple iterations.

    For polynomial coefficients [c0, c1, c2, ...], the derivative is
    [1*c1, 2*c2, ...] (the i=0 term is dropped by the [1:] slice).
    """
    # 3 + 4x + 5x^2  ->  4 + 10x
    assert derivative([3, 4, 5]) == [4, 10]
    # 1 + 2x + 3x^2 + 4x^3  ->  2 + 6x + 12x^2
    assert derivative([1, 2, 3, 4]) == [2, 6, 12]


def test_derivative_single_element():
    """Covers the comprehension loop body executing exactly once.

    [0*7] sliced with [1:] yields an empty list.
    """
    assert derivative([7]) == []


def test_derivative_empty_list():
    """Covers the branch where the comprehension loop is never entered.

    enumerate([]) yields nothing, so the comprehension produces [] and
    the [1:] slice of [] is still [].
    """
    assert derivative([]) == []


def test_derivative_negative_and_float_values():
    """Covers the loop body with negative and floating-point coefficients."""
    # [0*0, 1*(-1), 2*2.5] == [0, -1, 5.0]; drop the first element.
    assert derivative([0, -1, 2.5]) == [-1, 5.0]
