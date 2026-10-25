# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f029 import filter_by_prefix


def test_filter_by_prefix_basic_match():
    strings = ["apple", "apricot", "banana", "avocado", "blueberry"]
    result = filter_by_prefix(strings, "a")
    assert result == ["apple", "apricot", "avocado"]
    # verify input list is not mutated
    assert strings == ["apple", "apricot", "banana", "avocado", "blueberry"]


def test_filter_by_prefix_no_match():
    result = filter_by_prefix(["hello", "world"], "z")
    assert result == []


def test_filter_by_prefix_empty_list():
    assert filter_by_prefix([], "a") == []
    assert filter_by_prefix([], "") == []


def test_filter_by_prefix_empty_prefix_matches_all():
    strings = ["a", "b", "c"]
    assert filter_by_prefix(strings, "") == ["a", "b", "c"]


def test_filter_by_prefix_exact_and_longer_prefix():
    assert filter_by_prefix(["test", "testing", "tes"], "test") == ["test", "testing"]
    assert filter_by_prefix(["a", "ab"], "abc") == []
