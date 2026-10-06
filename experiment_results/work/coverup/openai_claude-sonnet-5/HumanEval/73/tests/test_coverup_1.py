# file: script_73.py:1-16
# asked: {"lines": [12, 13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}
# gained: {"lines": [12, 13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}

import pytest
from script_73 import smallest_change


def test_smallest_change_non_palindrome():
    """Test array that requires changes to become palindromic."""
    assert smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4


def test_smallest_change_almost_palindrome():
    """Test array with one mismatch."""
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1


def test_smallest_change_already_palindrome():
    """Test array that is already palindromic."""
    assert smallest_change([1, 2, 3, 2, 1]) == 0


def test_smallest_change_empty_array():
    """Test empty array."""
    assert smallest_change([]) == 0


def test_smallest_change_single_element():
    """Test single element array."""
    assert smallest_change([5]) == 0


def test_smallest_change_two_elements_same():
    """Test two identical elements."""
    assert smallest_change([3, 3]) == 0


def test_smallest_change_two_elements_different():
    """Test two different elements."""
    assert smallest_change([3, 5]) == 1


def test_smallest_change_all_different():
    """Test array where all pairs are different."""
    assert smallest_change([1, 2, 3, 4]) == 2


def test_smallest_change_odd_length_mismatch():
    """Test odd length array with mismatches."""
    assert smallest_change([1, 2, 5, 2, 3]) == 1
