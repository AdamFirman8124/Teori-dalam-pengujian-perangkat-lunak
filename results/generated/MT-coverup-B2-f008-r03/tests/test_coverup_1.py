# file: project/f008/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

import pytest

from f008 import sum_product


def test_empty_list():
    """Covers lines 6-7 and 12: initializers and return with loop never entered."""
    assert sum_product([]) == (0, 1)


def test_single_element():
    """Covers lines 9-11: loop body executes exactly once."""
    assert sum_product([5]) == (5, 5)


def test_multiple_elements():
    """Covers lines 9-11 with multiple iterations."""
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_negative_numbers():
    """Loop body with negative values."""
    assert sum_product([-1, 2, -3]) == (-2, 6)


def test_with_zero():
    """Zero forces product to 0 while sum still accumulates."""
    assert sum_product([0, 7, 3]) == (10, 0)
