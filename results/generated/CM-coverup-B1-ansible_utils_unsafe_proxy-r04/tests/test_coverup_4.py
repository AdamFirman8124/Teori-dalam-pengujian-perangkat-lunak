# file: project/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [73], "branches": []}
# gained: {"lines": [73], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeBytes, AnsibleUnsafeText


def test_unsafe_bytes_decode_default():
    value = AnsibleUnsafeBytes(b'hello world')
    result = value.decode()
    assert result == 'hello world'
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert getattr(result, '__UNSAFE__') is True
    assert type(result) is AnsibleUnsafeText


def test_unsafe_bytes_decode_with_positional_encoding_arg():
    value = AnsibleUnsafeBytes('héllo'.encode('utf-8'))
    result = value.decode('utf-8')
    assert result == 'héllo'
    assert isinstance(result, AnsibleUnsafeText)
    assert getattr(result, '__UNSAFE__') is True


def test_unsafe_bytes_decode_with_kwargs():
    value = AnsibleUnsafeBytes(b'hello')
    result = value.decode(encoding='utf-8', errors='strict')
    assert result == 'hello'
    assert isinstance(result, AnsibleUnsafeText)
    assert getattr(result, '__UNSAFE__') is True


def test_unsafe_bytes_decode_errors_kwarg():
    value = AnsibleUnsafeBytes(b'\xff\xfehello')
    result = value.decode('utf-8', errors='ignore')
    assert result == 'hello'
    assert isinstance(result, AnsibleUnsafeText)
    assert getattr(result, '__UNSAFE__') is True
