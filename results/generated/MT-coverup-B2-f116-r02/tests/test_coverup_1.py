# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f116 import sort_array


def test_sort_array_orders_by_set_bits_then_value():
    values = [7, 3, 8, 2, 5, 0, 1]
    original = values.copy()

    result = sort_array(values)

    assert result == [0, 1, 2, 8, 3, 5, 7]
    assert values == original
