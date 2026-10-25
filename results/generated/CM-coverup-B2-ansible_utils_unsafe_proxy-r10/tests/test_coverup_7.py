# file: project/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafeText, wrap_var


def test_wrap_var_wraps_items_in_set():
    original = {"value"}

    result = wrap_var(original)

    assert result == {"value"}
    assert result is not original
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert original == {"value"}
    assert all(type(item) is str for item in original)
