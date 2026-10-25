# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f085 import add


def test_add_sums_even_values_at_odd_indices():
    # indices 1, 3, 5 hold 2, 4, 6 (all even) -> 2 + 4 + 6 = 12
    assert add([1, 2, 3, 4, 5, 6]) == 12


def test_add_skips_odd_values_at_odd_indices():
    # index 1 holds 3 (odd) -> excluded; index 3 holds 4 (even) -> included
    assert add([0, 3, 0, 4]) == 4


def test_add_empty_list():
    assert add([]) == 0


def test_add_no_even_values_at_odd_indices():
    assert add([1, 1, 1, 1]) == 0
