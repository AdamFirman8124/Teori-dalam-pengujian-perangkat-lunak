# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f042 import incr_list


def test_incr_list_increments_each_element():
    values = [0, 1, -2]
    assert incr_list(values) == [1, 2, -1]
    assert values == [0, 1, -2]


def test_incr_list_handles_empty_list():
    assert incr_list([]) == []
