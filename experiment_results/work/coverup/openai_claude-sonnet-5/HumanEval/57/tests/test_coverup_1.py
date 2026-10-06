# file: script_57.py:1-12
# asked: {"lines": [10, 11, 12], "branches": [[10, 11], [10, 12]]}
# gained: {"lines": [10, 11, 12], "branches": [[10, 11], [10, 12]]}

import pytest
from script_57 import monotonic


def test_monotonic_increasing():
    """Test monotonic with strictly increasing list."""
    assert monotonic([1, 2, 4, 20]) is True


def test_monotonic_decreasing():
    """Test monotonic with strictly decreasing list."""
    assert monotonic([4, 1, 0, -10]) is True


def test_monotonic_non_monotonic():
    """Test monotonic with non-monotonic list."""
    assert monotonic([1, 20, 4, 10]) is False


def test_monotonic_empty_list():
    """Test monotonic with empty list."""
    assert monotonic([]) is True


def test_monotonic_single_element():
    """Test monotonic with single element."""
    assert monotonic([5]) is True


def test_monotonic_two_elements_increasing():
    """Test monotonic with two increasing elements."""
    assert monotonic([1, 2]) is True


def test_monotonic_two_elements_decreasing():
    """Test monotonic with two decreasing elements."""
    assert monotonic([2, 1]) is True


def test_monotonic_all_same():
    """Test monotonic with all identical elements."""
    assert monotonic([5, 5, 5, 5]) is True


def test_monotonic_negative_numbers_increasing():
    """Test monotonic with negative numbers increasing."""
    assert monotonic([-10, -5, -1, 0]) is True


def test_monotonic_negative_numbers_decreasing():
    """Test monotonic with negative numbers decreasing."""
    assert monotonic([0, -1, -5, -10]) is True
