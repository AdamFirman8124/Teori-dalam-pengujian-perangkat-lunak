# file: project/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeText,
    _wrap_sequence,
    wrap_var,
)


def test_wrap_sequence_list_of_strings():
    original = ["hello", "world"]
    result = _wrap_sequence(original)

    assert type(result) is list
    assert result == ["hello", "world"]
    assert result is not original
    assert all(type(item) is AnsibleUnsafeText for item in result)
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    # Original is not mutated / not marked unsafe
    assert all(type(item) is str for item in original)
    assert not any(isinstance(item, AnsibleUnsafe) for item in original)


def test_wrap_sequence_tuple_of_strings():
    original = ("hello", "world")
    result = _wrap_sequence(original)

    assert type(result) is tuple
    assert result == ("hello", "world")
    assert result is not original
    assert all(type(item) is AnsibleUnsafeText for item in result)
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert all(type(item) is str for item in original)


def test_wrap_sequence_empty_list_and_tuple():
    empty_list = _wrap_sequence([])
    empty_tuple = _wrap_sequence(())

    assert type(empty_list) is list
    assert empty_list == []
    assert type(empty_tuple) is tuple
    assert empty_tuple == ()


def test_wrap_sequence_mixed_and_nested_values():
    original = ["text", 42, ["nested"], {"key": "value"}]
    result = _wrap_sequence(original)

    assert type(result) is list
    assert type(result[0]) is AnsibleUnsafeText
    assert result[0] == "text"
    assert result[1] == 42
    assert type(result[1]) is int
    assert type(result[2]) is list
    assert type(result[2][0]) is AnsibleUnsafeText
    assert result[2][0] == "nested"
    assert type(result[3]) is dict
    assert list(result[3].keys())[0] == "key"
    assert type(list(result[3].keys())[0]) is AnsibleUnsafeText
    assert type(list(result[3].values())[0]) is AnsibleUnsafeText
    assert list(result[3].values())[0] == "value"
    # Original nested structures unchanged
    assert type(original[0]) is str
    assert type(original[2][0]) is str
    assert type(list(original[3].keys())[0]) is str


def test_wrap_sequence_via_wrap_var_list():
    result = wrap_var(["a", "b"])

    assert type(result) is list
    assert result == ["a", "b"]
    assert all(type(item) is AnsibleUnsafeText for item in result)
    assert all(isinstance(item, AnsibleUnsafe) for item in result)


def test_wrap_sequence_preserves_list_subclass_type():
    class MyList(list):
        pass

    result = _wrap_sequence(MyList(["x"]))

    assert type(result) is MyList
    assert result == ["x"]
    assert type(result[0]) is AnsibleUnsafeText
