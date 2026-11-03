# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

import pytest

from pysnooper import utils


def test_truncate_returns_string_when_max_length_is_none():
    """Covers the `max_length is None` short-circuit branch (line 82)."""
    result = utils.truncate('abcdefghij', None)
    assert result == 'abcdefghij'
    # The original object should be returned untouched.
    assert result is not None


def test_truncate_returns_string_when_shorter_than_max_length():
    """Covers the `len(string) <= max_length` branch (lines 82-83)."""
    result = utils.truncate('abc', 10)
    assert result == 'abc'


def test_truncate_returns_string_when_exactly_max_length():
    """Covers the boundary `len(string) == max_length` case (lines 82-83)."""
    result = utils.truncate('abcdef', 6)
    assert result == 'abcdef'


def test_truncate_truncates_long_string_even_max_length():
    """Covers the else branch (lines 85-87) with an even max_length."""
    result = utils.truncate('abcdefghij', 6)
    # left = (6 - 3) // 2 == 1, right = 6 - 3 - 1 == 2
    assert result == 'a...ij'
    assert len(result) == 6


def test_truncate_truncates_long_string_odd_max_length():
    """Covers the else branch (lines 85-87) with an odd max_length."""
    result = utils.truncate('abcdefghij', 7)
    # left = (7 - 3) // 2 == 2, right = 7 - 3 - 2 == 2
    assert result == 'ab...ij'
    assert len(result) == 7


def test_truncate_truncates_asymmetric_split():
    """Covers the else branch (lines 85-87) where left != right."""
    result = utils.truncate('abcdefghij', 8)
    # left = (8 - 3) // 2 == 2, right = 8 - 3 - 2 == 3
    assert result == 'ab...hij'
    assert len(result) == 8
