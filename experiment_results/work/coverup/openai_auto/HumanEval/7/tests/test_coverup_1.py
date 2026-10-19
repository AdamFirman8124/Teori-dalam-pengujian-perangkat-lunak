# file: script_7.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

from typing import List

from script_7 import filter_by_substring


def test_filter_by_substring_executes_return_statement():
    # Non-empty list: line 11 must execute and filter correctly.
    strings = ["abc", "bacd", "cde", "array"]
    result = filter_by_substring(strings, "a")
    assert result == ["abc", "bacd", "array"]


def test_filter_by_substring_empty_list():
    # Empty input: return list comprehension should yield [].
    assert filter_by_substring([], "a") == []


def test_filter_by_substring_no_matches():
    # All elements fail the substring check: comprehension branch filters all.
    strings = ["xyz", "hello", "world"]
    assert filter_by_substring(strings, "a") == []


def test_filter_by_substring_all_matches():
    # All elements contain the substring: comprehension keeps all.
    strings = ["cat", "bat", "rat"]
    assert filter_by_substring(strings, "at") == ["cat", "bat", "rat"]


def test_filter_by_substring_empty_substring():
    # Empty substring is contained in every string, so all are kept.
    strings = ["a", "b", ""]
    assert filter_by_substring(strings, "") == ["a", "b", ""]


def test_filter_by_substring_does_not_mutate_input():
    # Postcondition: input list remains unchanged and result is a new list.
    strings = ["abc", "cde", "array"]
    original = list(strings)
    result = filter_by_substring(strings, "a")
    assert result == ["abc", "array"]
    assert strings == original
    assert result is not strings
