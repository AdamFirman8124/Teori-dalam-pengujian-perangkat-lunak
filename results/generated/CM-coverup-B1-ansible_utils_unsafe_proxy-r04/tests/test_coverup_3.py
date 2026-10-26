# file: project/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    _wrap_sequence,
    wrap_var,
)


def test_wrap_sequence_list():
    src = ["hello", "world"]
    result = _wrap_sequence(src)
    assert isinstance(result, list)
    assert type(result) is list
    assert len(result) == 2
    for item in result:
        assert isinstance(item, AnsibleUnsafe)
        assert isinstance(item, AnsibleUnsafeText)
    assert [str(x) for x in result] == ["hello", "world"]
    # input is not mutated in place
    assert src == ["hello", "world"]
    assert all(type(x) is str for x in src)


def test_wrap_sequence_tuple_mixed_types():
    src = ("hello", b"bytes", 42, None)
    result = _wrap_sequence(src)
    assert isinstance(result, tuple)
    assert type(result) is tuple
    assert len(result) == 4
    assert isinstance(result[0], AnsibleUnsafeText)
    assert str(result[0]) == "hello"
    assert isinstance(result[1], AnsibleUnsafeBytes)
    assert bytes(result[1]) == b"bytes"
    assert result[2] == 42
    assert type(result[2]) is int
    assert result[3] is None


def test_wrap_var_list_delegates_to_wrap_sequence():
    src = ["a", b"b", 1]
    result = wrap_var(src)
    assert isinstance(result, list)
    assert type(result) is list
    assert isinstance(result[0], AnsibleUnsafeText)
    assert str(result[0]) == "a"
    assert isinstance(result[1], AnsibleUnsafeBytes)
    assert bytes(result[1]) == b"b"
    assert result[2] == 1


def test_wrap_var_tuple_delegates_to_wrap_sequence():
    src = ("x", "y")
    result = wrap_var(src)
    assert isinstance(result, tuple)
    assert type(result) is tuple
    assert len(result) == 2
    assert all(isinstance(x, AnsibleUnsafe) for x in result)
    assert tuple(str(x) for x in result) == ("x", "y")
