# file: project/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import _wrap_dict, wrap_var, AnsibleUnsafeText


def test_wrap_dict_wraps_keys_and_values():
    """Line 106: _wrap_dict must wrap both keys and values of the dict."""
    source = {'key1': 'value1', 'key2': 'value2'}

    result = _wrap_dict(source)

    # The result is a plain dict with the same number of entries
    assert isinstance(result, dict)
    assert len(result) == 2

    # Every key and value was passed through wrap_var, producing
    # AnsibleUnsafeText instances with the original content preserved
    for orig_key, orig_value in source.items():
        wrapped_keys = [k for k in result.keys() if k == orig_key]
        assert len(wrapped_keys) == 1
        wrapped_key = wrapped_keys[0]
        assert isinstance(wrapped_key, AnsibleUnsafeText)
        assert wrapped_key == orig_key

        wrapped_value = result[wrapped_key]
        assert isinstance(wrapped_value, AnsibleUnsafeText)
        assert wrapped_value == orig_value


def test_wrap_dict_empty():
    """An empty dict yields an empty dict without errors."""
    result = _wrap_dict({})
    assert result == {}
    assert isinstance(result, dict)


def test_wrap_dict_does_not_mutate_input():
    """The source dict must be left untouched (no state pollution)."""
    source = {'a': 'b'}
    snapshot = dict(source)

    _wrap_dict(source)

    assert source == snapshot
    assert all(not isinstance(k, AnsibleUnsafeText) for k in source.keys())
    assert all(not isinstance(v, AnsibleUnsafeText) for v in source.values())
