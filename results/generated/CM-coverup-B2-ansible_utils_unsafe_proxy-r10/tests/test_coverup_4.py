# file: project/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [73], "branches": []}
# gained: {"lines": [73], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafe
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes
from ansible.utils.unsafe_proxy import AnsibleUnsafeText


def test_ansible_unsafe_bytes_decode_default():
    value = AnsibleUnsafeBytes(b'hello world')
    result = value.decode()
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert getattr(result, '__UNSAFE__') is True
    assert result == 'hello world'
    assert type(result) is AnsibleUnsafeText
    # original is unchanged
    assert isinstance(value, AnsibleUnsafeBytes)
    assert value == b'hello world'


def test_ansible_unsafe_bytes_decode_with_encoding_arg():
    value = AnsibleUnsafeBytes('héllo'.encode('utf-8'))
    result = value.decode('utf-8')
    assert isinstance(result, AnsibleUnsafeText)
    assert getattr(result, '__UNSAFE__') is True
    assert result == 'héllo'


def test_ansible_unsafe_bytes_decode_with_encoding_and_errors_kwargs():
    value = AnsibleUnsafeBytes(b'caf\xc3\xa9')
    result = value.decode(*('utf-8',), **{'errors': 'strict'})
    assert isinstance(result, AnsibleUnsafeText)
    assert getattr(result, '__UNSAFE__') is True
    assert result == 'café'
    # errors handling path still preserves unsafe context
    result_replace = AnsibleUnsafeBytes(b'caf\xff').decode('utf-8', errors='replace')
    assert isinstance(result_replace, AnsibleUnsafeText)
    assert getattr(result_replace, '__UNSAFE__') is True
    assert 'caf' in result_replace
