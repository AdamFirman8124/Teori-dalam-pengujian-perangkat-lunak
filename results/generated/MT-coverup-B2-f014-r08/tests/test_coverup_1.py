# file: project/f014/__init__.py:4-10
# asked: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}
# gained: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}

import pytest

from f014 import all_prefixes


def test_all_prefixes_multiple_characters():
    """Covers lines 6-10 with several loop iterations."""
    result = all_prefixes("abc")
    assert result == ["a", "ab", "abc"]
    assert len(result) == len("abc")
    # Each prefix must be a prefix of the input and grow by one char.
    for i, prefix in enumerate(result):
        assert prefix == "abc"[: i + 1]


def test_all_prefixes_single_character():
    """Covers the loop body executing exactly once."""
    result = all_prefixes("x")
    assert result == ["x"]


def test_all_prefixes_empty_string():
    """Covers the zero-iteration branch of the loop (lines 6 and 10 only)."""
    result = all_prefixes("")
    assert result == []
    assert isinstance(result, list)
