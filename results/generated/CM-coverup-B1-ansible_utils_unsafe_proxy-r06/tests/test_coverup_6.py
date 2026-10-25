# file: project/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafeText, wrap_var


def test_wrap_var_wraps_dictionary_keys_and_values():
    original = {"key": "value"}

    wrapped = wrap_var(original)

    assert wrapped == original
    assert wrapped is not original

    wrapped_key = next(iter(wrapped))
    assert isinstance(wrapped_key, AnsibleUnsafeText)
    assert isinstance(wrapped[wrapped_key], AnsibleUnsafeText)

    assert type(next(iter(original))) is str
    assert type(original["key"]) is str
