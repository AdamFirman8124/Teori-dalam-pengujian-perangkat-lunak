# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f116 import sort_array


def test_sort_array_orders_by_bit_count_without_mutating_input():
    values = [7, 1, 8, 3, 2, 4]
    original = values.copy()

    result = sort_array(values)

    assert result == [1, 2, 4, 8, 3, 7]
    assert values == original
