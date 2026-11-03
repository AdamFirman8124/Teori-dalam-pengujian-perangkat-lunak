# file: project/f113/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f113 import odd_count


def test_odd_count_single_string():
    """Covers lines 3-7: builds res, iterates one string, counts odd digits, appends message, returns."""
    lst = ["1234567"]
    result = odd_count(lst)
    # digits 1,3,5,7 are odd -> n == 4
    assert result == ["the number of odd elements 4n the str4ng 4 of the 4nput."]


def test_odd_count_multiple_strings():
    """Covers multiple loop iterations (lines 4-6 executed repeatedly)."""
    lst = ["3", "11111111"]
    result = odd_count(lst)
    assert result == [
        "the number of odd elements 1n the str1ng 1 of the 1nput.",
        "the number of odd elements 8n the str8ng 8 of the 8nput.",
    ]


def test_odd_count_no_odd_digits():
    """Covers the branch where n == 0 (no odd digits in the string)."""
    lst = ["2468"]
    result = odd_count(lst)
    assert result == ["the number of odd elements 0n the str0ng 0 of the 0nput."]


def test_odd_count_empty_list():
    """Covers the loop-not-taken branch: empty input list returns empty list."""
    assert odd_count([]) == []


def test_odd_count_returns_new_list():
    """Verifies the returned list is a fresh object (postcondition of line 3/7)."""
    lst = ["1"]
    result = odd_count(lst)
    assert result is not lst
    assert isinstance(result, list)
    assert len(result) == 1
