# file: project/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}

from ansible.utils import unsafe_proxy
from ansible.utils.native_jinja import NativeJinjaText


def test_wrap_var_returns_none_unchanged():
    assert unsafe_proxy.wrap_var(None) is None


def test_wrap_var_returns_existing_unsafe_value_unchanged():
    value = unsafe_proxy.AnsibleUnsafeText("already unsafe")

    assert unsafe_proxy.wrap_var(value) is value


def test_wrap_var_wraps_mapping_keys_and_values():
    value = {"key": "value"}

    result = unsafe_proxy.wrap_var(value)

    assert result is not value
    assert result == value
    key = next(iter(result))
    assert isinstance(key, unsafe_proxy.AnsibleUnsafeText)
    assert isinstance(result[key], unsafe_proxy.AnsibleUnsafeText)
    assert value == {"key": "value"}
    assert type(next(iter(value))) is str
    assert type(value["key"]) is str


def test_wrap_var_wraps_set_members():
    value = {"first", "second"}

    result = unsafe_proxy.wrap_var(value)

    assert result is not value
    assert result == value
    assert all(isinstance(item, unsafe_proxy.AnsibleUnsafeText) for item in result)
    assert all(type(item) is str for item in value)


def test_wrap_var_wraps_sequence_members_and_preserves_sequence_type():
    value = ("text", b"bytes", 42)

    result = unsafe_proxy.wrap_var(value)

    assert result is not value
    assert type(result) is tuple
    assert result == value
    assert isinstance(result[0], unsafe_proxy.AnsibleUnsafeText)
    assert isinstance(result[1], unsafe_proxy.AnsibleUnsafeBytes)
    assert result[2] is value[2]
    assert type(value[0]) is str
    assert type(value[1]) is bytes


def test_wrap_var_wraps_native_jinja_text_with_specific_unsafe_type():
    value = NativeJinjaText("native text")

    result = unsafe_proxy.wrap_var(value)

    assert result == value
    assert result is not value
    assert isinstance(result, unsafe_proxy.NativeJinjaUnsafeText)
    assert isinstance(result, NativeJinjaText)
    assert isinstance(result, unsafe_proxy.AnsibleUnsafe)


def test_wrap_var_wraps_binary_value():
    value = b"binary value"

    result = unsafe_proxy.wrap_var(value)

    assert result == value
    assert result is not value
    assert isinstance(result, unsafe_proxy.AnsibleUnsafeBytes)


def test_wrap_var_wraps_text_value():
    value = "text value"

    result = unsafe_proxy.wrap_var(value)

    assert result == value
    assert result is not value
    assert isinstance(result, unsafe_proxy.AnsibleUnsafeText)


def test_wrap_var_returns_unsupported_value_unchanged():
    value = 123

    assert unsafe_proxy.wrap_var(value) is value
