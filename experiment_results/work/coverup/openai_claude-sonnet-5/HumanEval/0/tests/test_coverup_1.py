# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

from script_0 import has_close_elements
import pytest


def test_has_close_elements_two_elements_close():
    """Test with two close elements - executes lines 12-17"""
    result = has_close_elements([1.0, 1.2], 0.5)
    assert result == True


def test_has_close_elements_two_elements_far():
    """Test with two far elements - executes lines 12-19"""
    result = has_close_elements([1.0, 5.0], 0.5)
    assert result == False


def test_has_close_elements_multiple_with_close():
    """Test with multiple elements where some are close"""
    result = has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    assert result == True


def test_has_close_elements_multiple_no_close():
    """Test with multiple elements, none close - executes all lines including 19"""
    result = has_close_elements([1.0, 2.0, 3.0], 0.5)
    assert result == False


def test_has_close_elements_empty_list():
    """Test with empty list"""
    result = has_close_elements([], 0.5)
    assert result == False


def test_has_close_elements_single_element():
    """Test with single element"""
    result = has_close_elements([1.0], 0.5)
    assert result == False
