# file: project/f130/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}

"""Tests for f130.tri covering all previously uncovered lines (3-11) and branches.

tri is a pure function (no I/O, no module state), so no monkeypatching or
teardown is required; each test simply calls it with fresh arguments.
"""

import pytest

from f130 import tri


def test_tri_base_case_zero():
    """n == 0 hits the early return on line 4."""
    assert tri(0) == [1]


def test_tri_one_skips_loop():
    """n == 1 builds my_tri (line 5) but the loop body never runs (loop-false branch)."""
    result = tri(1)
    assert result == [1, 3]
    assert len(result) == 2


def test_tri_even_branch():
    """n == 2 enters the loop and takes the even branch (i % 2 == 0, line 8)."""
    result = tri(2)
    assert result == [1, 3, 2.0]  # i=2 -> 2/2 + 1 == 2.0
    assert result[-1] == 2 / 2 + 1


def test_tri_odd_branch():
    """n == 3 takes the odd branch (line 10) using previously appended values."""
    result = tri(3)
    # i=3 -> my_tri[2] + my_tri[1] + (3+3)/2 == 2.0 + 3 + 3.0 == 8.0
    assert result == [1, 3, 2.0, 8.0]
    assert result[-1] == result[2] + result[1] + (3 + 3) / 2


def test_tri_both_branches_and_return():
    """n == 5 exercises even and odd branches together and the final return (line 11)."""
    result = tri(5)
    assert result == [1, 3, 2.0, 8.0, 3.0, 15.0]
    # Even branch value: i=4 -> 4/2 + 1
    assert result[4] == 4 / 2 + 1
    # Odd branch value: i=5 -> my_tri[4] + my_tri[3] + (5+3)/2
    assert result[5] == result[4] + result[3] + (5 + 3) / 2


@pytest.mark.parametrize("n,expected", [
    (0, [1]),
    (1, [1, 3]),
    (2, [1, 3, 2.0]),
    (3, [1, 3, 2.0, 8.0]),
    (4, [1, 3, 2.0, 8.0, 3.0]),
    (5, [1, 3, 2.0, 8.0, 3.0, 15.0]),
])
def test_tri_parametrized(n, expected):
    """Table-driven check that also re-exercises every branch."""
    assert tri(n) == expected
