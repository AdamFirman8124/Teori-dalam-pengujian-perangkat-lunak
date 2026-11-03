# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

import pytest

from f163 import generate_integers


def test_generate_integers_basic_range():
    """Covers lines 3-6 with a typical ascending range."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]


def test_generate_integers_reversed_arguments():
    """min/max handle swapped arguments; covers lines 3-4 branches."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]


def test_generate_integers_clamped_lower_bound():
    """Values below 2 are clamped up to 2 (line 3 max branch)."""
    assert generate_integers(0, 3) == [2]


def test_generate_integers_clamped_upper_bound():
    """Values above 8 are clamped down to 8 (line 4 min branch)."""
    assert generate_integers(10, 12) == []


def test_generate_integers_equal_arguments():
    """When a == b, lower == upper; range yields at most one value."""
    assert generate_integers(4, 4) == [4]


def test_generate_integers_single_even_value():
    """A single even value in range is returned."""
    assert generate_integers(7, 7) == []


def test_generate_integers_filters_odd_numbers():
    """The comprehension (line 6) filters out odd numbers."""
    result = generate_integers(3, 6)
    assert result == [4, 6]
    assert all(i % 2 == 0 for i in result)
