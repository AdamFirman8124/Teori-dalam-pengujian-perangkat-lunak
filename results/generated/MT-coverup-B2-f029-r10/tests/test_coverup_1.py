# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f029 import filter_by_prefix


def test_filter_by_prefix_returns_matching_strings():
    strings = ["abc", "bcd", "cde", "abcde"]
    result = filter_by_prefix(strings, "abc")
    assert result == ["abc", "abcde"]
    assert all(x.startswith("abc") for x in result)


def test_filter_by_prefix_no_matches_returns_empty_list():
    strings = ["abc", "bcd", "cde"]
    result = filter_by_prefix(strings, "xyz")
    assert result == []
    assert isinstance(result, list)


def test_filter_by_prefix_empty_input_returns_empty_list():
    result = filter_by_prefix([], "a")
    assert result == []


def test_filter_by_prefix_empty_prefix_returns_all_strings():
    strings = ["abc", "bcd", ""]
    result = filter_by_prefix(strings, "")
    assert result == ["abc", "bcd", ""]


def test_filter_by_prefix_does_not_mutate_input():
    strings = ["abc", "bcd", "abcde"]
    original = list(strings)
    filter_by_prefix(strings, "abc")
    assert strings == original
