# file: project/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import _wrap_dict, wrap_var, AnsibleUnsafeText


def test_wrap_dict_wraps_string_keys_and_values():
    result = _wrap_dict({'key1': 'value1', 'key2': 'value2'})

    assert set(result.keys()) == {'key1', 'key2'}
    assert set(result.values()) == {'value1', 'value2'}
    for k, v in result.items():
        assert isinstance(k, AnsibleUnsafeText)
        assert isinstance(v, AnsibleUnsafeText)
        assert not isinstance(k, bytes)
        assert not isinstance(v, bytes)


def test_wrap_dict_mixed_types():
    original = {'a': 'text', 'b': 42, 'c': None, 'd': ['x', 'y']}
    result = _wrap_dict(original)

    # keys are wrapped strings
    assert set(result.keys()) == {'a', 'b', 'c', 'd'}
    for k in result.keys():
        assert isinstance(k, AnsibleUnsafeText)

    # string values wrapped, non-string values untouched
    assert isinstance(result['a'], AnsibleUnsafeText)
    assert result['b'] == 42
    assert result['c'] is None
    assert result['d'] == ['x', 'y']
    assert not isinstance(result['b'], AnsibleUnsafeText)


def test_wrap_dict_empty():
    assert _wrap_dict({}) == {}


def test_wrap_dict_does_not_mutate_input():
    original = {'k': 'v'}
    _wrap_dict(original)
    assert original == {'k': 'v'}
    assert not isinstance(list(original.keys())[0], AnsibleUnsafeText)
