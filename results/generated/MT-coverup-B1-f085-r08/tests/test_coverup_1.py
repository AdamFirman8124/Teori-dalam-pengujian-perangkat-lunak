# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f085 import add


def test_add_empty_list():
    assert add([]) == 0


def test_add_single_element():
    assert add([7]) == 0


def test_add_only_odd_index_values_odd():
    assert add([1, 3, 5, 7]) == 0


def test_add_only_odd_index_values_even():
    assert add([1, 2, 3, 4]) == 6


def test_add_mixed_parity():
    assert add([9, 1, 8, 2, 7, 3, 6, 4]) == 6


def test_add_negative_even_values():
    assert add([0, -2, 0, -4]) == -6


def test_add_does_not_mutate_input():
    lst = [1, 2, 3, 4, 5, 6]
    original = list(lst)
    add(lst)
    assert lst == original


def test_add_zero_values():
    assert add([0, 0, 0, 0]) == 0
