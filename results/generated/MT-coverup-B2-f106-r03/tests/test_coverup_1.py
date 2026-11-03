# file: project/f106/__init__.py:1-13
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13], "branches": [[4, 5], [4, 13], [5, 6], [5, 10], [7, 7], [7, 8], [11, 11], [11, 12]]}

import pytest

from f106 import f


def test_f_empty_range():
    """n <= 0: loop body never runs; covers lines 3 and 13 only."""
    assert f(0) == []
    assert f(-3) == []


def test_f_odd_only():
    """n = 1: only the odd branch (triangular sum) executes."""
    assert f(1) == [1]


def test_f_even_and_odd_branches():
    """n = 5: covers every line 3-13, both if/else branches, and
    inner loops with multiple iterations.

    For each i in 1..n:
      - even i -> factorial of i
      - odd i  -> sum of 1..i
    """
    result = f(5)
    assert result == [1, 2, 6, 24, 15]
    # Postconditions: even positions hold factorials, odd hold sums.
    assert result[1] == 2 and result[3] == 24          # 2!, 4!
    assert result[0] == 1 and result[2] == 6 and result[4] == 15  # 1, 1+2+3, 1+..+5
    assert len(result) == 5
