# file: project/f028/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f028 import concatenate


def test_concatenate_empty_list():
    """An empty list should produce an empty string."""
    assert concatenate([]) == ""


def test_concatenate_single_string():
    """A single-element list should return that element unchanged."""
    assert concatenate(["hello"]) == "hello"


def test_concatenate_multiple_strings():
    """Multiple strings should be joined in order with no separator."""
    assert concatenate(["foo", "bar", "baz"]) == "foobarbaz"


def test_concatenate_with_empty_strings():
    """Empty strings within the list should not affect the result."""
    assert concatenate(["", "a", "", "b", ""]) == "ab"


def test_concatenate_preserves_order_and_content():
    """The result must contain all input strings in the given order."""
    parts = ["x", "y", "z"]
    result = concatenate(parts)
    assert result == "xyz"
    # Postcondition: input list is not mutated by the call.
    assert parts == ["x", "y", "z"]
