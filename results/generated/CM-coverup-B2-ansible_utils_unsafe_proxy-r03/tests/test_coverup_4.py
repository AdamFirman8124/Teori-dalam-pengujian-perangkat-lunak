# file: project/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [73], "branches": []}
# gained: {"lines": [73], "branches": []}

"""Tests for ansible.utils.unsafe_proxy.AnsibleUnsafeBytes.decode (line 73).

These tests are pure (no global state is touched, no files, no env vars),
so no monkeypatching/cleanup is required; nothing leaks between tests.
"""

import pytest

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    wrap_var,
)


def test_ansible_unsafe_bytes_decode_returns_unsafe_text():
    """AnsibleUnsafeBytes.decode must return an AnsibleUnsafeText (line 73)."""
    unsafe_bytes = AnsibleUnsafeBytes(b"hello world")
    result = unsafe_bytes.decode()

    # Line 73 executed: result is the wrapped decode output.
    assert isinstance(result, AnsibleUnsafeText)
    assert not isinstance(result, AnsibleUnsafeBytes)
    # The decoded content is preserved.
    assert result == "hello world"
    # The unsafe context is maintained through the conversion.
    assert isinstance(result, AnsibleUnsafe)
    assert result.__UNSAFE__ is True


def test_ansible_unsafe_bytes_decode_forwards_args_and_kwargs():
    """decode(*args, **kwargs) must forward arguments to bytes.decode."""
    unsafe_bytes = AnsibleUnsafeBytes(b"caf\xc3\xa9")
    result = unsafe_bytes.decode("utf-8", errors="strict")

    assert isinstance(result, AnsibleUnsafeText)
    assert result == "caf\xe9"
    assert result.__UNSAFE__ is True


def test_ansible_unsafe_bytes_decode_via_wrap_var():
    """wrap_var() on bytes yields AnsibleUnsafeBytes whose decode stays unsafe."""
    unsafe_bytes = wrap_var(b"wrapped")
    assert isinstance(unsafe_bytes, AnsibleUnsafeBytes)

    result = unsafe_bytes.decode()
    assert isinstance(result, AnsibleUnsafeText)
    assert result == "wrapped"
    assert result.__UNSAFE__ is True


def test_ansible_unsafe_bytes_decode_error_propagates():
    """decode must propagate errors raised by the underlying bytes.decode."""
    unsafe_bytes = AnsibleUnsafeBytes(b"\xff\xfe\xfd")

    with pytest.raises(UnicodeDecodeError):
        unsafe_bytes.decode("ascii")
