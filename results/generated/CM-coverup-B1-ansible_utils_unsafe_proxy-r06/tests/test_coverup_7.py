# file: project/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    wrap_var,
)


def test_wrap_var_wraps_set_items():
    original = {"text", b"bytes", 42}

    wrapped = wrap_var(original)

    assert wrapped == original
    assert wrapped is not original
    assert original == {"text", b"bytes", 42}
    assert any(type(item) is AnsibleUnsafeText for item in wrapped)
    assert any(type(item) is AnsibleUnsafeBytes for item in wrapped)
    assert 42 in wrapped
