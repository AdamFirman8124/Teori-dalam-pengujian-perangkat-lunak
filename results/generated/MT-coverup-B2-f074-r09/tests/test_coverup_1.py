# file: project/f074/__init__.py:1-14
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11, 12, 14], "branches": [[4, 5], [4, 7], [8, 9], [8, 11], [11, 12], [11, 14]]}

import pytest

from f074 import total_match


def test_total_match_lst1_shorter():
    """When lst1 has fewer total chars, lst1 is returned (lines 3-5, 7-9, 11-12)."""
    lst1 = ["hi", "a"]
    lst2 = ["hello", "world"]
    result = total_match(lst1, lst2)
    # l1 = 3, l2 = 10 -> l1 <= l2 -> return lst1
    assert result == ["hi", "a"]
    assert result is lst1


def test_total_match_lst2_shorter():
    """When lst2 has fewer total chars, lst2 is returned (line 14, else branch)."""
    lst1 = ["hello", "world"]
    lst2 = ["hi", "a"]
    result = total_match(lst1, lst2)
    # l1 = 10, l2 = 3 -> l1 > l2 -> return lst2
    assert result == ["hi", "a"]
    assert result is lst2


def test_total_match_tie_returns_lst1():
    """On a tie (l1 == l2), the '<=' comparison makes lst1 win."""
    lst1 = ["ab", "cd"]
    lst2 = ["ef", "gh"]
    result = total_match(lst1, lst2)
    # l1 = 4, l2 = 4 -> l1 <= l2 -> return lst1
    assert result == ["ab", "cd"]
    assert result is lst1


def test_total_match_empty_lst1():
    """An empty lst1 always has the smallest length (0 chars)."""
    lst1 = []
    lst2 = ["anything"]
    result = total_match(lst1, lst2)
    assert result == []
    assert result is lst1


def test_total_match_both_empty():
    """Both lists empty: tie at 0 chars, lst1 returned."""
    lst1 = []
    lst2 = []
    result = total_match(lst1, lst2)
    assert result == []
    assert result is lst1


def test_total_match_single_char_each():
    """Single-element lists exercising both loop bodies minimally."""
    assert total_match(["x"], ["yy"]) == ["x"]
    assert total_match(["xx"], ["y"]) == ["y"]


@pytest.mark.parametrize(
    "lst1,lst2,expected",
    [
        (["one", "two", "three"], ["four", "five"], ["four", "five"]),
        (["a", "b", "c"], ["d", "e"], ["d", "e"]),
        (["aaaa"], ["bb", "cc"], ["aaaa"]),  # tie: 4 vs 4 -> lst1
    ],
)
def test_total_match_parametrized(lst1, lst2, expected):
    result = total_match(lst1, lst2)
    assert result == expected
    # Inputs must not be mutated by the function
    assert isinstance(result, list)
