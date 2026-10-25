# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f042 import incr_list


def test_incr_list_increments_each_element():
    values = [0, 1, 2, -3]
    original = values.copy()

    result = incr_list(values)

    assert result == [1, 2, 3, -2]
    assert values == original
    assert result is not values


def test_incr_list_returns_empty_list_for_empty_input():
    values = []

    result = incr_list(values)

    assert result == []
    assert result is not values
