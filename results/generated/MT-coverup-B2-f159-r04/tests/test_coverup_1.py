# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

import pytest

from f159 import eat


def test_eat_need_less_than_remaining():
    """Covers lines 3-4: need <= remaining branch (strictly less)."""
    result = eat(5, 6, 10)
    assert result == [11, 4]
    assert result[0] == 5 + 6
    assert result[1] == 10 - 6


def test_eat_need_equals_remaining():
    """Covers lines 3-4: boundary case need == remaining."""
    result = eat(1, 5, 5)
    assert result == [6, 0]
    assert result[0] == 1 + 5
    assert result[1] == 5 - 5


def test_eat_need_greater_than_remaining():
    """Covers lines 5-6: else branch (need > remaining)."""
    result = eat(2, 9, 5)
    assert result == [7, 0]
    assert result[0] == 2 + 5
    assert result[1] == 0


def test_eat_zero_need():
    """Covers lines 3-4: zero need is <= any remaining."""
    result = eat(3, 0, 7)
    assert result == [3, 7]
