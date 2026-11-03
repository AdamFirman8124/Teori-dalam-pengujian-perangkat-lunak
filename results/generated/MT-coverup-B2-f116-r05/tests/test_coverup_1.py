# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f116 import sort_array


def test_sort_array_counts_ones():
    # Pre-sorted: [1, 2, 3, 4, 5]
    # Ones in binary: 1->1, 2->1, 3->2, 4->1, 5->2
    # Stable sort by ones count: [1, 2, 4, 3, 5]
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]


def test_sort_array_empty():
    assert sort_array([]) == []


def test_sort_array_single_element():
    assert sort_array([7]) == [7]


def test_sort_array_ties_preserve_numeric_order():
    # 1 and 2 both have a single '1' bit; the inner numeric sort
    # must keep 1 before 2 in the result.
    assert sort_array([2, 1]) == [1, 2]


def test_sort_array_multi_digit_counts():
    # 7 -> '111' (3 ones), 8 -> '1000' (1 one), 15 -> '1111' (4 ones)
    # Pre-sorted: [3, 7, 8, 15]; ones: 3->2, 7->3, 8->1, 15->4
    assert sort_array([15, 7, 3, 8]) == [8, 3, 7, 15]
