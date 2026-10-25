# file: project/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafeText, wrap_var


def test_wrap_var_wraps_list_items_as_unsafe():
    value = ["first", "second"]

    result = wrap_var(value)

    assert type(result) is list
    assert result == value
    assert result is not value
    assert all(type(item) is AnsibleUnsafeText for item in result)
    assert all(type(item) is str for item in value)


def test_wrap_var_wraps_tuple_items_as_unsafe():
    value = ("first", "second")

    result = wrap_var(value)

    assert type(result) is tuple
    assert result == value
    assert result is not value
    assert all(type(item) is AnsibleUnsafeText for item in result)
    assert all(type(item) is str for item in value)
