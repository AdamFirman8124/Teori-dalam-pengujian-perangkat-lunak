# file: project/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafeText,
    wrap_var,
)


def test_wrap_var_wraps_dictionary_keys_and_values():
    source = {"key": "value"}

    result = wrap_var(source)

    assert result is not source
    assert len(result) == 1

    key, value = next(iter(result.items()))
    assert type(key) is AnsibleUnsafeText
    assert type(value) is AnsibleUnsafeText
    assert key == "key"
    assert value == "value"

    assert type(next(iter(source))) is str
    assert type(source["key"]) is str
