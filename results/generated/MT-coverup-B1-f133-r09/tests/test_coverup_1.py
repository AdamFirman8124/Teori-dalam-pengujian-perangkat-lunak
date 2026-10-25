# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest

from f133 import sum_squares


def test_sum_squares_empty_list():
    """Covers lines 3-4 (import, init) and line 7 (return) with an empty list."""
    assert sum_squares([]) == 0


def test_sum_squares_positive_integers():
    """Covers lines 3-7 with positive integers (ceil is identity)."""
    assert sum_squares([1, 2, 3]) == 1 + 4 + 9


def test_sum_squares_negative_and_floats():
    """Covers lines 3-7 with negative values and floats, exercising math.ceil."""
    # ceil(-2.5) == -2 -> 4; ceil(3.2) == 4 -> 16; ceil(-1.0) == -1 -> 1
    assert sum_squares([-2.5, 3.2, -1.0]) == 4 + 16 + 1
