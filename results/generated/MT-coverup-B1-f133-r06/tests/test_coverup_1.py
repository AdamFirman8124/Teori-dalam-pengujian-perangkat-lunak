# file: project/f133/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest

from f133 import sum_squares


def test_sum_squares_nonempty_list():
    # Covers: import math, squared = 0, loop body, return
    result = sum_squares([1.2, 2.5, -3.0])
    # math.ceil(1.2)=2 -> 4, math.ceil(2.5)=3 -> 9, math.ceil(-3.0)=-3 -> 9
    assert result == 4 + 9 + 9


def test_sum_squares_empty_list():
    # Covers: import math, squared = 0, loop skipped, return
    assert sum_squares([]) == 0
