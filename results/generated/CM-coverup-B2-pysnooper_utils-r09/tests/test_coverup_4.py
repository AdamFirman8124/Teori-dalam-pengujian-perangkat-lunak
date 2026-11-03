# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

import pytest

from pysnooper.utils import truncate


def test_truncate_with_none_max_length_returns_string_unchanged():
    """Covers line 82 (condition, `max_length is None` branch) and line 83."""
    result = truncate('hello world', None)
    assert result == 'hello world'


def test_truncate_short_string_returns_string_unchanged():
    """Covers line 82 (condition, `len(string) <= max_length` branch) and line 83."""
    # strictly shorter than max_length
    assert truncate('abc', 10) == 'abc'
    # exactly equal to max_length (boundary of the <= comparison)
    assert truncate('abc', 3) == 'abc'


def test_truncate_long_string_odd_max_length():
    """Covers lines 85, 86, 87 (else branch) with an odd max_length."""
    result = truncate('abcdefghij', 5)
    # left = (5 - 3) // 2 == 1, right = 5 - 3 - 1 == 1
    assert result == 'a...j'
    assert len(result) == 5


def test_truncate_long_string_even_max_length():
    """Covers lines 85, 86, 87 (else branch) with an even max_length,
    exercising the asymmetric left/right split."""
    result = truncate('abcdefghij', 6)
    # left = (6 - 3) // 2 == 1, right = 6 - 3 - 1 == 2
    assert result == 'a...ij'
    assert len(result) == 6


def test_truncate_long_string_larger_odd_max_length():
    """Covers lines 85, 86, 87 again with a different split."""
    result = truncate('abcdefghij', 7)
    # left = (7 - 3) // 2 == 2, right = 7 - 3 - 2 == 2
    assert result == 'ab...ij'
    assert len(result) == 7
