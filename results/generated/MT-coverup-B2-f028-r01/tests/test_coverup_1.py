# file: project/f028/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f028 import concatenate


def test_concatenate_multiple_strings():
    assert concatenate(["hello", " ", "world"]) == "hello world"


def test_concatenate_empty_list():
    assert concatenate([]) == ""


def test_concatenate_single_string():
    assert concatenate(["abc"]) == "abc"
