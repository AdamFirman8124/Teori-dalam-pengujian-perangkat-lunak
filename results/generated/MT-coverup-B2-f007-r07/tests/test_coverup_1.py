# file: project/f007/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f007 import filter_by_substring


def test_filter_by_substring_includes_matches_and_excludes_nonmatches():
    strings = ["alpha", "beta", "alphabet", "gamma"]

    result = filter_by_substring(strings, "alpha")

    assert result == ["alpha", "alphabet"]
    assert strings == ["alpha", "beta", "alphabet", "gamma"]


def test_filter_by_substring_returns_empty_list_when_no_strings_match():
    assert filter_by_substring(["alpha", "beta"], "z") == []
