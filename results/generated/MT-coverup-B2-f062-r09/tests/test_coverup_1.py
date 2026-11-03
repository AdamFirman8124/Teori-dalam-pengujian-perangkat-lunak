# file: project/f062/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f062 import derivative


def test_derivative_basic():
    """Calling derivative must execute line 3 and return the expected slice."""
    xs = [1, 2, 3, 4]
    # enumerate -> [(0,1),(1,2),(2,3),(3,4)] -> [0,2,6,12] -> sliced [1:]
    assert derivative(xs) == [2, 6, 12]


def test_derivative_empty_list():
    """Even an empty input executes line 3 and yields an empty result."""
    assert derivative([]) == []


def test_derivative_single_element():
    """A single-element list loses its first (index 0) element after slicing."""
    assert derivative([5]) == []


def test_derivative_with_zeroes_and_negatives():
    """Zero and negative values are multiplied by their index as-is."""
    xs = [0, -3, 4]
    # [0*0, 1*-3, 2*4] -> [0, -3, 8] -> [1:] -> [-3, 8]
    assert derivative(xs) == [-3, 8]


def test_derivative_does_not_mutate_input():
    """The function is pure: the input list must remain unchanged."""
    xs = [1, 2, 3]
    xs_copy = list(xs)
    result = derivative(xs)
    assert xs == xs_copy  # no side effects on the argument
    assert result == [2, 6]
