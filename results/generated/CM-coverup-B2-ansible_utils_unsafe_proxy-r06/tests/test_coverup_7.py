# file: project/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeText,
    _wrap_set,
    wrap_var,
)


def test_wrap_set_empty():
    original = set()
    result = _wrap_set(original)
    assert result == set()
    assert isinstance(result, set)
    assert result is not original


def test_wrap_set_with_strings():
    result = _wrap_set({"foo", "bar"})
    assert isinstance(result, set)
    assert len(result) == 2
    for item in result:
        assert isinstance(item, AnsibleUnsafe)
        assert isinstance(item, AnsibleUnsafeText)
    assert set(str(i) for i in result) == {"foo", "bar"}


def test_wrap_set_with_mixed_hashable_types():
    result = _wrap_set({"hello", 42, (1, 2)})
    assert isinstance(result, set)
    assert len(result) == 3
    # string element is wrapped as unsafe
    assert any(isinstance(i, AnsibleUnsafeText) and str(i) == "hello" for i in result)
    # non-string hashables pass through unchanged
    assert 42 in result
    assert (1, 2) in result


def test_wrap_var_dispatches_to_wrap_set():
    original = {"a", "b", 1}
    result = wrap_var(original)
    assert isinstance(result, set)
    assert result is not original
    assert len(result) == 3
    assert 1 in result
    texts = [i for i in result if isinstance(i, str)]
    assert len(texts) == 2
    for t in texts:
        assert isinstance(t, AnsibleUnsafe)
    assert {str(t) for t in texts} == {"a", "b"}


def test_wrap_var_with_frozenset_goes_through_wrap_set():
    result = wrap_var(frozenset(["x", "y"]))
    assert isinstance(result, set)
    assert len(result) == 2
    for item in result:
        assert isinstance(item, AnsibleUnsafe)
    assert {str(i) for i in result} == {"x", "y"}
