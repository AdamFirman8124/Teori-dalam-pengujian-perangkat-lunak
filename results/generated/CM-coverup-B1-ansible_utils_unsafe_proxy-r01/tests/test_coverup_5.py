# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes


def test_unsafe_text_encode_returns_unsafe_bytes():
    unsafe_text = AnsibleUnsafeText(u'unsafe value')

    result = unsafe_text.encode()

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, bytes)
    assert result == b'unsafe value'
    assert result.__UNSAFE__ is True
    assert getattr(result, '__UNSAFE__', False) is True


def test_unsafe_text_encode_passes_args_and_kwargs():
    unsafe_text = AnsibleUnsafeText(u'caf\u00e9')

    result = unsafe_text.encode('utf-8', 'strict')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == u'caf\u00e9'.encode('utf-8')
    assert result.__UNSAFE__ is True

    result_kwargs = unsafe_text.encode(encoding='utf-8', errors='replace')

    assert isinstance(result_kwargs, AnsibleUnsafeBytes)
    assert result_kwargs == u'caf\u00e9'.encode('utf-8')
    assert result_kwargs.__UNSAFE__ is True


def test_unsafe_text_encode_error_propagates():
    unsafe_text = AnsibleUnsafeText(u'caf\u00e9')

    with pytest.raises(UnicodeEncodeError):
        unsafe_text.encode('ascii', 'strict')


def test_unsafe_text_encode_does_not_mutate_original():
    unsafe_text = AnsibleUnsafeText(u'plain')

    result = unsafe_text.encode()

    assert unsafe_text == u'plain'
    assert isinstance(unsafe_text, AnsibleUnsafeText)
    assert unsafe_text.__UNSAFE__ is True
    assert result is not unsafe_text
