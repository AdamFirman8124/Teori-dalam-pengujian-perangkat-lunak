# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

import pytest

from f074 import total_match


def test_total_match_returns_first_when_shorter():
    lst1 = ["a", "b"]
    lst2 = ["aaa", "bbb"]
    result = total_match(lst1, lst2)
    assert result is lst1
    assert result == ["a", "b"]
    assert sum(len(s) for s in result) == 2


def test_total_match_returns_second_when_shorter():
    lst1 = ["aaa", "bbb"]
    lst2 = ["a"]
    result = total_match(lst1, lst2)
    assert result is lst2
    assert result == ["a"]
    assert sum(len(s) for s in result) == 1


def test_total_match_tie_returns_first():
    lst1 = ["ab"]
    lst2 = ["cd"]
    result = total_match(lst1, lst2)
    assert result is lst1
    assert result == ["ab"]


def test_total_match_both_empty_returns_first():
    lst1 = []
    lst2 = []
    assert total_match(lst1, lst2) is lst1
    assert total_match(lst2, lst1) is lst2


def test_total_match_empty_first_nonempty_second():
    lst1 = []
    lst2 = ["x"]
    assert total_match(lst1, lst2) is lst1


def test_total_match_empty_second_nonempty_first():
    lst1 = ["x"]
    lst2 = []
    assert total_match(lst1, lst2) is lst2


def test_total_match_does_not_mutate_inputs():
    lst1 = ["abc", "de"]
    lst2 = ["f"]
    snapshot1 = list(lst1)
    snapshot2 = list(lst2)
    total_match(lst1, lst2)
    assert lst1 == snapshot1
    assert lst2 == snapshot2
