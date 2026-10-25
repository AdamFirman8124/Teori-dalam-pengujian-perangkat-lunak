# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

from f018 import how_many_times


def test_how_many_times_counts_overlapping_matches_and_nonmatches():
    assert how_many_times("ababa", "aba") == 2


def test_how_many_times_with_substring_longer_than_string():
    assert how_many_times("ab", "abcd") == 0
