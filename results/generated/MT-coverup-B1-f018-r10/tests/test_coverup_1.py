# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

import pytest

from f018 import how_many_times


def test_counts_non_overlapping_occurrences():
    assert how_many_times("abcabc", "abc") == 2


def test_counts_overlapping_occurrences():
    assert how_many_times("aaaa", "aa") == 3


def test_returns_zero_when_substring_absent():
    assert how_many_times("hello", "z") == 0


def test_returns_zero_when_substring_longer_than_string():
    assert how_many_times("ab", "abc") == 0


def test_empty_string_returns_zero():
    assert how_many_times("", "a") == 0


def test_empty_substring_matches_every_position():
    # range(len(string) + 1) positions, each slice "" == "" -> len(string) + 1
    assert how_many_times("abc", "") == 4


def test_both_empty():
    assert how_many_times("", "") == 1


def test_single_character_string_and_substring():
    assert how_many_times("a", "a") == 1


def test_whole_string_is_substring():
    assert how_many_times("abc", "abc") == 1


@pytest.mark.parametrize(
    "string, substring, expected",
    [
        ("abcabcabc", "abc", 3),
        ("abababab", "aba", 3),
        ("mississippi", "issi", 2),
        ("xyz", "y", 1),
    ],
)
def test_parametrized_counts(string, substring, expected):
    assert how_many_times(string, substring) == expected
