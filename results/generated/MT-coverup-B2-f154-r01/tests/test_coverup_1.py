# file: project/f154/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[5, 6], [5, 9], [6, 5], [6, 7], [7, 6], [7, 8]]}

import pytest

from f154 import cycpattern_check


def test_true_when_b_is_direct_substring_of_a():
    # Covers: outer loop, inner loop, line 7 condition True -> line 8 return True.
    assert cycpattern_check("hello", "ell") is True


def test_true_when_rotation_of_b_matches():
    # "baa" itself is not in "abab", but its rotation "aba" is (matched at j=2),
    # so the inner loop must advance past j=0 before returning True.
    assert cycpattern_check("abab", "baa") is True


def test_true_for_another_rotation_match():
    # Requires scanning several i values and several j values before a hit.
    assert cycpattern_check("himenss", "simen") is True


def test_true_at_last_possible_position():
    # Match only occurs at the final i of the outer range.
    assert cycpattern_check("xxell", "ell") is True


def test_false_when_no_rotation_matches():
    # Covers: inner loop exhausting all j values (including j == l) with no
    # match, outer loop exhausting all i values -> line 9 return False.
    assert cycpattern_check("abcd", "abd") is False


def test_false_after_full_scan_single_outer_iteration():
    # len(a) == len(b): exactly one outer iteration, inner loop fully scans.
    assert cycpattern_check("efef", "eeff") is False


def test_false_multiple_outer_iterations_no_match():
    assert cycpattern_check("whassup", "psus") is False


def test_false_when_b_longer_than_a():
    # len(a) - l + 1 <= 0: outer loop body never executes -> line 9 return False.
    assert cycpattern_check("ab", "abc") is False


def test_false_for_empty_a_and_nonempty_b():
    # range(0 - 1 + 1) == range(0): outer loop skipped entirely.
    assert cycpattern_check("", "a") is False


def test_empty_b_trivially_matches():
    # l == 0: pat == "", inner loop runs once with j == 0 and the empty
    # slices compare equal -> line 8 return True.
    assert cycpattern_check("xyz", "") is True


def test_both_empty():
    # l == 0 and a single outer iteration (i == 0) with an empty-slice match.
    assert cycpattern_check("", "") is True
