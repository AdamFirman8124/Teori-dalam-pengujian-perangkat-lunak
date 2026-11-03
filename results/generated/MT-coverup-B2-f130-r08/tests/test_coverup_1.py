# file: project/f130/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11], "branches": [[3, 4], [3, 5], [6, 7], [6, 11], [7, 8], [7, 10]]}

import pytest

from f130 import tri


def test_tri_zero_returns_single_element():
    """Covers lines 3-4: the n == 0 early-return branch."""
    result = tri(0)
    assert result == [1]
    assert len(result) == 1


def test_tri_one_skips_loop():
    """Covers line 5 and line 11: base list built, loop body never runs."""
    result = tri(1)
    assert result == [1, 3]


def test_tri_even_index_branch():
    """Covers lines 6-8: loop entry and the even-index append branch."""
    result = tri(2)
    # i = 2 is even -> append 2 / 2 + 1 == 2.0
    assert result == [1, 3, 2.0]
    assert result[-1] == 2.0


def test_tri_odd_index_branch():
    """Covers lines 9-10: the odd-index append branch."""
    result = tri(3)
    # i = 2 (even): 2/2 + 1 = 2.0
    # i = 3 (odd): my_tri[2] + my_tri[1] + (3 + 3) / 2 = 2.0 + 3 + 3.0 = 8.0
    assert result == [1, 3, 2.0, 8.0]
    assert result[-1] == 8.0


def test_tri_mixed_branches_and_return():
    """Covers line 11 return with both branches exercised in one call."""
    result = tri(4)
    # i = 2 (even): 2.0
    # i = 3 (odd): 2.0 + 3 + 3.0 = 8.0
    # i = 4 (even): 4/2 + 1 = 3.0
    assert result == [1, 3, 2.0, 8.0, 3.0]
    assert result[0] == 1 and result[1] == 3


def test_tri_does_not_mutate_shared_state():
    """Ensures repeated calls are independent (no state pollution)."""
    first = tri(3)
    second = tri(3)
    assert first == second == [1, 3, 2.0, 8.0]
    assert first is not second
