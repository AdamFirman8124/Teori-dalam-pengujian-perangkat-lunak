# file: project/f130/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}

import pytest

from f130 import tri


def test_tri_zero():
    """Covers lines 3-4: n == 0 returns [1]."""
    assert tri(0) == [1]


def test_tri_one():
    """Covers line 5 and line 11: base list returned, loop body never runs."""
    assert tri(1) == [1, 3]


def test_tri_even_index():
    """Covers lines 6-8: even i appends i / 2 + 1."""
    result = tri(2)
    assert result == [1, 3, 2.0]
    assert result[2] == 2 / 2 + 1


def test_tri_odd_index():
    """Covers lines 9-10: odd i appends recurrence with (i + 3) / 2."""
    result = tri(3)
    expected_last = result[2] + result[1] + (3 + 3) / 2
    assert result == [1, 3, 2.0, expected_last]
    assert result[3] == 2.0 + 3 + 3.0


def test_tri_mixed_branches():
    """Covers both branches across a longer run and the final return (line 11)."""
    result = tri(5)
    assert len(result) == 6
    # i = 4 is even -> line 8
    assert result[4] == 4 / 2 + 1
    # i = 5 is odd -> line 10
    assert result[5] == result[4] + result[3] + (5 + 3) / 2
