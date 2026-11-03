# file: project/f062/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f062 import derivative


def test_derivative_basic():
    """Covers line 3: the list comprehension and slice on a multi-element list."""
    result = derivative([1, 2, 3])
    # enumerate yields (0,1),(1,2),(2,3) -> [0, 2, 6]; slicing drops the first element
    assert result == [2, 6]


def test_derivative_empty_list():
    """Covers line 3 with an empty input; comprehension yields [] and slice stays []."""
    assert derivative([]) == []


def test_derivative_single_element():
    """Covers line 3 with one element; the only item is sliced away."""
    assert derivative([5]) == []


def test_derivative_with_floats_and_zero():
    """Covers line 3 with non-integer values, verifying element-wise i * x."""
    result = derivative([0.5, 2.0, 3.0, 4.0])
    # [0*0.5, 1*2.0, 2*3.0, 3*4.0] = [0.0, 2.0, 6.0, 12.0]; drop first
    assert result == [2.0, 6.0, 12.0]


def test_derivative_does_not_mutate_input():
    """Covers line 3 and verifies the input list is left untouched (no state pollution)."""
    xs = [1, 2, 3]
    original = list(xs)
    derivative(xs)
    assert xs == original
