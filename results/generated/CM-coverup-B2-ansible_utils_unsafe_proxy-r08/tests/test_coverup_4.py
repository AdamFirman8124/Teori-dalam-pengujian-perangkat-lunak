# file: project/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [73], "branches": []}
# gained: {"lines": [73], "branches": []}

# -*- coding: utf-8 -*-
# Copyright: (c) 2024, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import annotations

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText


def test_unsafe_bytes_decode_returns_unsafe_text():
    """Line 73: AnsibleUnsafeBytes.decode must wrap the result in AnsibleUnsafeText."""
    unsafe_bytes = AnsibleUnsafeBytes(b'unsafe bytes')

    result = unsafe_bytes.decode('utf-8')

    assert isinstance(result, AnsibleUnsafeText)
    assert result == u'unsafe bytes'
    assert getattr(result, '__UNSAFE__', False) is True


def test_unsafe_bytes_decode_default_args():
    """Line 73 with no explicit encoding/errors arguments."""
    unsafe_bytes = AnsibleUnsafeBytes(b'default decode')

    result = unsafe_bytes.decode()

    assert isinstance(result, AnsibleUnsafeText)
    assert result == u'default decode'
    assert getattr(result, '__UNSAFE__', False) is True


def test_unsafe_bytes_decode_kwargs():
    """Line 73 with keyword arguments passed through to bytes.decode."""
    unsafe_bytes = AnsibleUnsafeBytes(b'caf\xe9')

    result = unsafe_bytes.decode(encoding='latin-1', errors='strict')

    assert isinstance(result, AnsibleUnsafeText)
    assert result == u'caf\xe9'
    assert getattr(result, '__UNSAFE__', False) is True


def test_unsafe_bytes_decode_errors_argument():
    """Line 73 with a non-strict error handler."""
    unsafe_bytes = AnsibleUnsafeBytes(b'bad \xff byte')

    result = unsafe_bytes.decode('utf-8', 'replace')

    assert isinstance(result, AnsibleUnsafeText)
    assert result == u'bad \ufffd byte'
    assert getattr(result, '__UNSAFE__', False) is True


def test_unsafe_bytes_decode_invalid_encoding_raises():
    """Line 73 propagates decode errors from the underlying bytes.decode."""
    unsafe_bytes = AnsibleUnsafeBytes(b'\xff')

    with pytest.raises(UnicodeDecodeError):
        unsafe_bytes.decode('utf-8', 'strict')


def test_unsafe_bytes_decode_roundtrip_with_unsafe_text_encode():
    """decode() output re-encodes back into AnsibleUnsafeBytes (unsafe context kept)."""
    unsafe_bytes = AnsibleUnsafeBytes(b'roundtrip')

    text = unsafe_bytes.decode('utf-8')
    assert isinstance(text, AnsibleUnsafeText)

    back = text.encode('utf-8')
    assert isinstance(back, AnsibleUnsafeBytes)
    assert back == b'roundtrip'
    assert getattr(back, '__UNSAFE__', False) is True


def test_unsafe_bytes_decode_does_not_mutate_original():
    """Postcondition: the original AnsibleUnsafeBytes instance is unchanged."""
    original = b'immutable'
    unsafe_bytes = AnsibleUnsafeBytes(original)

    result = unsafe_bytes.decode('utf-8')

    assert unsafe_bytes == original
    assert isinstance(unsafe_bytes, AnsibleUnsafeBytes)
    assert getattr(unsafe_bytes, '__UNSAFE__', False) is True
    assert result is not unsafe_bytes
