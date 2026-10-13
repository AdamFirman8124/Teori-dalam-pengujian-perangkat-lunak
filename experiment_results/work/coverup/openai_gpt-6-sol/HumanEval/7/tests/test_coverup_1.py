# file: script_7.py:4-11
# asked: {"lines": [11], "branches": []}
# gained: {"lines": [11], "branches": []}

from script_7 import filter_by_substring


def test_filter_by_substring_keeps_only_matching_strings():
    strings = ["abc", "bacd", "cde", "array"]

    result = filter_by_substring(strings, "a")

    assert result == ["abc", "bacd", "array"]
    assert strings == ["abc", "bacd", "cde", "array"]
