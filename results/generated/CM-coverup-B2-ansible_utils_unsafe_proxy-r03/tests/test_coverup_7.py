# file: project/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

import pytest

import ansible.utils.unsafe_proxy as unsafe_proxy
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafeText,
    _wrap_set,
    wrap_var,
)


def test_wrap_var_on_set_wraps_each_item():
    original = {'plain', 'other'}
    result = wrap_var(original)

    assert isinstance(result, set)
    assert result is not original
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert {str(item) for item in result} == {'plain', 'other'}

    # postcondition: the input set is not mutated
    assert original == {'plain', 'other'}
    assert all(type(item) is str for item in original)


def test_wrap_var_on_empty_set():
    original = set()
    result = wrap_var(original)

    assert isinstance(result, set)
    assert result == set()
    assert result is not original
    assert original == set()


def test_wrap_var_on_set_keeps_already_unsafe_items():
    unsafe_item = AnsibleUnsafeText('already-unsafe')
    original = {unsafe_item}
    result = wrap_var(original)

    assert isinstance(result, set)
    assert len(result) == 1
    (item,) = result
    assert isinstance(item, AnsibleUnsafeText)
    assert item == 'already-unsafe'
    assert item is unsafe_item

    # postcondition: original set untouched
    assert original == {unsafe_item}


def test_wrap_var_on_set_is_idempotent():
    once = wrap_var({'value'})
    twice = wrap_var(once)

    assert isinstance(twice, set)
    assert twice == once
    assert all(isinstance(item, AnsibleUnsafeText) for item in twice)


def test_wrap_set_calls_wrap_var_for_each_item(monkeypatch):
    calls = []

    def fake_wrap_var(item):
        calls.append(item)
        return 'wrapped-%s' % item

    monkeypatch.setattr(unsafe_proxy, 'wrap_var', fake_wrap_var)
    assert unsafe_proxy.wrap_var is fake_wrap_var

    result = _wrap_set({'x', 'y'})

    assert isinstance(result, set)
    assert result == {'wrapped-x', 'wrapped-y'}
    assert sorted(calls) == ['x', 'y']

    # cleanup + postcondition: monkeypatch restores the real wrap_var
    monkeypatch.undo()
    assert unsafe_proxy.wrap_var is wrap_var
