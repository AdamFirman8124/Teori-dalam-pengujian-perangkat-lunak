# file: project/f113/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f113 import odd_count


def test_odd_count_empty_list():
    assert odd_count([]) == []


def test_odd_count_single_mixed_list():
    lst = [[1, 2, 3]]
    original = [list(a) for a in lst]
    result = odd_count(lst)
    assert result == ["the number of odd elements 2n the str2ng 2 of the 2nput."]
    # verify no mutation of input (no state pollution)
    assert lst == original


def test_odd_count_multiple_lists_covers_branches():
    lst = [[1, 2, 3], [2, 4, 6], [1, 3, 5], []]
    original = [list(a) for a in lst]
    result = odd_count(lst)
    assert result == [
        "the number of odd elements 2n the str2ng 2 of the 2nput.",
        "the number of odd elements 0n the str0ng 0 of the 0nput.",
        "the number of odd elements 3n the str3ng 3 of the 3nput.",
        "the number of odd elements 0n the str0ng 0 of the 0nput.",
    ]
    assert lst == original


def test_odd_count_string_elements():
    # covers int(d) conversion branch for string digits, both odd and even
    lst = [["1", "2", "4"]]
    result = odd_count(lst)
    assert result == ["the number of odd elements 1n the str1ng 1 of the 1nput."]
