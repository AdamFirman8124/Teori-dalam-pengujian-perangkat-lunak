# file: project/f070/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}

from f070 import strange_sort_list


def test_strange_sort_list_empty():
    # Covers line 3 and line 8 with the while-loop body never taken (line 4 False branch).
    assert strange_sort_list([]) == []


def test_strange_sort_list_single():
    # Covers one iteration: min branch (switch True), remove, toggle, return.
    assert strange_sort_list([7]) == [7]


def test_strange_sort_list_two():
    # Covers both min (switch True) and max (switch False) branches.
    assert strange_sort_list([2, 1]) == [1, 2]


def test_strange_sort_list_even_length():
    # Alternating min/max over an even-length list.
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]


def test_strange_sort_list_odd_length():
    # Alternating min/max over an odd-length list.
    assert strange_sort_list([5, 1, 3, 2, 4]) == [1, 5, 2, 4, 3]


def test_strange_sort_list_duplicates():
    # Duplicates: min == max, remove() still removes one occurrence per step.
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]


def test_strange_sort_list_negatives():
    # Works with negative numbers too.
    assert strange_sort_list([-1, -3, 2, 0]) == [-3, 2, -1, 0]


def test_strange_sort_list_consumes_input_list():
    # The function mutates its argument (lst.remove); verify that postcondition
    # on a local list so no shared state is polluted.
    lst = [3, 1, 2]
    result = strange_sort_list(lst)
    assert result == [1, 3, 2]
    assert lst == []
