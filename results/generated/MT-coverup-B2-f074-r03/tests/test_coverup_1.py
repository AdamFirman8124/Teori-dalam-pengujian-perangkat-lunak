# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

"""Tests for f074.total_match — full line and branch coverage.

total_match(lst1, lst2) returns the list whose total character length is
smaller; on a tie (l1 <= l2) it returns lst1.

The function is pure (no I/O, no globals, no mutation of its arguments),
so no monkeypatching or fixture cleanup is required; the tests below also
assert that the inputs are left unmodified to guard against state pollution.
"""

import pytest

from f074 import total_match


def test_total_match_first_shorter_returns_lst1():
    """l1 < l2 -> returns lst1 (covers lines 3-5, 7-9, 11-12)."""
    lst1 = ["hi", "a"]          # total length 3
    lst2 = ["hello", "world"]   # total length 10
    result = total_match(lst1, lst2)
    assert result is lst1
    assert result == ["hi", "a"]
    # Inputs must not be mutated.
    assert lst1 == ["hi", "a"]
    assert lst2 == ["hello", "world"]


def test_total_match_equal_lengths_returns_lst1():
    """l1 == l2 -> tie broken in favour of lst1 (covers the '<=' branch)."""
    lst1 = ["ab", "cd"]         # total length 4
    lst2 = ["a", "bcd"]         # total length 4
    result = total_match(lst1, lst2)
    assert result is lst1
    assert result == ["ab", "cd"]
    assert lst1 == ["ab", "cd"]
    assert lst2 == ["a", "bcd"]


def test_total_match_first_longer_returns_lst2():
    """l1 > l2 -> returns lst2 (covers line 14, the 'else' branch)."""
    lst1 = ["hello", "world"]   # total length 10
    lst2 = ["hi", "a"]          # total length 3
    result = total_match(lst1, lst2)
    assert result is lst2
    assert result == ["hi", "a"]
    assert lst1 == ["hello", "world"]
    assert lst2 == ["hi", "a"]


def test_total_match_empty_lists():
    """Empty lists exercise the loop-skip paths (lines 3 and 7 without bodies)."""
    # Both empty: l1 == l2 == 0 -> lst1.
    assert total_match([], []) == []
    # lst1 empty: l1 = 0 <= l2 = 3 -> lst1.
    assert total_match([], ["abc"]) == []
    # lst2 empty: l1 = 3 > l2 = 0 -> lst2.
    assert total_match(["abc"], []) == []
