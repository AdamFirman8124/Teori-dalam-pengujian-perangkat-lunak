# file: project/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [73], "branches": []}
# gained: {"lines": [73], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeBytes, AnsibleUnsafeText


def test_ansible_unsafe_bytes_decode_default():
    unsafe_bytes = AnsibleUnsafeBytes(b'hello world')
    result = unsafe_bytes.decode()
    assert result == 'hello world'
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, str)
    assert getattr(result, '__UNSAFE__', False) is True
    assert isinstance(result, AnsibleUnsafe)


def test_ansible_unsafe_bytes_decode_with_positional_encoding():
    unsafe_bytes = AnsibleUnsafeBytes('héllo'.encode('utf-8'))
    result = unsafe_bytes.decode('utf-8')
    assert result == 'héllo'
    assert isinstance(result, AnsibleUnsafeText)
    assert getattr(result, '__UNSAFE__', False) is True


def test_ansible_unsafe_bytes_decode_with_kwargs():
    unsafe_bytes = AnsibleUnsafeBytes(b'\xff\xfehello\xff')
    result = unsafe_bytes.decode(encoding='utf-8', errors='ignore')
    assert isinstance(result, AnsibleUnsafeText)
    assert getattr(result, '__UNSAFE__', False) is True
    assert 'hello' in result
    # original object is unchanged and still unsafe bytes
    assert isinstance(unsafe_bytes, bytes)
    assert getattr(unsafe_bytes, '__UNSAFE__', False) is True
