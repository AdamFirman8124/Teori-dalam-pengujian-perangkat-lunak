# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

import pytest

from f018 import how_many_times


def test_empty_string_nonempty_substring():
    """Loop body never runs (range is empty); covers lines 3, 5, 9."""
    assert how_many_times("", "a") == 0


def test_single_character_multiple_occurrences():
    """Covers loop body executing and the branch evaluating True each time."""
    assert how_many_times("aaa", "a") == 3


def test_overlapping_occurrences_counted():
    """Overlaps must be counted: 'aaaa' contains 'aa' at i=0,1,2."""
    assert how_many_times("aaaa", "aa") == 3


def test_substring_equals_whole_string():
    """Single iteration where the slice matches exactly."""
    assert how_many_times("aaaa", "aaaa") == 1


def test_substring_longer_than_string():
    """range(len - len + 1) is empty; loop body never runs."""
    assert how_many_times("abc", "abcd") == 0


def test_no_match_branch_false():
    """Covers the branch evaluating False (times stays 0)."""
    assert how_many_times("abc", "xyz") == 0


def test_mixed_matches_and_misses():
    """Both branch outcomes exercised in one loop."""
    assert how_many_times("ababab", "ab") == 3
    assert how_many_times("ababab", "aba") == 2


def test_empty_substring_matches_every_position():
    """Empty substring matches at every index, including len(string)."""
    assert how_many_times("abc", "") == 4


def test_both_empty():
    """range(1) runs once; empty slice equals empty substring."""
    assert how_many_times("", "") == 1


@pytest.mark.parametrize(
    "string,substring,expected",
    [
        ("", "a", 0),
        ("aaa", "a", 3),
        ("aaaa", "aa", 3),
        ("aaaa", "aaaa", 1),
        ("abc", "abcd", 0),
        ("abc", "xyz", 0),
        ("abc", "", 4),
        ("", "", 1),
        ("abababab", "abab", 3),
    ],
)
def test_how_many_times_parametrized(string, substring, expected):
    assert how_many_times(string, substring) == expected
