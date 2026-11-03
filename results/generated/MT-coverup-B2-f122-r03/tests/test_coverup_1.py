# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f122 import add_elements


def test_add_elements_all_small():
    """All elements within k have at most 2 digits; all are summed."""
    assert add_elements([1, -2, 23, 0], 4) == 22


def test_add_elements_filters_large():
    """Elements with more than 2 digits (in string form) are excluded,
    exercising the False branch of the filter condition."""
    # 111 and -999 have 3-digit string representations -> excluded
    assert add_elements([1, 111, -999, 23], 4) == 24


def test_add_elements_k_limits_slice():
    """Only the first k elements are considered, exercising the slice branch."""
    # 100 is beyond k=2, so it must not be excluded-summed
    assert add_elements([10, 20, 100], 2) == 30


def test_add_elements_empty():
    """Empty input yields 0 while still executing the return line."""
    assert add_elements([], 3) == 0


def test_add_elements_k_zero():
    """k=0 slices to an empty list, yielding 0."""
    assert add_elements([1, 2, 3], 0) == 0


def test_add_elements_k_exceeds_length():
    """k larger than len(arr) is safe due to slicing."""
    assert add_elements([5, 6], 10) == 11


def test_add_elements_negative_k():
    """Negative k slices from the end; verify documented slice behavior."""
    # arr[:-1] == [1, 2], both small -> sum 3
    assert add_elements([1, 2, 999], -1) == 3
