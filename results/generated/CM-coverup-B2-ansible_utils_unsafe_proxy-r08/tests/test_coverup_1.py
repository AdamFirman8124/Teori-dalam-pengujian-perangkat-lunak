# file: project/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}

from ansible.utils.native_jinja import NativeJinjaText
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    NativeJinjaUnsafeText,
    wrap_var,
)


def test_wrap_var_returns_none_unchanged():
    assert wrap_var(None) is None


def test_wrap_var_returns_existing_unsafe_value_unchanged():
    value = AnsibleUnsafeText("already unsafe")

    assert wrap_var(value) is value


def test_wrap_var_wraps_mapping_keys_and_values_without_mutating_input():
    value = {"key": "value"}

    result = wrap_var(value)

    assert result == value
    assert result is not value
    assert type(next(iter(result))) is AnsibleUnsafeText
    assert type(result["key"]) is AnsibleUnsafeText
    assert type(next(iter(value))) is str
    assert type(value["key"]) is str


def test_wrap_var_wraps_set_items_without_mutating_input():
    value = {"item"}

    result = wrap_var(value)

    assert result == value
    assert result is not value
    assert type(next(iter(result))) is AnsibleUnsafeText
    assert type(next(iter(value))) is str


def test_wrap_var_wraps_sequence_items_and_preserves_sequence_type():
    value = ["text", b"bytes", 42]

    result = wrap_var(value)

    assert result == value
    assert result is not value
    assert type(result) is list
    assert type(result[0]) is AnsibleUnsafeText
    assert type(result[1]) is AnsibleUnsafeBytes
    assert result[2] is value[2]
    assert type(value[0]) is str
    assert type(value[1]) is bytes


def test_wrap_var_wraps_native_jinja_text():
    value = NativeJinjaText("native text")

    result = wrap_var(value)

    assert result == value
    assert type(result) is NativeJinjaUnsafeText


def test_wrap_var_wraps_bytes():
    value = b"binary value"

    result = wrap_var(value)

    assert result == value
    assert type(result) is AnsibleUnsafeBytes


def test_wrap_var_wraps_text():
    value = "text value"

    result = wrap_var(value)

    assert result == value
    assert type(result) is AnsibleUnsafeText


def test_wrap_var_returns_unsupported_value_unchanged():
    value = 42

    assert wrap_var(value) is value
