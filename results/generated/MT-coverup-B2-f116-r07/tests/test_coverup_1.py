# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f116 import sort_array


def test_sort_array_orders_by_number_of_ones_then_value():
    # ones count: 1->'1'(1), 2->'10'(1), 3->'11'(2), 4->'100'(1), 5->'101'(2)
    # pre-sorted [1, 2, 3, 4, 5]; stable re-sort by ones count -> [1, 2, 4, 3, 5]
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]


def test_sort_array_zero_sorts_first():
    # 0 -> bin(0)[2:] == '0' has zero ones, so it comes before everything else
    assert sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]


def test_sort_array_negative_numbers():
    # bin(-n)[2:] keeps the 'b' prefix but only '1' characters are counted:
    # -6->'b110'(2), -5->'b101'(2), -4->'b100'(1), -3->'b11'(2), -2->'b10'(1)
    assert sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]


def test_sort_array_empty_and_single_element():
    assert sort_array([]) == []
    assert sort_array([7]) == [7]


def test_sort_array_does_not_mutate_input():
    arr = [3, 1, 2]
    result = sort_array(arr)
    assert arr == [3, 1, 2]          # input list untouched
    assert result == [1, 2, 3]       # 1->1 one, 2->1 one, 3->2 ones
    assert result is not arr         # a new list is returned


def test_sort_array_matches_composite_key_sort():
    # The double sort is equivalent to sorting by (ones_count, value):
    # first pass orders by value, the stable second pass orders by ones count,
    # preserving the value order among ties.
    samples = [
        [0, 1, 2, 3, 4, 5, 6, 7],
        [7, 6, 5, 4, 3, 2, 1, 0],
        [10, 20, 30, 15, 7, 9],
        [-1, -2, -3, 0, 8],
    ]
    for arr in samples:
        expected = sorted(arr, key=lambda x: (bin(x)[2:].count('1'), x))
        assert sort_array(arr) == expected
