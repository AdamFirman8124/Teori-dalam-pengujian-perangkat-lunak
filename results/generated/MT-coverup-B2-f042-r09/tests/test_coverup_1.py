# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f042 import incr_list


def test_incr_list_increments_each_element():
    assert incr_list([0, 1, 2, -3]) == [1, 2, 3, -2]


def test_incr_list_returns_empty_list_for_empty_input():
    assert incr_list([]) == []
