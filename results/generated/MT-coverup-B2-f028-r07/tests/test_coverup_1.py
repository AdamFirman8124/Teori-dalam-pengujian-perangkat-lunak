# file: project/f028/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f028 import concatenate


def test_concatenate_empty_list():
    """Empty input list joins to an empty string."""
    assert concatenate([]) == ""


def test_concatenate_single_string():
    """A single-element list returns that element unchanged."""
    assert concatenate(["hello"]) == "hello"


def test_concatenate_multiple_strings():
    """Multiple elements are joined in order with no separator."""
    assert concatenate(["foo", "bar", "baz"]) == "foobarbaz"


def test_concatenate_preserves_internal_whitespace_and_order():
    """Joining preserves internal whitespace and element ordering."""
    assert concatenate(["a b", "", "c\n"]) == "a bc\n"
