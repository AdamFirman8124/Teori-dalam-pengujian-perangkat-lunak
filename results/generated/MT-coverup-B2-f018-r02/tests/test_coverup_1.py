# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

import pytest

from f018 import how_many_times


def test_empty_string_nonempty_substring():
    # Loop range is empty (0 - 1 + 1 = 0); returns 0 without entering loop body.
    assert how_many_times("", "a") == 0


def test_single_character_multiple_occurrences():
    # Exercises loop body with both matching and non-matching slices.
    assert how_many_times("aaa", "a") == 3
    assert how_many_times("abc", "a") == 1
    assert how_many_times("abc", "z") == 0


def test_overlapping_occurrences():
    # Overlaps must be counted: "aaaa" contains "aa" at indices 0, 1, 2.
    assert how_many_times("aaaa", "aa") == 3


def test_substring_equals_string():
    # Single iteration where the whole string matches.
    assert how_many_times("aaaa", "aaaa") == 1


def test_substring_longer_than_string():
    # Loop range is empty (3 - 4 + 1 = 0); returns 0.
    assert how_many_times("abc", "abcd") == 0


def test_empty_substring_matches_every_position():
    # len("abc") - 0 + 1 = 4 iterations, each empty slice equals "".
    assert how_many_times("abc", "") == 4


def test_both_empty():
    # One iteration (0 - 0 + 1 = 1); empty slice equals empty substring.
    assert how_many_times("", "") == 1


def test_mixed_occurrences():
    # "abcabc" contains "abc" twice, non-overlapping.
    assert how_many_times("abcabc", "abc") == 2
    # Overlapping pattern "aba" in "ababa" occurs at indices 0 and 2.
    assert how_many_times("ababa", "aba") == 2


@pytest.mark.parametrize(
    "string,substring,expected",
    [
        ("", "a", 0),
        ("", "", 1),
        ("a", "a", 1),
        ("aaa", "aa", 2),
        ("xyxyxyx", "xyx", 3),
        ("hello", "world", 0),
    ],
)
def test_parametrized_counts(string, substring, expected):
    assert how_many_times(string, substring) == expected
