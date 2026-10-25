# file: project/f113/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f113 import odd_count


def test_odd_count_with_mixed_digits():
    assert odd_count(["1234", "2468"]) == [
        "the number of odd elements 2n the str2ng 2 of the 2nput.",
        "the number of odd elements 0n the str0ng 0 of the 0nput.",
    ]


def test_odd_count_with_empty_list():
    assert odd_count([]) == []
