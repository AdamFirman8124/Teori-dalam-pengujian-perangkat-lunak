# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f035 import max_element


def test_max_element_last_is_max():
    """Covers lines 3-7 including the True branch of the comparison (line 6)."""
    result = max_element([1, 5, 3])
    assert result == 5


def test_max_element_first_is_max():
    """Covers the False branch of the comparison (line 5) when no element exceeds m."""
    result = max_element([9, 4, 2])
    assert result == 9


def test_max_element_single_element():
    """Covers loop with a single iteration (False branch, no update)."""
    result = max_element([42])
    assert result == 42


def test_max_element_all_equal():
    """All elements equal: comparison always False, first element returned."""
    result = max_element([7, 7, 7])
    assert result == 7


def test_max_element_negative_numbers():
    """Works correctly with negative values, exercising both branches."""
    result = max_element([-10, -3, -7])
    assert result == -3
