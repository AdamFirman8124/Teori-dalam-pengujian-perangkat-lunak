# file: project/f159/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [3, 4, 6], "branches": [[3, 4], [3, 6]]}

from f159 import eat


def test_eat_need_within_remaining():
    """Covers the if-branch (lines 3-4): need <= remaining."""
    result = eat(5, 3, 10)
    assert result == [8, 7]
    assert result[0] == 5 + 3
    assert result[1] == 10 - 3


def test_eat_need_equals_remaining():
    """Covers the boundary of the if-branch: need == remaining."""
    result = eat(2, 4, 4)
    assert result == [6, 0]
    assert result[0] == 2 + 4
    assert result[1] == 4 - 4


def test_eat_need_exceeds_remaining():
    """Covers the else-branch (line 6): need > remaining."""
    result = eat(5, 10, 3)
    assert result == [8, 0]
    assert result[0] == 5 + 3
    assert result[1] == 0
