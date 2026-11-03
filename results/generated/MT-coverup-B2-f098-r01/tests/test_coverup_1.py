# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f098 import count_upper


def test_count_upper_empty_string():
    """Covers lines 3, 4 (loop never entered) and 7."""
    assert count_upper("") == 0


def test_count_upper_all_uppercase_vowels_at_even_indices():
    """Covers lines 3-7 including the true branch of line 5 and line 6."""
    # Even indices 0, 2, 4 hold 'A', 'I', 'U' -> all counted
    assert count_upper("AEIOU") == 3


def test_count_upper_no_vowels_at_even_indices():
    """Covers the false branch of line 5 (consonants at even indices)."""
    assert count_upper("BCDFG") == 0


def test_count_upper_lowercase_vowels_not_counted():
    """Lowercase vowels at even indices must not count (false branch)."""
    assert count_upper("aeiou") == 0


def test_count_upper_mixed_string():
    """Mix of true and false branches across even indices."""
    # Even indices 0, 2, 4 -> 'A' (count), 'C' (no), 'E' (count)
    assert count_upper("AbCdE") == 2


def test_count_upper_odd_length_string():
    """Odd-length string: last even index is len(s) - 1."""
    # Even indices 0, 2 -> 'E' (count), 'b' (no)
    assert count_upper("Exb") == 1


def test_count_upper_vowels_only_at_odd_indices():
    """Uppercase vowels at odd indices are ignored (false branch)."""
    # Even indices 0, 2 -> 'b', 'd' (no); odd indices 1, 3 hold 'A', 'E'
    assert count_upper("bAdE") == 0


def test_count_upper_single_char():
    """Single-character strings exercise both branches of line 5."""
    assert count_upper("A") == 1
    assert count_upper("b") == 0
