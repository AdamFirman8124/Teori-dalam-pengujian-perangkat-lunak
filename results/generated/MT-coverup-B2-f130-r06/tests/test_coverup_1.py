# file: project/f130/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}

"""Tests for f130.tri covering all previously unexecuted lines (3-11).

The function under test is pure (no module state, no I/O, no globals),
so no monkeypatching or teardown is required; each test is fully
self-contained and leaves no state behind.
"""

from f130 import tri


def test_tri_zero_hits_early_return():
    """Covers lines 3-4: the n == 0 branch."""
    assert tri(0) == [1]


def test_tri_one_skips_loop_body():
    """Covers line 5 and line 11 with the loop body never entered (n=1)."""
    assert tri(1) == [1, 3]


def test_tri_even_branch():
    """Covers lines 6-8: loop entry and the even-index append."""
    result = tri(2)
    assert result == [1, 3, 2.0]
    # Postcondition: last element follows the even formula i / 2 + 1.
    assert result[-1] == 2 / 2 + 1


def test_tri_odd_branch():
    """Covers lines 9-10: the else branch (odd-index append)."""
    result = tri(3)
    assert result == [1, 3, 2.0, 8.0]
    # Postcondition: last element follows the odd recurrence.
    assert result[-1] == result[2] + result[1] + (3 + 3) / 2


def test_tri_alternating_branches():
    """Exercises both branches repeatedly within one call (i = 2..5)."""
    result = tri(5)
    assert result == [1, 3, 2.0, 8.0, 3.0, 15.0]
    # Postconditions for each appended element:
    assert result[2] == 2 / 2 + 1          # even branch, i = 2
    assert result[3] == result[2] + result[1] + (3 + 3) / 2  # odd, i = 3
    assert result[4] == 4 / 2 + 1          # even branch, i = 4
    assert result[5] == result[4] + result[3] + (5 + 3) / 2  # odd, i = 5
    # Postcondition: length is n + 1 for n >= 1.
    assert len(result) == 6
