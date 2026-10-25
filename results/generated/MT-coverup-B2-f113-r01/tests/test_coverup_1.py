# file: project/f113/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f113 import odd_count


def test_odd_count_with_odd_and_even_digits():
    assert odd_count(["1234567", "2468"]) == [
        "the number of odd elements 4n the str4ng 4 of the 4nput.",
        "the number of odd elements 0n the str0ng 0 of the 0nput.",
    ]


def test_odd_count_with_empty_inputs():
    assert odd_count([]) == []
    assert odd_count([""]) == [
        "the number of odd elements 0n the str0ng 0 of the 0nput."
    ]
