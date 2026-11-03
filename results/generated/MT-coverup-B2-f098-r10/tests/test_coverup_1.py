# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f098 import count_upper


def test_count_upper_empty_string():
    """Empty string: loop body never runs, returns 0."""
    assert count_upper("") == 0


def test_count_upper_single_vowel_at_even_index():
    """Single uppercase vowel at index 0 is counted."""
    assert count_upper("A") == 1


def test_count_upper_single_consonant_at_even_index():
    """Single consonant at index 0 is not counted (false branch)."""
    assert count_upper("B") == 0


def test_count_upper_lowercase_vowels_not_counted():
    """Lowercase vowels at even indices are not counted (false branch)."""
    assert count_upper("aeiou") == 0


def test_count_upper_vowels_at_odd_indices_not_counted():
    """Uppercase vowels at odd indices are skipped by the step-2 loop."""
    assert count_upper("aAaAaA") == 0


def test_count_upper_all_vowels_at_even_indices():
    """'AEIOU' has vowels at indices 0, 2, 4 -> count 3."""
    assert count_upper("AEIOU") == 3


def test_count_upper_mixed_string():
    """Mixed content: only uppercase vowels at even indices count."""
    # indices: 0='A'(count), 1='b', 2='E'(count), 3='x', 4='I'(count),
    #          5='u', 6='O'(count), 7='Y', 8='U'(count)
    assert count_upper("AbExIuOYU") == 5


def test_count_upper_odd_length_string():
    """Odd-length strings: last even index is len(s)-1."""
    assert count_upper("aXbEc") == 0  # even indices 0='a', 2='b', 4='c'
    assert count_upper("UXbEc") == 1  # even indices 0='U', 2='b', 4='c'
    assert count_upper("AbEcI") == 3  # even indices 0='A', 2='E', 4='I'


def test_count_upper_no_vowels():
    """String with no vowels at all returns 0."""
    assert count_upper("BCDFG") == 0
