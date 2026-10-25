# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f042 import incr_list


def test_incr_list_increments_each_element_without_mutating_input():
    values = [0, 1, -2, 10]
    original_values = values.copy()

    result = incr_list(values)

    assert result == [1, 2, -1, 11]
    assert values == original_values
    assert result is not values
