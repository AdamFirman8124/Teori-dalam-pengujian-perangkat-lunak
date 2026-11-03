# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f035 import max_element


def test_max_element_max_at_end():
    """Covers lines 3-7, including the True branch of `if e > m`."""
    result = max_element([1, 2, 3])
    assert result == 3


def test_max_element_max_at_start():
    """Covers lines 3-7, including the False branch of `if e > m`."""
    result = max_element([3, 2, 1])
    assert result == 3


def test_max_element_single_element():
    """Covers lines 3-7 with a single-element list (loop body runs once, False branch)."""
    result = max_element([42])
    assert result == 42


def test_max_element_with_duplicates():
    """Covers lines 3-7 with duplicate values; max appears multiple times."""
    result = max_element([5, 5, 5])
    assert result == 5


def test_max_element_negative_numbers():
    """Covers lines 3-7 with negative values, ensuring no default-zero assumption."""
    result = max_element([-10, -3, -7])
    assert result == -3


def test_max_element_matches_builtin_max():
    """Covers lines 3-7 and verifies equivalence with the built-in max."""
    data = [7, 1, 9, 4, 9, 2]
    assert max_element(data) == max(data)
