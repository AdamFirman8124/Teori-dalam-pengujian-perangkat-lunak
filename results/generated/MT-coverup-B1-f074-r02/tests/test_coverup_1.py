# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

from f074 import total_match


def test_total_match_returns_first_list_when_total_length_is_smaller_or_equal():
    lst1 = ["a", "bc"]
    lst2 = ["long", "list"]

    result = total_match(lst1, lst2)

    assert result is lst1
    assert lst1 == ["a", "bc"]
    assert lst2 == ["long", "list"]


def test_total_match_returns_second_list_when_total_length_is_smaller():
    lst1 = ["longer", "list"]
    lst2 = ["a", "bc"]

    result = total_match(lst1, lst2)

    assert result is lst2
    assert lst1 == ["longer", "list"]
    assert lst2 == ["a", "bc"]
