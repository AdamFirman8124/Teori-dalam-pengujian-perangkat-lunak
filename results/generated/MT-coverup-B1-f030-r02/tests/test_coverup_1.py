# file: project/f030/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f030 import get_positive


def test_get_positive_mixed():
    inp = [1, -2, 3, 0, -5, 4]
    result = get_positive(inp)
    assert result == [1, 3, 4]
    # verify input not mutated
    assert inp == [1, -2, 3, 0, -5, 4]


def test_get_positive_empty():
    result = get_positive([])
    assert result == []


def test_get_positive_all_non_positive():
    result = get_positive([-3, -1, 0, -10])
    assert result == []


def test_get_positive_all_positive():
    result = get_positive([2, 5, 1])
    assert result == [2, 5, 1]
