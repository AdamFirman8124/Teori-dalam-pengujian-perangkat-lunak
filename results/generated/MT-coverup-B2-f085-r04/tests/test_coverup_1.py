# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f085 import add


def test_add_empty_list():
    assert add([]) == 0


def test_add_single_element_no_odd_index():
    assert add([10]) == 0


def test_add_all_odd_indices_even():
    # indices 1 and 3 are even -> 2 + 4 = 6
    assert add([1, 2, 3, 4]) == 6


def test_add_all_odd_indices_odd():
    # indices 1 and 3 are odd -> filtered out -> 0
    assert add([0, 1, 0, 3]) == 0


def test_add_mixed_odd_indices():
    # index 1 -> 6 (even, included), index 3 -> 3 (odd, excluded), index 5 -> 8 (even, included)
    assert add([5, 6, 7, 3, 9, 8]) == 14


def test_add_ignores_even_indices():
    # even numbers at even indices (0, 2) must be ignored
    assert add([2, 1, 4, 1]) == 0
    assert add([2, 2, 4, 4]) == 6
