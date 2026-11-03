# file: project/f098/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

"""Tests for f098.count_upper.

Covers all previously missing lines (3-7):
- line 3 (count = 0): every call
- line 4 (for loop): every call; loop body entered via non-empty strings
- line 5 (if): both branches (vowel at even index / non-vowel at even index)
- line 6 (count += 1): strings with uppercase vowels at even indices
- line 7 (return): every call

The function under test is pure (no I/O, no globals, no mutable state),
so no monkeypatching or fixture teardown is required; each test is fully
self-contained and leaves no state behind.
"""

from f098 import count_upper


def test_count_upper_empty_string():
    """Empty string: loop body never runs, count stays 0 (lines 3, 4, 7)."""
    assert count_upper("") == 0


def test_count_upper_all_vowels_at_even_indices():
    """Every even index holds an uppercase vowel -> all counted (lines 3-7)."""
    # indices 0, 2, 4 hold 'A', 'I', 'U'
    assert count_upper("AEIOU") == 3


def test_count_upper_no_vowels_at_even_indices():
    """Even indices hold consonants -> if-branch False, count stays 0."""
    assert count_upper("BCDFG") == 0


def test_count_upper_single_char_consonant():
    """Single iteration of the loop with a non-vowel."""
    assert count_upper("B") == 0


def test_count_upper_single_char_vowel():
    """Single iteration of the loop with an uppercase vowel."""
    assert count_upper("A") == 1


def test_count_upper_mixed_case_and_positions():
    """Only uppercase vowels at even indices are counted."""
    # even indices: 0='a' (lowercase), 2='C', 4='E' -> only 'E' counts
    assert count_upper("aBCdEf") == 1
    # even indices: 0='a', 2='c', 4='e', 6='g' -> none are uppercase vowels
    assert count_upper("abcdefg") == 0
    # even indices: 0='d', 2='B' -> none are uppercase vowels
    assert count_upper("dBBE") == 0
    # odd-index uppercase vowels must not be counted
    assert count_upper("aEaE") == 0
