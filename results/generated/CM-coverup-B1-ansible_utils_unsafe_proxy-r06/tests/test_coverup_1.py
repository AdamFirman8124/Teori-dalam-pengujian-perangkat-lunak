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

    result = unsafe_proxy.wrap_var(value)

    assert result is value


def test_wrap_var_wraps_mapping_keys_and_values():
    value = {"key": "value"}

    result = unsafe_proxy.wrap_var(value)

    assert isinstance(result, dict)
    assert result == value
    assert result is not value

    (wrapped_key, wrapped_value), = result.items()
    assert isinstance(wrapped_key, unsafe_proxy.AnsibleUnsafeText)
    assert isinstance(wrapped_value, unsafe_proxy.AnsibleUnsafeText)


def test_wrap_var_wraps_set_items():
    value = {"first", "second"}

    result = unsafe_proxy.wrap_var(value)

    assert isinstance(result, set)
    assert result == value
    assert result is not value
    assert all(
        isinstance(item, unsafe_proxy.AnsibleUnsafeText)
        for item in result
    )


@pytest.mark.parametrize("sequence_type", [list, tuple])
def test_wrap_var_wraps_sequence_items_and_preserves_type(sequence_type):
    value = sequence_type(("first", "second"))

    result = unsafe_proxy.wrap_var(value)

    assert type(result) is sequence_type
    assert result == value
    assert result is not value
    assert all(
        isinstance(item, unsafe_proxy.AnsibleUnsafeText)
        for item in result
    )


def test_wrap_var_wraps_native_jinja_text():
    value = NativeJinjaText("native text")

    result = unsafe_proxy.wrap_var(value)

    assert type(result) is unsafe_proxy.NativeJinjaUnsafeText
    assert result == value
    assert result is not value
    assert isinstance(result, NativeJinjaText)
    assert isinstance(result, unsafe_proxy.AnsibleUnsafe)


def test_wrap_var_wraps_binary_value():
    value = b"binary value"

    result = unsafe_proxy.wrap_var(value)

    assert type(result) is unsafe_proxy.AnsibleUnsafeBytes
    assert result == value
    assert result is not value
    assert isinstance(result, unsafe_proxy.AnsibleUnsafe)


def test_wrap_var_wraps_text_value():
    value = "text value"

    result = unsafe_proxy.wrap_var(value)

    assert type(result) is unsafe_proxy.AnsibleUnsafeText
    assert result == value
    assert result is not value
    assert isinstance(result, unsafe_proxy.AnsibleUnsafe)


def test_wrap_var_returns_unsupported_value_unchanged():
    value = object()

    result = unsafe_proxy.wrap_var(value)

    assert result is value
