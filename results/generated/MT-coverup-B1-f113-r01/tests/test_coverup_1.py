# file: project/f113/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f113 import odd_count


def test_odd_count_empty_list():
    assert odd_count([]) == []


def test_odd_count_single_mixed_string():
    # '1','3','5' are odd (True branch), '2','4' are even (False branch)
    assert odd_count(["12345"]) == [
        "the number of odd elements 3n the str3ng 3 of the 3nput."
    ]


def test_odd_count_multiple_cases():
    # all even -> n=0, all odd -> n=5, empty string -> n=0 (empty generator)
    assert odd_count(["2468", "13579", ""]) == [
        "the number of odd elements 0n the str0ng 0 of the 0nput.",
        "the number of odd elements 5n the str5ng 5 of the 5nput.",
        "the number of odd elements 0n the str0ng 0 of the 0nput.",
    ]


def test_odd_count_list_of_ints():
    # covers arr as list of ints: 1 odd, 2 even
    assert odd_count([[1, 2, 3]]) == [
        "the number of odd elements 2n the str2ng 2 of the 2nput."
    ]
