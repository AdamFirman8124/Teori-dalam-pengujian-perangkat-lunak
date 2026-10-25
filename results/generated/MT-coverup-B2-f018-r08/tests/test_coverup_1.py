# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

from f018 import how_many_times


def test_how_many_times_counts_overlapping_matches():
    assert how_many_times("aaaa", "aa") == 3


def test_how_many_times_handles_no_matches_and_substring_longer_than_string():
    assert how_many_times("abc", "z") == 0
    assert how_many_times("abc", "abcd") == 0


def test_how_many_times_counts_empty_substrings():
    assert how_many_times("abc", "") == 4
