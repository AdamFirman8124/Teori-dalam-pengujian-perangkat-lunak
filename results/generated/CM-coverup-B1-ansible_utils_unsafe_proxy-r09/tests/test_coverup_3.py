# file: project/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    wrap_var,
)


def test_wrap_var_wraps_list_items_as_unsafe():
    original = ["text", b"bytes", 42]

    wrapped = wrap_var(original)

    assert type(wrapped) is list
    assert wrapped is not original
    assert wrapped == original
    assert isinstance(wrapped[0], AnsibleUnsafeText)
    assert isinstance(wrapped[1], AnsibleUnsafeBytes)
    assert wrapped[2] == 42
    assert type(original[0]) is str
    assert type(original[1]) is bytes


def test_wrap_var_wraps_tuple_items_as_unsafe():
    original = ("text", b"bytes", 42)

    wrapped = wrap_var(original)

    assert type(wrapped) is tuple
    assert wrapped is not original
    assert wrapped == original
    assert isinstance(wrapped[0], AnsibleUnsafeText)
    assert isinstance(wrapped[1], AnsibleUnsafeBytes)
    assert wrapped[2] == 42
    assert type(original[0]) is str
    assert type(original[1]) is bytes
