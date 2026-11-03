# file: project/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

from ansible.utils.unsafe_proxy import (
    _wrap_sequence,
    wrap_var,
    AnsibleUnsafeText,
    AnsibleUnsafeBytes,
    NativeJinjaUnsafeText,
    AnsibleUnsafe,
)


def test_wrap_sequence_list():
    """Test _wrap_sequence with a list of strings; lines 113-114 execute."""
    result = _wrap_sequence(['a', 'b'])

    # Postconditions: result is a list, same length, each element wrapped as unsafe
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert list(result) == ['a', 'b']


def test_wrap_sequence_tuple():
    """Test _wrap_sequence with a tuple; type of result matches input type."""
    result = _wrap_sequence(('x', 'y'))

    # Postconditions: result is a tuple, elements wrapped as unsafe
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert tuple(result) == ('x', 'y')


def test_wrap_sequence_empty():
    """Test _wrap_sequence with an empty list."""
    result = _wrap_sequence([])

    # Postconditions: empty list back
    assert isinstance(result, list)
    assert len(result) == 0


def test_wrap_sequence_nested_via_wrap_var():
    """Test that wrap_var on a nested list reaches _wrap_sequence recursively."""
    result = wrap_var([{'k': 'v'}, ['nested']])

    assert isinstance(result, list)
    assert isinstance(result[0], dict)
    assert isinstance(result[1], list)
    assert isinstance(result[1][0], AnsibleUnsafeText)
