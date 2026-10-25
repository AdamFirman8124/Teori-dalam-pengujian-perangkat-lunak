# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeBytes, AnsibleUnsafeText


def test_ansible_unsafe_text_encode_default():
    text = AnsibleUnsafeText(u'hello')
    result = text.encode()
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b'hello'
    assert bytes(result) == u'hello'.encode()


def test_ansible_unsafe_text_encode_with_positional_encoding():
    text = AnsibleUnsafeText(u'caf\xe9')
    result = text.encode('utf-8')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u'caf\xe9'.encode('utf-8')


def test_ansible_unsafe_text_encode_with_kwargs():
    text = AnsibleUnsafeText(u'caf\xe9')
    result = text.encode(encoding='utf-8', errors='strict')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u'caf\xe9'.encode(encoding='utf-8', errors='strict')


def test_ansible_unsafe_text_encode_errors_kwarg():
    text = AnsibleUnsafeText(u'caf\xe9')
    result = text.encode('ascii', 'ignore')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b'caf'
