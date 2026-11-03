# file: project/f012/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

import pytest

from f012 import longest


def test_longest_empty_list_returns_none():
    """An empty input list should return None (covers lines 6-7)."""
    assert longest([]) is None


def test_longest_single_element():
    """A single-element list should return that element (covers lines 9-12)."""
    result = longest(["hello"])
    assert result == "hello"


def test_longest_returns_first_of_max_length():
    """When several strings share the max length, the first one is returned."""
    strings = ["ab", "xyz", "cdef", "abcd", "w"]
    result = longest(strings)
    assert result == "cdef"
    assert len(result) == 4


def test_longest_first_string_longest():
    """The first string being the longest should be returned directly."""
    strings = ["longest", "a", "bb"]
    assert longest(strings) == "longest"


def test_longest_last_string_longest():
    """The last string being the longest should be found via the loop."""
    strings = ["a", "bb", "ccc"]
    assert longest(strings) == "ccc"


def test_longest_all_same_length_returns_first():
    """All strings of equal length -> the very first one is returned."""
    strings = ["aa", "bb", "cc"]
    assert longest(strings) == "aa"


def test_longest_does_not_mutate_input():
    """The function must not modify the input list."""
    strings = ["one", "three", "two"]
    snapshot = list(strings)
    longest(strings)
    assert strings == snapshot


@pytest.mark.parametrize(
    "strings, expected",
    [
        ([], None),
        (["a"], "a"),
        (["a", "bb"], "bb"),
        (["bb", "a"], "bb"),
        (["x", "yy", "zz"], "yy"),
    ],
)
def test_longest_parametrized(strings, expected):
    assert longest(strings) == expected
