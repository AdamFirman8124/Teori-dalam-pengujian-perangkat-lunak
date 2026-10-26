# file: project/f028/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f028 import concatenate


def test_concatenate_empty_list():
    assert concatenate([]) == ""


def test_concatenate_single_string():
    assert concatenate(["hello"]) == "hello"


def test_concatenate_multiple_strings():
    assert concatenate(["foo", "bar", "baz"]) == "foobarbaz"
