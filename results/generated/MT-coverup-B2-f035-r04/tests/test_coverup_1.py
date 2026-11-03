# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f035 import max_element


def test_max_element_max_at_end():
    """Covers lines 3-7 including the True branch of `if e > m` (line 6)."""
    result = max_element([1, 5, 3, 9, 2])
    assert result == 9


def test_max_element_max_at_start():
    """Covers the False branch of `if e > m` (line 5) when max is the first element."""
    result = max_element([10, 3, 7, 1])
    assert result == 10


def test_max_element_single_element():
    """Covers loop with a single iteration (both branches of the comparison)."""
    assert max_element([42]) == 42


def test_max_element_with_duplicates():
    """Duplicates exercise the `e > m` False branch (e == m)."""
    assert max_element([4, 4, 4]) == 4


def test_max_element_negative_numbers():
    """Works correctly with all-negative values."""
    assert max_element([-5, -1, -9]) == -1
