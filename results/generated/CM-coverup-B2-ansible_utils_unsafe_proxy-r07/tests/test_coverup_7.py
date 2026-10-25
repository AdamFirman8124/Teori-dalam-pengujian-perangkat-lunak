# file: project/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    _wrap_set,
    wrap_var,
)


def test_wrap_var_with_set_wraps_strings_as_unsafe():
    original = {"alpha", "beta"}
    result = wrap_var(original)
    assert isinstance(result, set)
    assert result is not original
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert {str(item) for item in result} == {"alpha", "beta"}
    # original must be unchanged
    assert original == {"alpha", "beta"}
    assert all(type(item) is str for item in original)


def test_wrap_var_with_empty_set_covers_empty_branch():
    result = wrap_var(set())
    assert isinstance(result, set)
    assert result == set()
    assert len(result) == 0


def test_wrap_set_directly_covers_line_118():
    original = {"x", "y"}
    result = _wrap_set(original)
    assert isinstance(result, set)
    assert result is not original
    assert {str(item) for item in result} == {"x", "y"}
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)


def test_wrap_var_with_frozenset_dispatches_to_wrap_set():
    original = frozenset(["hello", "world"])
    result = wrap_var(original)
    # _wrap_set always returns a mutable set
    assert isinstance(result, set)
    assert not isinstance(result, frozenset)
    assert {str(item) for item in result} == {"hello", "world"}
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)


def test_wrap_set_mixed_types_and_already_unsafe():
    already = AnsibleUnsafeText("already")
    original = {"plain", already, 42, b"bytes"}
    result = wrap_var(original)
    assert isinstance(result, set)
    assert len(result) == 4
    # already-unsafe object is returned as-is (same object preserved)
    assert any(item is already for item in result)
    # plain string becomes unsafe text
    assert AnsibleUnsafeText("plain") in result
    # bytes become unsafe bytes
    assert AnsibleUnsafeBytes(b"bytes") in result
    # non-string scalar passes through unwrapped
    assert 42 in result
    assert any(type(item) is int for item in result)
