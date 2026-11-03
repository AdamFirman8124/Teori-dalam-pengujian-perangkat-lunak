# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f098 import count_upper


def test_count_upper_empty_string():
    """Empty input: covers line 3, line 4 (loop condition false immediately) and line 7."""
    assert count_upper("") == 0


def test_count_upper_all_uppercase_vowels():
    """Covers lines 3-7, including the true branch of line 5 and the increment on line 6."""
    # Even indices 0, 2, 4 hold 'A', 'I', 'U' -> all three counted.
    assert count_upper("AEIOU") == 3


def test_count_upper_no_vowels_at_even_indices():
    """Covers the false branch of line 5 (condition never true)."""
    assert count_upper("BCDFG") == 0


def test_count_upper_lowercase_vowels_ignored():
    """Lowercase vowels at even indices must not be counted (false branch of line 5)."""
    assert count_upper("aeiou") == 0


def test_count_upper_mixed_branches():
    """Exercises both branches of line 5 within a single call."""
    # Even indices: 0='A' (counted), 2='E' (counted), 4='D' (not counted).
    assert count_upper("AbEcD") == 2


def test_count_upper_odd_indices_ignored():
    """Vowels located at odd indices must be skipped by the range(0, len(s), 2) loop."""
    # 'A' at index 1 and 'E' at index 3 are never visited.
    assert count_upper("xAyE") == 0


def test_count_upper_single_char():
    """Single-character strings cover both loop-exit paths."""
    assert count_upper("A") == 1
    assert count_upper("b") == 0
