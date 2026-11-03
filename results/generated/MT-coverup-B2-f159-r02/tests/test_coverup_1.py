# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

import pytest

from f159 import eat


def test_eat_need_less_than_remaining():
    """Covers line 3 (True branch) and line 4: need < remaining."""
    result = eat(5, 2, 10)
    assert result == [5 + 2, 10 - 2]
    assert result == [7, 8]


def test_eat_need_equals_remaining():
    """Covers line 3 (True branch) and line 4: need == remaining (boundary)."""
    result = eat(3, 4, 4)
    assert result == [3 + 4, 4 - 4]
    assert result == [7, 0]


def test_eat_need_greater_than_remaining():
    """Covers line 6 (False branch): need > remaining."""
    result = eat(10, 5, 3)
    assert result == [10 + 3, 0]
    assert result == [13, 0]


def test_eat_zero_remaining():
    """Covers line 6 (False branch): nothing left to eat."""
    result = eat(1, 1, 0)
    assert result == [1 + 0, 0]
    assert result == [1, 0]
