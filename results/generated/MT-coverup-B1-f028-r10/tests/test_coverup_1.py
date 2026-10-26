# file: project/f028/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f028 import concatenate


def test_concatenate_multiple_strings():
    result = concatenate(["hello", " ", "world"])
    assert result == "hello world"


def test_concatenate_empty_list():
    result = concatenate([])
    assert result == ""


def test_concatenate_single_string():
    result = concatenate(["abc"])
    assert result == "abc"


def test_concatenate_empty_strings():
    result = concatenate(["", "", ""])
    assert result == ""
