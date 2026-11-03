# file: project/f028/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f028 import concatenate


def test_concatenate_empty_list():
    """Calling with an empty list executes the join and returns an empty string."""
    assert concatenate([]) == ""


def test_concatenate_single_string():
    """Calling with a single string executes the join and returns it unchanged."""
    assert concatenate(["hello"]) == "hello"


def test_concatenate_multiple_strings():
    """Calling with multiple strings executes the join and concatenates them."""
    assert concatenate(["a", "b", "c"]) == "abc"


def test_concatenate_no_mutation():
    """The join must not mutate the input list."""
    strings = ["x", "y"]
    result = concatenate(strings)
    assert result == "xy"
    assert strings == ["x", "y"]
