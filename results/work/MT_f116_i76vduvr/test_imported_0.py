# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f116 import sort_array


def test_sort_array_orders_by_set_bit_count_without_mutating_input():
    values = [5, 3, 7, 8, 2, 6]
    original = values.copy()

    result = sort_array(values)

    assert result == [2, 8, 3, 5, 6, 7]
    assert values == original
