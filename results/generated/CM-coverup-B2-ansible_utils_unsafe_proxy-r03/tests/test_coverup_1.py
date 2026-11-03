# file: project/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.six import binary_type, text_type
from ansible.utils.native_jinja import NativeJinjaText
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    NativeJinjaUnsafeText,
    wrap_var,
)


def _assert_unsafe(obj):
    """Verify obj was wrapped: it is an instance of AnsibleUnsafe and
    carries the ``__UNSAFE__`` marker."""
    assert isinstance(obj, AnsibleUnsafe)
    assert obj.__UNSAFE__ is True


def test_wrap_var_none_is_returned_as_is():
    # Covers line 122 -> 123 (the None branch, early return)
    assert wrap_var(None) is None


def test_wrap_var_already_unsafe_is_returned_as_is():
    # Covers line 122 -> 123 (the isinstance(v, AnsibleUnsafe) branch, early return)
    already_unsafe = AnsibleUnsafeText(u'do not touch')
    result = wrap_var(already_unsafe)
    assert result is already_unsafe
    _assert_unsafe(result)


def test_wrap_var_mapping():
    # Covers lines 125 -> 126 (_wrap_dict), including recursion into values.
    # Note: only leaf values (and keys) are wrapped; nested containers are
    # recursed into but the container objects themselves are not AnsibleUnsafe.
    value = {u'k1': u'v1', u'k2': b'v2', u'k3': {u'nested': u'value'}}
    result = wrap_var(value)

    assert isinstance(result, dict)
    assert result == value
    for key, item in result.items():
        _assert_unsafe(key)
        if isinstance(item, dict):
            # nested dict: keys and leaf values are wrapped recursively
            for nested_key, nested_item in item.items():
                _assert_unsafe(nested_key)
                _assert_unsafe(nested_item)
        else:
            _assert_unsafe(item)

    # nested dict values are wrapped recursively
    _assert_unsafe(result[u'k3'][u'nested'])
    assert isinstance(result[u'k3'][u'nested'], AnsibleUnsafeText)
    assert isinstance(result[u'k2'], AnsibleUnsafeBytes)
    assert isinstance(result[u'k1'], AnsibleUnsafeText)


def test_wrap_var_set():
    # Covers lines 127 -> 128 (_wrap_set)
    value = {u'item1', u'item2'}
    result = wrap_var(value)

    assert isinstance(result, set)
    assert result == value
    for item in result:
        _assert_unsafe(item)
        assert isinstance(item, AnsibleUnsafeText)


def test_wrap_var_list_sequence():
    # Covers lines 129 -> 130 (_wrap_sequence) for list
    value = [u'one', b'two']
    result = wrap_var(value)

    assert isinstance(result, list)
    assert result == value
    _assert_unsafe(result[0])
    _assert_unsafe(result[1])
    assert isinstance(result[0], AnsibleUnsafeText)
    assert isinstance(result[1], AnsibleUnsafeBytes)


def test_wrap_var_tuple_sequence():
    # Covers lines 129 -> 130 again; _wrap_sequence preserves the concrete type
    value = (u'one', b'two')
    result = wrap_var(value)

    assert isinstance(result, tuple)
    assert result == value
    _assert_unsafe(result[0])
    _assert_unsafe(result[1])


def test_wrap_var_native_jinja_text():
    # Covers lines 131 -> 132 (NativeJinjaText branch).
    # NativeJinjaText subclasses text_type, so this must be reached before
    # the plain text_type branch and must not take the sequence branch.
    value = NativeJinjaText(u'template output')
    result = wrap_var(value)

    assert isinstance(result, NativeJinjaUnsafeText)
    assert isinstance(result, NativeJinjaText)
    assert isinstance(result, AnsibleUnsafeText)
    _assert_unsafe(result)
    assert result == u'template output'


def test_wrap_var_binary():
    # Covers lines 133 -> 134 (binary_type branch)
    value = b'binary value'
    result = wrap_var(value)

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, binary_type)
    _assert_unsafe(result)
    assert result == b'binary value'


def test_wrap_var_text():
    # Covers lines 135 -> 136 (text_type branch)
    value = u'text value'
    result = wrap_var(value)

    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, text_type)
    _assert_unsafe(result)
    assert result == u'text value'


def test_wrap_var_unsupported_type_falls_through_to_return():
    # Ensures the fall-through path reaching the final ``return v`` (line 138)
    # for types matching no branch leaves the value untouched
    value = 42
    assert wrap_var(value) is value
    assert wrap_var(3.14) == 3.14


def test_wrap_var_empty_containers():
    # Exercise the container branches with empty values (no infinite recursion,
    # results are new, equivalent containers)
    empty_list = wrap_var([])
    empty_dict = wrap_var({})
    empty_set = wrap_var(set())

    assert empty_list == []
    assert empty_dict == {}
    assert empty_set == set()

    assert empty_list is not None
    assert empty_dict is not None
    assert empty_set is not None
