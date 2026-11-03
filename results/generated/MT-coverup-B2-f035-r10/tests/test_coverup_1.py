# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f035 import max_element


def test_max_element_first_is_max():
    """Covers lines 3-5 (False branch of `if e > m`) and line 7:
    the first element is already the maximum, so line 6 never runs."""
    assert max_element([3, 2, 1]) == 3


def test_max_element_later_is_max():
    """Covers lines 3-7 including the True branch of `if e > m` (line 6):
    a later element replaces the running maximum."""
    assert max_element([1, 5, 3]) == 5


def test_max_element_single_element():
    """Covers the loop body executing exactly once with the False branch."""
    assert max_element([7]) == 7


def test_max_element_with_duplicates():
    """Duplicates exercise both branches of the comparison across iterations."""
    assert max_element([2, 2, 3, 3, 1]) == 3


def test_max_element_negative_numbers():
    """Works correctly with all-negative values (max is the least negative)."""
    assert max_element([-5, -1, -3]) == -1
