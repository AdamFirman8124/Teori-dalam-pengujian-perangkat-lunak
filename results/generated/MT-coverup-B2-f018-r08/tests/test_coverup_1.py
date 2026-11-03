# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

import pytest

from f018 import how_many_times


def test_counts_overlapping_occurrences():
    """Overlapping matches must each be counted."""
    assert how_many_times("aaaa", "aa") == 3
    assert how_many_times("aaaa", "a") == 4
    assert how_many_times("abcabc", "abc") == 2


def test_counts_single_occurrence():
    assert how_many_times("hello world", "world") == 1


def test_no_occurrence_returns_zero():
    assert how_many_times("hello", "xyz") == 0


def test_substring_longer_than_string_returns_zero():
    """The loop range is empty, so the function must return 0."""
    assert how_many_times("ab", "abc") == 0


def test_empty_substring_matches_every_position():
    """An empty substring matches at every index, including the end."""
    assert how_many_times("abc", "") == 4
    assert how_many_times("", "") == 1


def test_empty_string_nonempty_substring_returns_zero():
    assert how_many_times("", "a") == 0


def test_result_is_non_negative_int():
    result = how_many_times("banana", "ana")
    assert isinstance(result, int)
    assert result == 2
    assert result >= 0


@pytest.mark.parametrize(
    "string, substring, expected",
    [
        ("", "", 1),
        ("", "x", 0),
        ("x", "", 2),
        ("x", "x", 1),
        ("xyx", "x", 2),
        ("aaa", "aa", 2),
        ("aaaaa", "aaa", 3),
        ("mississippi", "issi", 2),
    ],
)
def test_how_many_times_parametrized(string, substring, expected):
    assert how_many_times(string, substring) == expected
