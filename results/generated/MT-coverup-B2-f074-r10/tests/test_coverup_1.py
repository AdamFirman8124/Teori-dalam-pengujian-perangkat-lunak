# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

import pytest

from f074 import total_match


def test_total_match_returns_lst1_when_total_length_smaller():
    """l1 = 4, l2 = 7 -> l1 <= l2 -> returns lst1 (covers lines 3-5, 7-9, 11-12)."""
    lst1 = ["hi", "Hi"]
    lst2 = ["hi", "admin"]
    result = total_match(lst1, lst2)
    assert result == ["hi", "Hi"]
    assert result is lst1


def test_total_match_returns_lst2_when_total_length_smaller():
    """l1 = 7, l2 = 2 -> l1 > l2 -> returns lst2 (covers the else branch, line 14)."""
    lst1 = ["hi", "admin"]
    lst2 = ["hi"]
    result = total_match(lst1, lst2)
    assert result == ["hi"]
    assert result is lst2


def test_total_match_equal_total_lengths_returns_lst1():
    """l1 = 2, l2 = 2 -> l1 <= l2 (tie) -> returns lst1."""
    lst1 = ["ab"]
    lst2 = ["cd"]
    result = total_match(lst1, lst2)
    assert result == ["ab"]
    assert result is lst1


def test_total_match_both_empty_returns_lst1():
    """l1 = 0, l2 = 0 -> returns lst1 (empty lists skip both loops)."""
    result = total_match([], [])
    assert result == []
