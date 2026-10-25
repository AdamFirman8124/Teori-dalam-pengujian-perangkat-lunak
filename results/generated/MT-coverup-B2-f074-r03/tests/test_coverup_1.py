# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

from f074 import total_match


def test_total_match_returns_first_list_when_total_length_is_smaller_or_equal():
    lst1 = ["a", "bb"]
    lst2 = ["long"]
    original_lst1 = lst1.copy()
    original_lst2 = lst2.copy()

    result = total_match(lst1, lst2)

    assert result is lst1
    assert lst1 == original_lst1
    assert lst2 == original_lst2


def test_total_match_returns_second_list_when_its_total_length_is_smaller():
    lst1 = ["long", "text"]
    lst2 = ["a", "b"]
    original_lst1 = lst1.copy()
    original_lst2 = lst2.copy()

    result = total_match(lst1, lst2)

    assert result is lst2
    assert lst1 == original_lst1
    assert lst2 == original_lst2
