# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

import pytest

from f159 import eat


def test_eat_need_within_remaining():
    """Covers lines 3-4: need <= remaining branch."""
    result = eat(5, 3, 10)
    assert result == [8, 7]
    assert result[0] == 5 + 3
    assert result[1] == 10 - 3


def test_eat_need_exactly_remaining():
    """Covers the boundary of the branch on line 3 (need == remaining)."""
    result = eat(2, 5, 5)
    assert result == [7, 0]
    assert result[0] == 2 + 5
    assert result[1] == 5 - 5


def test_eat_need_exceeds_remaining():
    """Covers lines 3, 5-6: need > remaining branch."""
    result = eat(5, 10, 3)
    assert result == [8, 0]
    assert result[0] == 5 + 3
    assert result[1] == 0
