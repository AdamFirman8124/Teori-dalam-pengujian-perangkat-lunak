# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
)


def test_unsafe_text_encode_default():
    text = AnsibleUnsafeText(u'hello')
    result = text.encode()
    assert result == b'hello'
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, bytes)


def test_unsafe_text_encode_with_positional_encoding():
    text = AnsibleUnsafeText(u'caf\u00e9')
    result = text.encode('utf-8')
    assert result == u'caf\u00e9'.encode('utf-8')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)


def test_unsafe_text_encode_with_kwargs():
    text = AnsibleUnsafeText(u'hello')
    result = text.encode(encoding='utf-8', errors='strict')
    assert result == b'hello'
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)


def test_unsafe_text_encode_with_errors_kwarg():
    text = AnsibleUnsafeText(u'hello \udcff world')
    strict_plain = u'hello \udcff world'
    result = text.encode('utf-8', errors='ignore')
    assert result == strict_plain.encode('utf-8', errors='ignore')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
