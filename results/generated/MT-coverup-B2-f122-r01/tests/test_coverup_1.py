# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f122 import add_elements


def test_add_elements_all_elements_within_k_are_counted():
    # Covers the generator branch where every element satisfies len(str(elem)) <= 2.
    assert add_elements([1, 22, 3], 3) == 26


def test_add_elements_filters_out_elements_with_long_repr():
    # Covers the branch where len(str(elem)) > 2, so the element is skipped.
    assert add_elements([1, 100, 22, 333, 4], 5) == 27


def test_add_elements_only_first_k_elements_are_considered():
    # Covers the arr[:k] slicing branch: elements beyond index k are ignored.
    assert add_elements([1, 2, 3, 4], 2) == 3


def test_add_elements_k_zero_returns_zero():
    # Covers the empty-slice branch (arr[:0] is empty, sum of empty generator is 0).
    assert add_elements([1, 2, 3], 0) == 0


def test_add_elements_k_larger_than_array_length():
    # Covers slicing beyond the end of the array; all elements are considered.
    assert add_elements([5, 6], 10) == 11


def test_add_elements_empty_array_returns_zero():
    # Covers the empty-array branch.
    assert add_elements([], 3) == 0


def test_add_elements_negative_numbers():
    # str(-5) has length 2 (included), str(-100) has length 4 (excluded).
    assert add_elements([-5, -100, 7], 3) == 2


def test_add_elements_floats():
    # str(1.5) has length 3 (excluded), str(2) has length 1 (included),
    # str(3.25) has length 4 (excluded).
    assert add_elements([1.5, 2, 3.25], 3) == 2


def test_add_elements_no_element_qualifies():
    # Covers the branch where the generator yields nothing at all.
    assert add_elements([100, 200, 300], 3) == 0
