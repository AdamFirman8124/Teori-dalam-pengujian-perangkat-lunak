# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

import pytest

from f074 import total_match


def test_total_match_returns_first_when_shorter():
    lst1 = ["a", "bb"]
    lst2 = ["ccc", "dddd"]
    result = total_match(lst1, lst2)
    assert result == lst1
    assert result is lst1


def test_total_match_returns_first_when_equal():
    lst1 = ["ab", "c"]
    lst2 = ["abc"]
    result = total_match(lst1, lst2)
    assert result == lst1
    assert result is lst1


def test_total_match_returns_second_when_longer():
    lst1 = ["aaaa", "bbbb"]
    lst2 = ["c"]
    result = total_match(lst1, lst2)
    assert result == lst2
    assert result is lst2


def test_total_match_both_empty_returns_first():
    lst1 = []
    lst2 = []
    result = total_match(lst1, lst2)
    assert result == []
    assert result is lst1


def test_total_match_empty_first_returns_first():
    lst1 = []
    lst2 = ["abc"]
    result = total_match(lst1, lst2)
    assert result is lst1


def test_total_match_empty_second_returns_second():
    lst1 = ["abc"]
    lst2 = []
    result = total_match(lst1, lst2)
    assert result is lst2


def test_total_match_does_not_mutate_inputs():
    lst1 = ["a", "bb"]
    lst2 = ["ccc"]
    snapshot1 = list(lst1)
    snapshot2 = list(lst2)
    total_match(lst1, lst2)
    assert lst1 == snapshot1
    assert lst2 == snapshot2
