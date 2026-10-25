# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

from f018 import how_many_times


def test_overlapping_occurrences():
    assert how_many_times("aaa", "aa") == 2


def test_mixed_match_and_mismatch():
    # i=0 True, i=1 False, i=2 True, i=3 False, i=4 True
    assert how_many_times("abababa", "aba") == 3


def test_no_occurrence():
    assert how_many_times("abc", "d") == 0


def test_substring_longer_than_string_skips_loop():
    assert how_many_times("hi", "hello") == 0


def test_exact_match():
    assert how_many_times("abc", "abc") == 1
