# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import f085


def test_add_sums_even_values_at_odd_indices():
    assert f085.add([1, 2, 3, 4]) == 6


def test_add_ignores_odd_values_at_odd_indices():
    assert f085.add([1, 3, 5, 7]) == 0


def test_add_mixed_parity():
    assert f085.add([10, 1, 20, 2, 30, 3, 40, 4]) == 6


def test_add_empty_list_returns_zero():
    assert f085.add([]) == 0


def test_add_single_element_returns_zero():
    assert f085.add([2]) == 0


def test_add_two_elements_uses_index_one():
    assert f085.add([1, 2]) == 2
    assert f085.add([1, 3]) == 0


def test_add_does_not_mutate_input():
    lst = [1, 2, 3, 4]
    f085.add(lst)
    assert lst == [1, 2, 3, 4]
