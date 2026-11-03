# file: project/f028/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f028 import concatenate


def test_concatenate_empty_list():
    """Concatenating an empty list yields the empty string (hits line 6)."""
    assert concatenate([]) == ""


def test_concatenate_single_string():
    """Concatenating a single-element list returns that element unchanged."""
    assert concatenate(["hello"]) == "hello"


def test_concatenate_multiple_strings():
    """Concatenating several strings joins them in order with no separator."""
    assert concatenate(["foo", "bar", "baz"]) == "foobarbaz"


def test_concatenate_preserves_order_and_content():
    """Order of elements and exact contents are preserved."""
    parts = ["a", "b", "c", "d", "e"]
    assert concatenate(parts) == "abcde"
    # The input list must not be mutated by the function.
    assert parts == ["a", "b", "c", "d", "e"]
