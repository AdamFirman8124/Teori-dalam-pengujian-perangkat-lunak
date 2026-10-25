# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f042 import incr_list


def test_incr_list_basic():
    result = incr_list([1, 2, 3])
    assert result == [2, 3, 4]


def test_incr_list_empty():
    result = incr_list([])
    assert result == []


def test_incr_list_does_not_mutate_input():
    original = [0, -1, 10]
    snapshot = list(original)
    result = incr_list(original)
    assert result == [1, 0, 11]
    assert original == snapshot
