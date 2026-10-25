# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f042 import incr_list


def test_incr_list_typical():
    result = incr_list([1, 2, 3])
    assert result == [2, 3, 4]


def test_incr_list_empty():
    result = incr_list([])
    assert result == []


def test_incr_list_negative_and_zero():
    result = incr_list([-1, 0, 5])
    assert result == [0, 1, 6]


def test_incr_list_does_not_mutate_input():
    data = [1, 2, 3]
    original = list(data)
    result = incr_list(data)
    assert result == [2, 3, 4]
    assert data == original
