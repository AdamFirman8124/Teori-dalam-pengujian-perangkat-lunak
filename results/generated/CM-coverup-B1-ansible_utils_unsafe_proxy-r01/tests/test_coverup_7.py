# file: project/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    wrap_var,
)


def test_wrap_var_set_of_text_is_marked_unsafe():
    original = {"alpha", "beta"}
    result = wrap_var(original)

    assert isinstance(result, set)
    assert result == original
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert all(getattr(item, "__UNSAFE__", False) is True for item in result)
    assert not any(isinstance(item, AnsibleUnsafe) for item in original)


def test_wrap_var_set_of_bytes_is_marked_unsafe():
    original = {b"alpha", b"beta"}
    result = wrap_var(original)

    assert isinstance(result, set)
    assert result == original
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafeBytes) for item in result)
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert all(getattr(item, "__UNSAFE__", False) is True for item in result)
    assert not any(isinstance(item, AnsibleUnsafe) for item in original)


def test_wrap_var_empty_set():
    result = wrap_var(set())

    assert isinstance(result, set)
    assert result == set()
    assert len(result) == 0


def test_wrap_var_mixed_hashable_set_preserves_non_string_values():
    original = {"text", b"bytes", 42}
    result = wrap_var(original)

    assert isinstance(result, set)
    assert result == original
    text_item = next(item for item in result if item == "text")
    bytes_item = next(item for item in result if item == b"bytes")
    int_item = next(item for item in result if item == 42)
    assert isinstance(text_item, AnsibleUnsafeText)
    assert isinstance(bytes_item, AnsibleUnsafeBytes)
    assert type(int_item) is int


def test_wrap_var_set_nested_in_dict_and_list():
    dict_result = wrap_var({"key": {"nested"}})
    list_result = wrap_var([{"listed"}])

    assert isinstance(dict_result, dict)
    dict_value = next(iter(dict_result.values()))
    assert isinstance(dict_value, set)
    assert dict_value == {"nested"}
    assert all(isinstance(item, AnsibleUnsafeText) for item in dict_value)

    assert isinstance(list_result, list)
    assert isinstance(list_result[0], set)
    assert list_result[0] == {"listed"}
    assert all(isinstance(item, AnsibleUnsafeText) for item in list_result[0])
