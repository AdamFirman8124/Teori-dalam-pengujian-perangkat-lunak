# file: script_73.py:1-16
# asked: {"lines": [12, 13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}
# gained: {"lines": [12, 13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}

import pytest
from script_73 import smallest_change


def test_smallest_change_empty_array():
    """Test with empty array - no changes needed."""
    assert smallest_change([]) == 0


def test_smallest_change_single_element():
    """Test with single element - already palindromic."""
    assert smallest_change([5]) == 0


def test_smallest_change_two_elements_same():
    """Test with two identical elements - already palindromic."""
    assert smallest_change([3, 3]) == 0


def test_smallest_change_two_elements_different():
    """Test with two different elements - needs one change."""
    assert smallest_change([1, 2]) == 1


def test_smallest_change_palindrome_odd_length():
    """Test with odd-length palindrome - no changes needed."""
    assert smallest_change([1, 2, 3, 2, 1]) == 0


def test_smallest_change_palindrome_even_length():
    """Test with even-length palindrome - no changes needed."""
    assert smallest_change([1, 2, 2, 1]) == 0


def test_smallest_change_non_palindrome_example_1():
    """Test example from docstring."""
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4


def test_smallest_change_non_palindrome_example_2():
    """Test example from docstring."""
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1


def test_smallest_change_all_different():
    """Test with completely non-palindromic array."""
    assert smallest_change([1, 2, 3, 4]) == 2


def test_smallest_change_partial_palindrome():
    """Test with partially palindromic array."""
    assert smallest_change([5, 3, 7, 3, 5]) == 0
    assert smallest_change([5, 3, 7, 2, 5]) == 1
