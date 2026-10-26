# file: project/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    wrap_var,
)


def test_wrap_var_wraps_dictionary_keys_and_values():
    original = {"key": "value", b"bytes-key": b"bytes-value"}

    wrapped = wrap_var(original)

    assert isinstance(wrapped, dict)
    assert wrapped is not original
    assert isinstance(next(key for key in wrapped if key == "key"), AnsibleUnsafeText)
    assert isinstance(wrapped["key"], AnsibleUnsafeText)
    assert isinstance(next(key for key in wrapped if key == b"bytes-key"), AnsibleUnsafeBytes)
    assert isinstance(wrapped[b"bytes-key"], AnsibleUnsafeBytes)
    assert type(next(iter(original))) is str
    assert type(original["key"]) is str
    assert type(original[b"bytes-key"]) is bytes
