# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

from f074 import total_match


def test_total_match_returns_lst1_when_total_less():
    lst1 = ["a", "bb"]
    lst2 = ["abcd"]
    result = total_match(lst1, lst2)
    assert result == ["a", "bb"]
    assert result is lst1


def test_total_match_returns_lst1_when_totals_equal():
    lst1 = ["ab", "c"]
    lst2 = ["xyz"]
    result = total_match(lst1, lst2)
    assert result == ["ab", "c"]
    assert result is lst1


def test_total_match_returns_lst2_when_total_greater():
    lst1 = ["abc", "de"]
    lst2 = ["a"]
    result = total_match(lst1, lst2)
    assert result == ["a"]
    assert result is lst2


def test_total_match_both_empty():
    lst1 = []
    lst2 = []
    result = total_match(lst1, lst2)
    assert result == []
    assert result is lst1


def test_total_match_empty_lst1():
    lst1 = []
    lst2 = ["hello"]
    result = total_match(lst1, lst2)
    assert result == []
    assert result is lst1


def test_total_match_empty_lst2():
    lst1 = ["hello"]
    lst2 = []
    result = total_match(lst1, lst2)
    assert result == []
    assert result is lst2
