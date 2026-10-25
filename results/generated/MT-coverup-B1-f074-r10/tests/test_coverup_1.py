# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

from f074 import total_match


def test_total_match_returns_first_list_when_total_lengths_are_equal():
    lst1 = ["ab", "c"]
    lst2 = ["a", "bc"]

    result = total_match(lst1, lst2)

    assert result is lst1


def test_total_match_returns_second_list_when_first_is_longer():
    lst1 = ["abcd", "ef"]
    lst2 = ["a", "bc"]

    result = total_match(lst1, lst2)

    assert result is lst2
