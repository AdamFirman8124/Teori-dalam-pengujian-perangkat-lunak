# file: project/f028/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f028 import concatenate


def test_concatenate_basic():
    """Calling concatenate executes line 6 (the join) for a non-empty list."""
    result = concatenate(["hello", " ", "world"])
    assert result == "hello world"
    assert isinstance(result, str)


def test_concatenate_empty_list():
    """Edge case: an empty list joins to the empty string."""
    assert concatenate([]) == ""


def test_concatenate_single_element():
    """A single-element list returns that element unchanged."""
    assert concatenate(["only"]) == "only"


def test_concatenate_no_state_pollution():
    """The function is pure: repeated calls with same input give same output."""
    input_list = ["a", "b", "c"]
    assert concatenate(input_list) == "abc"
    assert concatenate(input_list) == "abc"
    # Input list must not be mutated by the call.
    assert input_list == ["a", "b", "c"]
