# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f035 import max_element


def test_max_element_max_is_first():
    """First element is already the max: the `e > m` branch is never taken."""
    result = max_element([5, 3, 1, 2])
    assert result == 5


def test_max_element_max_is_last():
    """A later element exceeds the running max, so the update branch executes."""
    result = max_element([1, 2, 9, 3])
    assert result == 9


def test_max_element_max_in_middle():
    """Maximum appears in the middle of the list."""
    result = max_element([1, 7, 2, 3])
    assert result == 7


def test_max_element_single_element():
    """Loop body executes exactly once with no update."""
    assert max_element([42]) == 42


def test_max_element_all_equal():
    """Equal elements never satisfy `e > m`; first element is returned."""
    assert max_element([4, 4, 4]) == 4


def test_max_element_negative_numbers():
    """Works correctly with negative values."""
    assert max_element([-10, -3, -7]) == -3


def test_max_element_mixed_signs():
    """Mix of negative and positive values."""
    assert max_element([-5, 0, 3, -1]) == 3


def test_max_element_floats():
    """Works with float values."""
    assert max_element([1.5, 2.75, 0.25]) == 2.75
