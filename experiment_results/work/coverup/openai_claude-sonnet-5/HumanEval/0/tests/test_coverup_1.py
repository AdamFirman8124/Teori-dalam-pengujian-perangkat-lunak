# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

from typing import List
import pytest
from script_0 import has_close_elements


def test_has_close_elements_empty_list():
    """Test with empty list - should return False without entering loop."""
    assert has_close_elements([], 0.5) == False


def test_has_close_elements_single_element():
    """Test with single element - should return False."""
    assert has_close_elements([1.0], 0.5) == False


def test_has_close_elements_two_close():
    """Test with two elements closer than threshold."""
    assert has_close_elements([1.0, 1.2], 0.3) == True


def test_has_close_elements_two_not_close():
    """Test with two elements not closer than threshold."""
    assert has_close_elements([1.0, 2.0], 0.5) == False


def test_has_close_elements_multiple_no_close():
    """Test with multiple elements, none close."""
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False


def test_has_close_elements_multiple_with_close():
    """Test with multiple elements, some close."""
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True


def test_has_close_elements_exact_threshold():
    """Test with distance exactly at threshold - should be False."""
    assert has_close_elements([1.0, 1.5], 0.5) == False


def test_has_close_elements_just_below_threshold():
    """Test with distance just below threshold - should be True."""
    assert has_close_elements([1.0, 1.49], 0.5) == True


def test_has_close_elements_negative_numbers():
    """Test with negative numbers."""
    assert has_close_elements([-1.0, -1.2], 0.3) == True
    assert has_close_elements([-1.0, -2.0], 0.5) == False


def test_has_close_elements_mixed_signs():
    """Test with mixed positive and negative numbers."""
    assert has_close_elements([-0.1, 0.1], 0.3) == True
    assert has_close_elements([-1.0, 1.0], 1.5) == False
