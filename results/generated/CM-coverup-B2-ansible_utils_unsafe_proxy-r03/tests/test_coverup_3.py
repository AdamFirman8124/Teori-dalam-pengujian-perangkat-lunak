# file: project/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import _wrap_sequence, AnsibleUnsafeText, AnsibleUnsafeBytes


def test_wrap_sequence_list():
    result = _wrap_sequence(['a', 'b'])
    assert isinstance(result, list)
    assert len(result) == 2
    for item in result:
        assert isinstance(item, AnsibleUnsafeText)
        assert not isinstance(item, AnsibleUnsafeBytes)
    assert result[0] == 'a'
    assert result[1] == 'b'


def test_wrap_sequence_tuple():
    result = _wrap_sequence(('x', 'y'))
    assert isinstance(result, tuple)
    assert len(result) == 2
    for item in result:
        assert isinstance(item, AnsibleUnsafeText)
    assert result == ('x', 'y')


def test_wrap_sequence_bytes():
    result = _wrap_sequence([b'a', b'b'])
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, AnsibleUnsafeBytes)
        assert not isinstance(item, AnsibleUnsafeText)
    assert result[0] == b'a'


def test_wrap_sequence_empty_list():
    result = _wrap_sequence([])
    assert result == []
    assert isinstance(result, list)


def test_wrap_sequence_nested():
    result = _wrap_sequence([['a'], 'b'])
    assert isinstance(result, list)
    assert isinstance(result[0], list)
    assert isinstance(result[0][0], AnsibleUnsafeText)
    assert isinstance(result[1], AnsibleUnsafeText)
