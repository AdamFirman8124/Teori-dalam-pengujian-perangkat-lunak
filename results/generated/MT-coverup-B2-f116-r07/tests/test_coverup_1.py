# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f116 import sort_array


def test_sort_array_orders_by_set_bits_then_value():
    values = [3, 1, 4, 2]
    original = values.copy()

    result = sort_array(values)

    assert result == [1, 2, 4, 3]
    assert values == original


def test_sort_array_handles_empty_list():
    assert sort_array([]) == []
