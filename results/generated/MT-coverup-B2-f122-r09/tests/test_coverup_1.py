# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f122 import add_elements


def test_add_elements_mixed_sizes():
    """Covers the generator expression: elements of len(str) <= 2 are summed."""
    arr = [1, -2, 23, 100, 5]
    # str(1)='1', str(-2)='-2', str(23)='23', str(5)='5' all have length <= 2;
    # str(100)='100' has length 3 and is excluded.
    assert add_elements(arr, 5) == 1 + (-2) + 23 + 5


def test_add_elements_excludes_large_elements():
    """All elements are three digits, so the sum is empty -> 0."""
    arr = [111, 23, 4567]
    assert add_elements(arr, 3) == 23


def test_add_elements_k_limits_slice():
    """k truncates arr before filtering, so the 999 at the end is ignored."""
    arr = [1, 2, 999]
    assert add_elements(arr, 2) == 3


def test_add_elements_empty_arr():
    """Empty input yields sum of empty generator -> 0."""
    assert add_elements([], 5) == 0


def test_add_elements_k_zero():
    """k=0 slices to an empty list -> sum is 0."""
    assert add_elements([1, 2, 3], 0) == 0
