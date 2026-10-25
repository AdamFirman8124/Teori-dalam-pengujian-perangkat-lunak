# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f042 import incr_list


def test_incr_list_increments_each_element_without_mutating_input():
    values = [0, -2, 41]

    result = incr_list(values)

    assert result == [1, -1, 42]
    assert values == [0, -2, 41]
    assert result is not values
