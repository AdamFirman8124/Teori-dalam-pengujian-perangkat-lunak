# file: script_131.py:1-19
# asked: {"lines": [9, 10, 11, 12, 13, 14, 15, 16, 17, 19], "branches": [[11, 12], [11, 16], [13, 11], [13, 14], [16, 17], [16, 19]]}
# gained: {"lines": [9, 10, 11, 12, 13, 14, 15, 16, 17, 19], "branches": [[11, 12], [11, 16], [13, 11], [13, 14], [16, 17], [16, 19]]}

import pytest
from script_131 import digits


def test_digits_single_odd():
    """Test with a single odd digit."""
    assert digits(1) == 1
    assert digits(3) == 3
    assert digits(5) == 5
    assert digits(7) == 7
    assert digits(9) == 9


def test_digits_single_even():
    """Test with a single even digit."""
    assert digits(2) == 0
    assert digits(4) == 0
    assert digits(6) == 0
    assert digits(8) == 0


def test_digits_multiple_odd():
    """Test with multiple odd digits."""
    assert digits(13) == 3
    assert digits(135) == 15
    assert digits(235) == 15
    assert digits(1357) == 105
    assert digits(9753) == 945


def test_digits_multiple_even():
    """Test with multiple even digits."""
    assert digits(24) == 0
    assert digits(2468) == 0


def test_digits_mixed_odd_and_even():
    """Test with mixed odd and even digits."""
    assert digits(12) == 1
    assert digits(123) == 3
    assert digits(1234) == 3
    assert digits(2345) == 15
    assert digits(102030) == 3


def test_digits_all_zeros():
    """Test with zeros."""
    assert digits(0) == 0
    assert digits(100) == 1
    assert digits(1000) == 1
