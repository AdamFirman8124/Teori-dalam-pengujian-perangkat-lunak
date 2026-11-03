# file: project/f070/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}

from f070 import strange_sort_list


def test_empty_list_returns_empty():
    """Covers lines 3, 4 (loop never entered) and 8."""
    assert strange_sort_list([]) == []


def test_single_element():
    """Covers one loop iteration: min branch, remove, toggle, exit."""
    assert strange_sort_list([7]) == [7]


def test_even_length_alternates_min_and_max():
    """Covers both the min (switch True) and max (switch False) branches."""
    src = [4, 1, 3, 2]
    result = strange_sort_list(list(src))  # pass a copy: function mutates its arg
    assert result == [1, 4, 2, 3]
    # postconditions: same multiset, alternating smallest/largest
    assert sorted(result) == sorted(src)
    assert result[0] == min(src)
    assert result[1] == max(src)


def test_odd_length_with_duplicates_and_negatives():
    """Exercises min/max branches with repeated values and negative numbers."""
    src = [5, -2, 5, 0, 3]
    result = strange_sort_list(list(src))
    assert result == [-2, 5, 0, 5, 3]
    assert sorted(result) == sorted(src)


def test_alternation_property():
    """Verifies the alternating min/max pattern against a reference construction."""
    src = [9, 9, 1, 8, 2, 7, 3]
    result = strange_sort_list(list(src))
    remaining = sorted(src)
    expected = []
    take_min = True
    while remaining:
        expected.append(remaining.pop(0) if take_min else remaining.pop())
        take_min = not take_min
    assert result == expected
    assert sorted(result) == sorted(src)
