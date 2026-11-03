# file: project/f014/__init__.py:4-10
# asked: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}
# gained: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}

import pytest

from f014 import all_prefixes


def test_all_prefixes_empty_string():
    """Empty input: loop body (lines 8-9) never runs, but lines 6 and 10 do."""
    result = all_prefixes("")
    assert result == []
    assert isinstance(result, list)


def test_all_prefixes_single_character():
    """Single character: loop body executes exactly once."""
    result = all_prefixes("a")
    assert result == ["a"]


def test_all_prefixes_multiple_characters():
    """Multiple characters: every prefix of increasing length is returned, in order."""
    result = all_prefixes("abc")
    assert result == ["a", "ab", "abc"]
    assert len(result) == len("abc")


def test_all_prefixes_postconditions():
    """Each returned element is a string prefix of the input, with strictly growing length."""
    string = "hello"
    result = all_prefixes(string)
    assert len(result) == len(string)
    for i, prefix in enumerate(result):
        assert isinstance(prefix, str)
        assert string.startswith(prefix)
        assert len(prefix) == i + 1
        assert prefix == string[: i + 1]
