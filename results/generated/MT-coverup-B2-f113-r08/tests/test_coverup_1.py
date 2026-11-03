# file: project/f113/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f113 import odd_count


def test_odd_count_returns_empty_list_for_empty_input():
    assert odd_count([]) == []


def test_odd_count_counts_odd_digits_correctly():
    lst = ["1234567"]
    expected = ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(lst) == expected


def test_odd_count_multiple_items():
    lst = ["3", "11111111", "2468"]
    expected = [
        "the number of odd elements 1n the str1ng 1 of the 1nput.",
        "the number of odd elements 8n the str8ng 8 of the 8nput.",
        "the number of odd elements 0n the str0ng 0 of the 0nput.",
    ]
    assert odd_count(lst) == expected
