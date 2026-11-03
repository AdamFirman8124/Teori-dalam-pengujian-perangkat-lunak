# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f122 import add_elements


def test_add_elements_mixed_filters_large_elements():
    """Exercises both branches of the len(str(elem)) <= 2 condition on line 3."""
    arr = [1, -2, 100, 23, 456, 78]
    # str(-2) == '-2' has length 2 and is included; 100 and 456 have 3-digit
    # string reprs and are excluded.
    assert add_elements(arr, 6) == 1 + (-2) + 23 + 78


def test_add_elements_empty_array():
    """Line 3 must execute (and sum to 0) even for an empty iterable."""
    assert add_elements([], 3) == 0


def test_add_elements_k_exceeds_length():
    """arr[:k] slicing must not fail when k is larger than len(arr)."""
    assert add_elements([5, 99], 10) == 5 + 99


def test_add_elements_k_limits_slice():
    """Only the first k elements are considered, even if later ones qualify."""
    assert add_elements([100, 7, 999], 2) == 7


def test_add_elements_all_filtered_out():
    """Sum is 0 when every element fails the two-digit condition."""
    assert add_elements([-100, 1000], 2) == 0


def test_add_elements_two_digit_boundaries():
    """len(str(elem)) <= 2 means -9..99 pass; -10 and 100 fail.

    Note: str(-10) == '-10' has length 3, so two-digit *negative*
    numbers are excluded by this implementation, not included.
    """
    arr = [99, -9, -10, 100, -100, 0]
    assert add_elements(arr, 6) == 99 + (-9) + 0
