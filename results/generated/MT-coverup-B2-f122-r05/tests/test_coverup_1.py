# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f122 import add_elements


def test_add_elements_basic():
    """Elements whose string form has at most 2 chars are summed; longer ones skipped."""
    # arr[:4] = [1, -2, 12, 123]; str lengths: 1, 2, 2, 3 -> only first three qualify.
    assert add_elements([1, -2, 12, 123, 5], 4) == 1 + (-2) + 12


def test_add_elements_k_exceeds_length():
    """k larger than len(arr): slicing handles it gracefully, all elements considered."""
    assert add_elements([7, 8], 10) == 15


def test_add_elements_no_qualifying_elements():
    """No element qualifies -> sum over an empty generator is 0."""
    assert add_elements([100, 200, -300], 3) == 0


def test_add_elements_k_zero():
    """k == 0 -> empty slice -> sum is 0."""
    assert add_elements([1, 2, 3], 0) == 0


def test_add_elements_negative_numbers():
    """str(-5) == '-5' (len 2) qualifies; str(-10) == '-10' (len 3) does not."""
    assert add_elements([-5, -10, 99], 3) == -5 + 99


def test_add_elements_k_equals_length():
    """k exactly equal to len(arr): every element is considered."""
    assert add_elements([11, 222, 3], 3) == 11 + 3
