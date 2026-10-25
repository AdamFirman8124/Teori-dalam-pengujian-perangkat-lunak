# file: project/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import _wrap_set, wrap_var, AnsibleUnsafeText, AnsibleUnsafeBytes


def test_wrap_set_wraps_string_elements():
    """_wrap_set must wrap each string element of the input set (line 118)."""
    result = _wrap_set({u'foo', b'bar'})

    assert isinstance(result, set)
    assert len(result) == 2
    # Each string element is converted to its unsafe counterpart
    assert u'foo' in result
    assert b'bar' in result
    assert any(isinstance(item, AnsibleUnsafeText) for item in result)
    assert any(isinstance(item, AnsibleUnsafeBytes) for item in result)
    # Consistency with wrap_var applied directly
    assert result == {wrap_var(u'foo'), wrap_var(b'bar')}


def test_wrap_set_empty():
    """An empty set yields an empty set, still exercising line 118."""
    result = _wrap_set(set())
    assert result == set()


def test_wrap_set_non_string_elements_pass_through():
    """Non-string elements are returned unchanged, matching wrap_var behavior."""
    sentinel = object()
    result = _wrap_set({1, None, sentinel})

    assert result == {1, None, sentinel}
    assert sentinel in result
