# file: project/f007/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f007 import filter_by_substring


def test_filter_by_substring_basic():
    strings = ["hello", "world", "hello world"]
    result = filter_by_substring(strings, "hello")
    assert result == ["hello", "hello world"]
    # verify input not mutated
    assert strings == ["hello", "world", "hello world"]


def test_filter_by_substring_no_match():
    result = filter_by_substring(["abc", "def"], "xyz")
    assert result == []


def test_filter_by_substring_empty_list():
    result = filter_by_substring([], "a")
    assert result == []


def test_filter_by_substring_empty_substring_matches_all():
    strings = ["a", "b", ""]
    result = filter_by_substring(strings, "")
    assert result == ["a", "b", ""]
    assert strings == ["a", "b", ""]


def test_filter_by_substring_all_match():
    result = filter_by_substring(["aa", "aaa", "baa"], "aa")
    assert result == ["aa", "aaa", "baa"]
