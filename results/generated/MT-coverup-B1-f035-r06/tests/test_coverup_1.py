# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f035 import max_element


def test_max_element_max_in_middle_or_end():
    """Covers lines 3-7 including the branch where e > m is True."""
    result = max_element([1, 5, 3, 2])
    assert result == 5


def test_max_element_max_is_first_element():
    """Covers the branch where e > m is never True (max is l[0])."""
    result = max_element([9, 1, 2, 3])
    assert result == 9


def test_max_element_single_element():
    """Covers loop with a single element (loop body executes once, branch False)."""
    result = max_element([42])
    assert result == 42


def test_max_element_with_duplicates():
    """Duplicates never trigger the e > m branch for equal values."""
    result = max_element([7, 7, 7])
    assert result == 7


def test_max_element_negative_numbers():
    result = max_element([-10, -3, -50])
    assert result == -3


def test_max_element_empty_list_raises():
    """l[0] on an empty list raises IndexError; no state to pollute."""
    with pytest.raises(IndexError):
        max_element([])
