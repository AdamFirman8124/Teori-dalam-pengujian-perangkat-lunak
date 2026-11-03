# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

import pytest

from f159 import eat


def test_eat_need_le_remaining():
    """Covers lines 3-4: the branch where need <= remaining."""
    # need strictly less than remaining
    assert eat(5, 3, 10) == [8, 7]
    # boundary case: need == remaining (still takes the if-branch)
    assert eat(2, 4, 4) == [6, 0]
    # boundary case: need == 0
    assert eat(7, 0, 3) == [7, 3]


def test_eat_need_gt_remaining():
    """Covers lines 5-6: the else branch where need > remaining."""
    assert eat(1, 10, 5) == [6, 0]
    # boundary case: remaining == 0
    assert eat(4, 2, 0) == [4, 0]
