# file: script_40.py:1-23
# asked: {"lines": [18, 19, 20, 21, 22, 23], "branches": [[18, 19], [18, 23], [19, 18], [19, 20], [20, 19], [20, 21], [21, 20], [21, 22]]}
# gained: {"lines": [18, 19, 20, 21, 22, 23], "branches": [[18, 19], [18, 23], [19, 18], [19, 20], [20, 19], [20, 21], [21, 20], [21, 22]]}

import pytest
from script_40 import triples_sum_to_zero


def test_triples_sum_to_zero_with_valid_triple():
    """Test that function returns True when three elements sum to zero."""
    result = triples_sum_to_zero([1, -1, 0])
    assert result is True


def test_triples_sum_to_zero_with_no_valid_triple():
    """Test that function returns False when no three elements sum to zero."""
    result = triples_sum_to_zero([1, 2, 3])
    assert result is False


def test_triples_sum_to_zero_with_exactly_three_elements_no_sum():
    """Test with exactly 3 elements that don't sum to zero."""
    result = triples_sum_to_zero([5, 10, 15])
    assert result is False


def test_triples_sum_to_zero_with_exactly_three_elements_with_sum():
    """Test with exactly 3 elements that sum to zero."""
    result = triples_sum_to_zero([2, -1, -1])
    assert result is True
