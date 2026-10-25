# file: project/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}

from ansible.utils.native_jinja import NativeJinjaText
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    NativeJinjaUnsafeText,
    wrap_var,
)


def test_wrap_var_returns_none_unchanged():
    assert wrap_var(None) is None


def test_wrap_var_returns_existing_unsafe_value_unchanged():
    value = AnsibleUnsafeText("already unsafe")

    result = wrap_var(value)

    assert result is value
    assert isinstance(result, AnsibleUnsafe)


def test_wrap_var_wraps_mapping_keys_and_values():
    value = {"key": "value"}

    result = wrap_var(value)

    assert type(result) is dict
    assert len(result) == 1

    key = next(iter(result))
    assert type(key) is AnsibleUnsafeText
    assert key == "key"
    assert type(result[key]) is AnsibleUnsafeText
    assert result[key] == "value"


def test_wrap_var_wraps_set_elements():
    value = {"element"}

    result = wrap_var(value)

    assert type(result) is set
    assert len(result) == 1

    element = next(iter(result))
    assert type(element) is AnsibleUnsafeText
    assert element == "element"


def test_wrap_var_wraps_sequence_and_preserves_its_type():
    value = ["first", b"second"]

    result = wrap_var(value)

    assert type(result) is list
    assert type(result[0]) is AnsibleUnsafeText
    assert result[0] == "first"
    assert type(result[1]) is AnsibleUnsafeBytes
    assert result[1] == b"second"


def test_wrap_var_wraps_native_jinja_text():
    value = NativeJinjaText("native text")

    result = wrap_var(value)

    assert type(result) is NativeJinjaUnsafeText
    assert result == "native text"
    assert isinstance(result, AnsibleUnsafe)


def test_wrap_var_wraps_bytes():
    value = b"bytes"

    result = wrap_var(value)

    assert type(result) is AnsibleUnsafeBytes
    assert result == value
    assert isinstance(result, AnsibleUnsafe)


def test_wrap_var_wraps_text():
    value = "text"

    result = wrap_var(value)

    assert type(result) is AnsibleUnsafeText
    assert result == value
    assert isinstance(result, AnsibleUnsafe)


def test_wrap_var_returns_unsupported_value_unchanged():
    value = object()

    result = wrap_var(value)

    assert result is value
