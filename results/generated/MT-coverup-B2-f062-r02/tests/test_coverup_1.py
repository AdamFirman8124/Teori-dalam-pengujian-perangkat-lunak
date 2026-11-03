# file: project/f062/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f062 import derivative


def test_derivative_basic():
    """Covers line 3: enumerate, multiply by index, slice off first element."""
    result = derivative([1, 2, 3])
    # enumerate -> (0,1),(1,2),(2,3) -> [0, 2, 6] -> drop first -> [2, 6]
    assert result == [2, 6]


def test_derivative_empty_list():
    """Covers line 3 with an empty input list."""
    assert derivative([]) == []


def test_derivative_single_element():
    """Covers line 3 where the slice removes the only element."""
    assert derivative([5]) == []


def test_derivative_with_zero_and_negatives():
    """Covers line 3 with zero and negative values."""
    result = derivative([0, -1, 4])
    # enumerate -> (0,0),(1,-1),(2,4) -> [0, -1, 8] -> drop first -> [-1, 8]
    assert result == [-1, 8]
