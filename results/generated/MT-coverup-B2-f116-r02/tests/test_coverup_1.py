# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f116 import sort_array


def test_sort_array_basic():
    """Covers line 3: the return statement with a non-trivial array."""
    arr = [1, 5, 2, 3, 4]
    result = sort_array(arr)
    # sorted ascending: [1, 2, 3, 4, 5]
    # bit counts: 1->1, 2->1, 3->2, 4->1, 5->2
    # stable sort by bit count: [1, 2, 4, 3, 5]
    assert result == [1, 2, 4, 3, 5]


def test_sort_array_empty():
    """Covers line 3 with an empty input."""
    assert sort_array([]) == []


def test_sort_array_stability_and_no_mutation():
    """Elements with equal bit counts keep their ascending order; input is unchanged."""
    arr = [7, 3, 5, 1]
    result = sort_array(arr)
    # sorted ascending: [1, 3, 5, 7]
    # bit counts: 1->1, 3->2, 5->2, 7->3
    # stable: [1, 3, 5, 7]
    assert result == [1, 3, 5, 7]
    # the original list must not be mutated
    assert arr == [7, 3, 5, 1]
