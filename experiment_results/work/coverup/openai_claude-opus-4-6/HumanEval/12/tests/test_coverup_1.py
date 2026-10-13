# file: script_12.py:4-20
# asked: {"lines": [14, 15, 17, 18, 19, 20], "branches": [[14, 15], [14, 17], [18, 0], [18, 19], [19, 18], [19, 20]]}
# gained: {"lines": [14, 15, 17, 18, 19, 20], "branches": [[14, 15], [14, 17], [18, 19], [19, 18], [19, 20]]}

from typing import List, Optional

import pytest

from script_12 import longest


def test_longest_empty_list_returns_none():
    result = longest([])
    assert result is None


def test_longest_single_element_returns_that_element():
    result = longest(["hello"])
    assert result == "hello"


def test_longest_returns_longest_string():
    result = longest(["a", "bb", "ccc"])
    assert result == "ccc"


def test_longest_returns_first_of_equal_lengths():
    result = longest(["a", "b", "c"])
    assert result == "a"
    assert longest(["aa", "bb", "cc"]) == "aa"


def test_longest_ignores_shorter_strings_before_the_longest():
    result = longest(["x", "yyy", "z"])
    assert result == "yyy"


def test_longest_handles_empty_strings():
    assert longest([""]) == ""
    assert longest(["", "", "a"]) == "a"
    assert longest(["", ""]) == ""


def test_longest_with_sequence_of_strings():
    strings: List[str] = ["ab", "cdef", "gh"]
    result: Optional[str] = longest(strings)
    assert result == "cdef"
    assert strings == ["ab", "cdef", "gh"]


@pytest.mark.parametrize(
    "strings, expected",
    [
        ([], None),
        (["a"], "a"),
        (["a", "bb", "ccc"], "ccc"),
        (["a", "b", "c"], "a"),
        (["longest", "lo", "l"], "longest"),
        (["", ""], ""),
    ],
)
def test_longest_parametrized(strings, expected):
    assert longest(strings) == expected
