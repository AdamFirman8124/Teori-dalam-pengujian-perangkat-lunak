# file: project/ansible/utils/unsafe_proxy.py:105-106
# asked: {"lines": [106], "branches": []}
# gained: {"lines": [106], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafeText,
    AnsibleUnsafeBytes,
    wrap_var,
)


def test_wrap_dict_wraps_keys_and_values():
    """Line 106: _wrap_dict wraps both keys and values of a plain dict."""
    original = {'key': 'value'}
    result = wrap_var(original)

    assert isinstance(result, dict)
    assert len(result) == 1

    (key, value), = result.items()
    assert isinstance(key, AnsibleUnsafeText)
    assert isinstance(value, AnsibleUnsafeText)
    assert key == 'key'
    assert value == 'value'

    # Lookup by the original (unsafe-free) key still works.
    assert result['key'] == 'value'

    # The input dict must not be mutated.
    assert original == {'key': 'value'}
    assert type(next(iter(original.keys()))) is str
    assert type(next(iter(original.values()))) is str


def test_wrap_dict_multiple_items_and_mixed_types():
    """Line 106 with several items and non-string values left untouched."""
    original = {'a': 'b', 'c': 1, 'd': None}
    result = wrap_var(original)

    assert len(result) == 3
    for key in result:
        assert isinstance(key, AnsibleUnsafeText)

    assert isinstance(result['a'], AnsibleUnsafeText)
    assert result['a'] == 'b'
    assert result['c'] == 1
    assert type(result['c']) is int
    assert result['d'] is None

    # Original untouched.
    assert original == {'a': 'b', 'c': 1, 'd': None}


def test_wrap_dict_empty():
    """Line 106 executes with an empty generator."""
    original = {}
    result = wrap_var(original)

    assert result == {}
    assert isinstance(result, dict)
    assert original == {}


def test_wrap_dict_nested():
    """Line 106 recurses into nested dicts and sequences."""
    original = {'outer': {'inner': 'value'}, 'seq': ['x']}
    result = wrap_var(original)

    assert isinstance(result, dict)
    outer_key = next(k for k in result if k == 'outer')
    assert isinstance(outer_key, AnsibleUnsafeText)

    inner = result['outer']
    assert isinstance(inner, dict)
    inner_key = next(k for k in inner if k == 'inner')
    assert isinstance(inner_key, AnsibleUnsafeText)
    assert isinstance(inner['inner'], AnsibleUnsafeText)
    assert inner['inner'] == 'value'

    seq = result['seq']
    assert isinstance(seq, list)
    assert isinstance(seq[0], AnsibleUnsafeText)
    assert seq[0] == 'x'

    # Original structure untouched.
    assert original == {'outer': {'inner': 'value'}, 'seq': ['x']}
    assert type(original['outer']['inner']) is str


def test_wrap_dict_bytes_keys_and_values():
    """Line 106 wraps binary keys/values as AnsibleUnsafeBytes."""
    original = {b'k': b'v'}
    result = wrap_var(original)

    assert len(result) == 1
    (key, value), = result.items()
    assert isinstance(key, AnsibleUnsafeBytes)
    assert isinstance(value, AnsibleUnsafeBytes)
    assert key == b'k'
    assert value == b'v'

    assert original == {b'k': b'v'}
    assert type(next(iter(original.keys()))) is bytes


def test_wrap_dict_does_not_mutate_and_is_idempotent():
    """Wrapping an already-wrapped dict keeps values unsafe and equal."""
    original = {'k': 'v'}
    once = wrap_var(original)
    twice = wrap_var(once)

    assert twice == once
    assert isinstance(twice['k'], AnsibleUnsafeText)
    assert twice['k'] == 'v'
    assert original == {'k': 'v'}
