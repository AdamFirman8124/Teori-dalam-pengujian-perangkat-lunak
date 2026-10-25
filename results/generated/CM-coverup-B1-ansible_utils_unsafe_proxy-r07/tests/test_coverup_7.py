# file: project/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

import pytest

from ansible.utils import unsafe_proxy
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    _wrap_set,
    wrap_var,
)


def test_wrap_var_set_wraps_every_item():
    original = {'alpha', 'beta'}
    result = wrap_var(original)

    assert isinstance(result, set)
    assert result is not original
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert {str(item) for item in result} == {'alpha', 'beta'}

    # the input set must not be mutated
    assert original == {'alpha', 'beta'}
    assert all(type(item) is str for item in original)


def test_wrap_var_empty_set():
    original = set()
    result = wrap_var(original)

    assert isinstance(result, set)
    assert result is not original
    assert result == set()


def test_wrap_var_set_of_bytes():
    result = wrap_var({b'one', b'two'})

    assert isinstance(result, set)
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafeBytes) for item in result)
    assert {bytes(item) for item in result} == {b'one', b'two'}


def test_wrap_var_set_preserves_already_unsafe_items():
    unsafe_a = AnsibleUnsafeText('a')
    unsafe_b = AnsibleUnsafeText('b')
    original = {unsafe_a, unsafe_b}

    result = wrap_var(original)

    assert isinstance(result, set)
    assert result is not original
    assert result == original
    # already-unsafe items are returned unchanged (same objects)
    assert any(item is unsafe_a for item in result)
    assert any(item is unsafe_b for item in result)


def test_wrap_var_set_is_idempotent():
    once = wrap_var({'x', 'y'})
    twice = wrap_var(once)

    assert isinstance(twice, set)
    assert twice == once
    assert all(isinstance(item, AnsibleUnsafeText) for item in twice)


def test_wrap_var_set_with_nested_sequence():
    result = wrap_var({('a', 'b')})

    assert isinstance(result, set)
    assert len(result) == 1
    (inner,) = result
    # _wrap_sequence may return a list or tuple; accept either
    assert len(inner) == 2
    assert all(isinstance(item, AnsibleUnsafe) for item in inner)
    assert [str(item) for item in inner] == ['a', 'b']


def test_wrap_set_calls_wrap_var_for_each_item(monkeypatch):
    calls = []
    real_wrap_var = unsafe_proxy.wrap_var

    def spy(item):
        calls.append(item)
        return real_wrap_var(item)

    monkeypatch.setattr(unsafe_proxy, 'wrap_var', spy)

    result = _wrap_set({'x', 'y'})

    # the spy was actually used for every item
    assert sorted(calls) == ['x', 'y']
    assert isinstance(result, set)
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert {str(item) for item in result} == {'x', 'y'}


def test_wrap_set_returns_plain_set_not_generator():
    result = _wrap_set({'only'})

    assert type(result) is set
    assert len(result) == 1
    (item,) = result
    assert isinstance(item, AnsibleUnsafeText)
    assert str(item) == 'only'
