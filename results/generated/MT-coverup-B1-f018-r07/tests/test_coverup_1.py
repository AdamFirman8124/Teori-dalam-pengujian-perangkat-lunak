# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

import pytest

from f018 import how_many_times


def test_no_occurrences():
    assert how_many_times("hello", "xyz") == 0


def test_single_occurrence():
    assert how_many_times("hello", "ell") == 1


def test_overlapping_occurrences():
    # "aaa" contains "aa" at indices 0 and 1 (overlapping matches count)
    assert how_many_times("aaa", "aa") == 2


def test_multiple_occurrences():
    assert how_many_times("aaaa", "aa") == 3


def test_substring_longer_than_string():
    # loop range is empty; returns 0
    assert how_many_times("ab", "abc") == 0


def test_empty_string():
    assert how_many_times("", "a") == 0


def test_empty_substring():
    # empty substring matches at every position len(string)+1 times
    assert how_many_times("abc", "") == 4


def test_both_empty():
    assert how_many_times("", "") == 1


def test_exact_match_whole_string():
    assert how_many_times("abc", "abc") == 1
