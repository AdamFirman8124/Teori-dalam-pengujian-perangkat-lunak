# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest

from f133 import sum_squares


def test_sum_squares_empty_list():
    """Covers lines 3-4, 7: import, initialization, and return with no loop iterations."""
    assert sum_squares([]) == 0


def test_sum_squares_integers():
    """Covers lines 3-7 with integer inputs (ceil is identity for ints)."""
    assert sum_squares([1, 2, 3]) == 1 + 4 + 9


def test_sum_squares_floats_uses_ceil():
    """Covers lines 3-7 with float inputs to exercise math.ceil."""
    # ceil(1.2) == 2 -> 4, ceil(2.7) == 3 -> 9, total 13
    assert sum_squares([1.2, 2.7]) == 13


def test_sum_squares_negative_floats():
    """Covers lines 3-7 with negative floats (ceil rounds toward +infinity)."""
    # ceil(-1.5) == -1 -> 1, ceil(-0.2) == 0 -> 0, total 1
    assert sum_squares([-1.5, -0.2]) == 1


def test_sum_squares_mixed():
    """Covers lines 3-7 with a mixed list of ints and floats."""
    # ceil(0.5) == 1 -> 1, ceil(3) == 3 -> 9, ceil(-2.1) == -2 -> 4, total 14
    assert sum_squares([0.5, 3, -2.1]) == 14
