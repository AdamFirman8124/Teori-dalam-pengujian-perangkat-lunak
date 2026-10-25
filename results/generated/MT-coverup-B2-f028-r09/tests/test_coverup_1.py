# file: project/f028/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f028 import concatenate


def test_concatenate_empty_list():
    result = concatenate([])
    assert result == ""
    assert isinstance(result, str)


def test_concatenate_single_string():
    result = concatenate(["hello"])
    assert result == "hello"


def test_concatenate_multiple_strings():
    result = concatenate(["foo", "bar", "baz"])
    assert result == "foobarbaz"


def test_concatenate_does_not_mutate_input():
    strings = ["a", "b"]
    concatenate(strings)
    assert strings == ["a", "b"]
