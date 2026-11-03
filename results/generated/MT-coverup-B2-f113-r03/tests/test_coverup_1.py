# file: project/f113/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

from f113 import odd_count


def test_odd_count_empty_list():
    """Covers lines 3 and 7 (loop body skipped)."""
    result = odd_count([])
    assert result == []
    assert isinstance(result, list)


def test_odd_count_single_string():
    """Covers lines 3-7: loop body executes once."""
    result = odd_count(["1234567"])
    # digits 1, 3, 5, 7 are odd -> n == 4
    assert result == ["the number of odd elements 4n the str4ng 4 of the 4nput."]


def test_odd_count_multiple_strings():
    """Covers lines 3-7 with multiple loop iterations."""
    result = odd_count(["3", "11111111"])
    assert result == [
        "the number of odd elements 1n the str1ng 1 of the 1nput.",
        "the number of odd elements 8n the str8ng 8 of the 8nput.",
    ]


def test_odd_count_no_odd_digits():
    """Covers lines 3-7 when the odd-count is zero."""
    result = odd_count(["2468"])
    assert result == ["the number of odd elements 0n the str0ng 0 of the 0nput."]


def test_odd_count_does_not_mutate_input():
    """Postcondition: the input list is left untouched (pure function)."""
    lst = ["135", "246"]
    snapshot = list(lst)
    result = odd_count(lst)
    assert lst == snapshot
    assert result == [
        "the number of odd elements 3n the str3ng 3 of the 3nput.",
        "the number of odd elements 0n the str0ng 0 of the 0nput.",
    ]
