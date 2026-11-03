# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

import pytest

from f159 import eat


def test_eat_enough_remaining():
    """Covers lines 3-4: the need <= remaining branch."""
    result = eat(5, 3, 10)
    # number + need, remaining - need
    assert result == [8, 7]
    assert result[0] == 5 + 3
    assert result[1] == 10 - 3


def test_eat_exactly_enough_remaining():
    """Covers the boundary of lines 3-4: need == remaining."""
    result = eat(2, 5, 5)
    assert result == [7, 0]
    assert result[0] == 2 + 5
    assert result[1] == 5 - 5


def test_eat_not_enough_remaining():
    """Covers lines 5-6: the need > remaining branch."""
    result = eat(5, 12, 4)
    # number + remaining, 0
    assert result == [9, 0]
    assert result[0] == 5 + 4
    assert result[1] == 0
