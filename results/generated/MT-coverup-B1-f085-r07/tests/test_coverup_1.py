# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f085 import add


def test_add_with_even_elements_at_odd_indices():
    # indices 1 and 3 hold even numbers -> both included in the sum
    assert add([1, 2, 3, 4]) == 6


def test_add_with_odd_elements_at_odd_indices():
    # indices 1 and 3 hold odd numbers -> filtered out, sum is 0
    assert add([1, 1, 3, 3]) == 0


def test_add_empty_list():
    assert add([]) == 0


def test_add_single_element():
    # no odd indices exist
    assert add([2]) == 0


def test_add_mixed():
    # index 1 -> 4 (even, included), index 3 -> 5 (odd, excluded)
    assert add([0, 4, 0, 5, 0, 6]) == 10
