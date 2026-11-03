# file: project/f130/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}

import pytest

from f130 import tri


def test_tri_zero():
    """n == 0 hits the early return on lines 3-4."""
    assert tri(0) == [1]


def test_tri_one_loop_not_entered():
    """n == 1 hits line 5 but the loop body never runs (range(2, 2) is empty)."""
    assert tri(1) == [1, 3]


def test_tri_even_branch():
    """n == 2 exercises the even branch (lines 7-8)."""
    # i = 2 is even -> append 2 / 2 + 1 == 2.0
    assert tri(2) == [1, 3, 2.0]


def test_tri_odd_branch():
    """n == 3 exercises the odd branch (lines 9-10)."""
    # i = 2 even -> 2.0; i = 3 odd -> my_tri[2] + my_tri[1] + (3 + 3) / 2 == 2.0 + 3 + 3.0
    assert tri(3) == [1, 3, 2.0, 8.0]


def test_tri_mixed_sequence():
    """Larger n alternates both branches, covering lines 6-11 fully."""
    result = tri(5)
    # i=2 (even): 2/2 + 1 = 2.0
    # i=3 (odd):  2.0 + 3 + (3+3)/2 = 8.0
    # i=4 (even): 4/2 + 1 = 3.0
    # i=5 (odd):  3.0 + 8.0 + (5+3)/2 = 15.0
    assert result == [1, 3, 2.0, 8.0, 3.0, 15.0]
    assert len(result) == 6


def test_tri_length_matches_n():
    """Postcondition: result length is n + 1 for n >= 1."""
    for n in (1, 2, 3, 4, 5, 6, 7):
        assert len(tri(n)) == n + 1


def test_tri_is_pure_no_state_pollution():
    """Calling twice yields identical results (no shared mutable state)."""
    first = tri(4)
    second = tri(4)
    assert first == second == [1, 3, 2.0, 8.0, 3.0]
