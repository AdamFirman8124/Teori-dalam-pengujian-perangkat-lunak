# file: script_7.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

import pytest

from script_7 import filter_by_substring


def test_filter_by_substring_empty_list():
    result = filter_by_substring([], "a")
    assert result == []
    assert isinstance(result, list)


def test_filter_by_substring_docstring_example():
    result = filter_by_substring(["abc", "bacd", "cde", "array"], "a")
    assert result == ["abc", "bacd", "array"]


def test_filter_by_substring_no_matches():
    assert filter_by_substring(["xyz", "qrs", "tuv"], "a") == []


def test_filter_by_substring_empty_substring_keeps_all():
    strings = ["abc", "bacd", "cde", "array"]
    result = filter_by_substring(strings, "")
    assert result == strings
    assert result is not strings


def test_filter_by_substring_does_not_mutate_input():
    strings = ["abc", "cde", "array"]
    snapshot = list(strings)
    filter_by_substring(strings, "a")
    assert strings == snapshot


@pytest.mark.parametrize(
    "strings, substring, expected",
    [
        (["hello", "world"], "o", ["hello", "world"]),
        (["hello", "world"], "z", []),
        (["abc"], "abcd", []),
        (["abc"], "abc", ["abc"]),
        (["abc", "abc"], "abc", ["abc", "abc"]),
    ],
)
def test_filter_by_substring_parametrized(strings, substring, expected):
    assert filter_by_substring(strings, substring) == expected
