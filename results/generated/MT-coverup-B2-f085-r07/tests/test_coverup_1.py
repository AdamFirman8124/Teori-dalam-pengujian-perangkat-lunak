# file: project/f085/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f085 import add


def test_add_sums_even_values_at_odd_indices():
    # Indices 1 and 3 hold 2 and 4, both even -> both included.
    assert add([1, 2, 3, 4]) == 6


def test_add_skips_odd_values_at_odd_indices():
    # Index 1 holds 4 (even, included); index 3 holds 5 (odd, skipped).
    # Covers both the True and False branches of the comprehension filter.
    assert add([1, 4, 3, 5]) == 4


def test_add_all_odd_values_at_odd_indices():
    # Index 1 holds 3 (odd) -> filter excludes it, sum is 0.
    assert add([2, 3]) == 0


def test_add_empty_list():
    # range(1, 0, 2) is empty: comprehension body never runs, sum is 0.
    assert add([]) == 0


def test_add_single_element_list():
    # range(1, 1, 2) is empty: no odd indices exist, sum is 0.
    assert add([7]) == 0
