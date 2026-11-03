# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

import pytest

from f159 import eat


def test_eat_need_le_remaining():
    """Covers lines 3-4: the 'need <= remaining' branch.

    The rabbit eats exactly what it needs; the leftover carrots decrease.
    """
    # need < remaining
    assert eat(5, 3, 10) == [8, 7]
    # need == remaining (boundary): eats all remaining carrots
    assert eat(2, 4, 4) == [6, 0]


def test_eat_need_gt_remaining():
    """Covers lines 5-6: the 'else' branch (need > remaining).

    The rabbit eats only what is left, so no carrots remain.
    """
    assert eat(5, 10, 3) == [8, 0]
    # boundary just past the branch condition
    assert eat(0, 1, 0) == [0, 0]


def test_eat_returns_list_of_ints():
    """Postcondition: result is a two-element list of ints."""
    result = eat(1, 2, 3)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(x, int) for x in result)
