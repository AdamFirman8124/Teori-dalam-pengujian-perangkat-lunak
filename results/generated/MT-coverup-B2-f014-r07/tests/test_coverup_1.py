# file: project/f014/__init__.py:4-10
# asked: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}
# gained: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}

import pytest

from f014 import all_prefixes


def test_all_prefixes_multiple_characters():
    """Covers lines 6, 8, 9, 10 with several loop iterations."""
    result = all_prefixes("abc")
    assert result == ["a", "ab", "abc"]
    # Postconditions: one prefix per character, last prefix is the full string,
    # and every entry is a prefix of the input in increasing length order.
    assert len(result) == len("abc")
    assert result[-1] == "abc"
    assert all(s.startswith(result[i - 1]) for i, s in enumerate(result) if i > 0)


def test_all_prefixes_single_character():
    """Loop body executes exactly once."""
    assert all_prefixes("x") == ["x"]


def test_all_prefixes_empty_string():
    """Covers lines 6 and 10 with zero loop iterations (loop branch not taken)."""
    assert all_prefixes("") == []


@pytest.mark.parametrize(
    "string",
    ["hello", "a", "", " ", "ab"],
)
def test_all_prefixes_generic_postconditions(string):
    result = all_prefixes(string)
    assert isinstance(result, list)
    assert len(result) == len(string)
    for i, prefix in enumerate(result):
        assert prefix == string[: i + 1]
    if string:
        assert result[-1] == string
