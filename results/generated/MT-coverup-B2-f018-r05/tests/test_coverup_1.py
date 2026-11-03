# file: project/f018/__init__.py:1-9
# asked: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}
# gained: {"lines": [3, 5, 6, 7, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7]]}

"""Tests for f018.how_many_times — full line and branch coverage."""

from f018 import how_many_times


def test_matches_found_executes_loop_and_increment():
    """Lines 3, 5, 6 (True branch), 7 and 9: overlapping matches counted."""
    # 'aa' occurs at indices 0, 1, 2 in 'aaaa' (overlaps allowed).
    assert how_many_times('aaaa', 'aa') == 3
    # Single occurrence exercises exactly one increment.
    assert how_many_times('abcde', 'bcd') == 1


def test_no_match_covers_false_branch_of_comparison():
    """Line 6 (False branch): loop runs but comparison never succeeds."""
    assert how_many_times('abcdef', 'xyz') == 0


def test_substring_longer_than_string_skips_loop_body():
    """Line 5 with an empty range: loop body (lines 6-7) never executes."""
    assert how_many_times('ab', 'abc') == 0
    assert how_many_times('', 'a') == 0


def test_empty_substring_counts_every_position():
    """Empty substring matches at every index, including len(string)."""
    assert how_many_times('abc', '') == 4


def test_both_arguments_empty():
    """Edge case: empty string and empty substring yield one match."""
    assert how_many_times('', '') == 1


def test_result_is_always_nonnegative_int():
    """Postcondition: return value is a non-negative int for any input."""
    result = how_many_times('mississippi', 'issi')
    assert isinstance(result, int)
    assert result >= 0
    assert result == 2  # overlapping occurrences at indices 1 and 4
