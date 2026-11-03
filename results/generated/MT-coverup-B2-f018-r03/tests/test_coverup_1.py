# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

"""Tests for f018.how_many_times.

The function under test is pure (no I/O, no module-level mutable state,
no external dependencies), so no monkeypatching or fixture-based cleanup
is required; each test leaves no state behind.
"""

from f018 import how_many_times


def test_empty_string_loop_never_runs():
    # Covers line 3 (times = 0) and line 9 (return) with the loop on
    # line 5 never entered (range(0 - 1 + 1) == range(0)).
    assert how_many_times("", "a") == 0


def test_substring_longer_than_string_loop_never_runs():
    # Another way to skip the loop body: range(2 - 3 + 1) == range(0).
    assert how_many_times("ab", "abc") == 0


def test_single_character_multiple_matches():
    # Covers lines 5-7 with the if-branch taken on every iteration.
    assert how_many_times("aaa", "a") == 3


def test_overlapping_occurrences_are_counted():
    # 'aa' occurs at indices 0, 1 and 2 in 'aaaa' (overlapping case).
    assert how_many_times("aaaa", "aa") == 3


def test_no_match_if_branch_never_taken():
    # Covers lines 5-7 with the if-branch never taken (line 7 skipped).
    assert how_many_times("abc", "xyz") == 0


def test_mixed_matches_and_misses():
    # Exercises both outcomes of the if on line 6 within one loop:
    # 'ab' matches at 0 and 2, misses at 1 and 3.
    assert how_many_times("abab", "ab") == 2


def test_substring_equals_whole_string():
    # Exactly one iteration, one match.
    assert how_many_times("abc", "abc") == 1


def test_result_is_always_an_int():
    # Postcondition: the return value is a non-negative int.
    result = how_many_times("hello", "l")
    assert isinstance(result, int)
    assert result >= 0
    assert result == 2
