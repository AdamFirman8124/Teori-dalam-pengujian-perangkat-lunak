# file: project/f113/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f113 import odd_count


def test_odd_count_empty_list():
    assert odd_count([]) == []


def test_odd_count_single_string_all_odd():
    assert odd_count(["13579"]) == [
        "the number of odd elements 5n the str5ng 5 of the 5nput."
    ]


def test_odd_count_single_string_all_even():
    assert odd_count(["2468"]) == [
        "the number of odd elements 0n the str0ng 0 of the 0nput."
    ]


def test_odd_count_empty_string():
    assert odd_count([""]) == [
        "the number of odd elements 0n the str0ng 0 of the 0nput."
    ]


def test_odd_count_multiple_strings():
    result = odd_count(["1234567", "0", "11"])
    assert result == [
        "the number of odd elements 4n the str4ng 4 of the 4nput.",
        "the number of odd elements 0n the str0ng 0 of the 0nput.",
        "the number of odd elements 2n the str2ng 2 of the 2nput.",
    ]
    assert len(result) == 3


def test_odd_count_does_not_mutate_input():
    lst = ["123", "456"]
    snapshot = list(lst)
    odd_count(lst)
    assert lst == snapshot
