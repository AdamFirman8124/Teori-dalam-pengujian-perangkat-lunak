# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

import pytest

from f018 import how_many_times


def test_empty_string_returns_zero():
    """Empty input string: loop body never runs, but lines 3 and 9 execute."""
    assert how_many_times("", "a") == 0


def test_single_character_counts_all_occurrences():
    """Each single character position matches, including the last one."""
    assert how_many_times("aaa", "a") == 3


def test_overlapping_occurrences_are_counted():
    """Overlapping matches must be counted: 'aaaa' contains 'aa' 3 times."""
    assert how_many_times("aaaa", "aa") == 3


def test_exact_full_match():
    """Substring equal to the whole string matches exactly once."""
    assert how_many_times("abc", "abc") == 1


def test_no_match_returns_zero():
    """Substring not present anywhere yields zero."""
    assert how_many_times("abc", "xyz") == 0


def test_substring_longer_than_string_returns_zero():
    """When substring is longer than string, range is empty and result is 0."""
    assert how_many_times("ab", "abc") == 0


def test_empty_substring_matches_every_position():
    """Empty substring trivially matches at len(string) + 1 positions."""
    assert how_many_times("abc", "") == 4


def test_multiple_matches_mixed_content():
    """Mixed content with several non-overlapping and overlapping hits."""
    assert how_many_times("abababab", "abab") == 3
    assert how_many_times("mississippi", "issi") == 2
