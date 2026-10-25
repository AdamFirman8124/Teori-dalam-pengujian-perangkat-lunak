# file: project/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}

import pytest

from ansible.utils import unsafe_proxy
from ansible.utils.native_jinja import NativeJinjaText


def test_wrap_var_returns_none_unchanged():
    assert unsafe_proxy.wrap_var(None) is None


def test_wrap_var_returns_existing_unsafe_value_unchanged():
    value = unsafe_proxy.AnsibleUnsafeText("already unsafe")

    assert unsafe_proxy.wrap_var(value) is value


def test_wrap_var_wraps_mapping_keys_and_values():
    result = unsafe_proxy.wrap_var({"key": "value"})

    assert type(result) is dict
    [(key, value)] = result.items()
    assert type(key) is unsafe_proxy.AnsibleUnsafeText
    assert type(value) is unsafe_proxy.AnsibleUnsafeText
    assert key == "key"
    assert value == "value"


def test_wrap_var_wraps_set_items():
    result = unsafe_proxy.wrap_var({"first", "second"})

    assert type(result) is set
    assert result == {"first", "second"}
    assert all(type(item) is unsafe_proxy.AnsibleUnsafeText for item in result)


@pytest.mark.parametrize("value", [["item"], ("item",)])
def test_wrap_var_wraps_sequence_items_and_preserves_type(value):
    result = unsafe_proxy.wrap_var(value)

    assert type(result) is type(value)
    assert result == value
    assert type(result[0]) is unsafe_proxy.AnsibleUnsafeText


def test_wrap_var_wraps_native_jinja_text():
    value = NativeJinjaText("native")

    result = unsafe_proxy.wrap_var(value)

    assert type(result) is unsafe_proxy.NativeJinjaUnsafeText
    assert result == value


def test_wrap_var_wraps_bytes():
    value = b"bytes"

    result = unsafe_proxy.wrap_var(value)

    assert type(result) is unsafe_proxy.AnsibleUnsafeBytes
    assert result == value


def test_wrap_var_wraps_text():
    value = "text"

    result = unsafe_proxy.wrap_var(value)

    assert type(result) is unsafe_proxy.AnsibleUnsafeText
    assert result == value


def test_wrap_var_returns_unsupported_value_unchanged():
    value = object()

    assert unsafe_proxy.wrap_var(value) is value
