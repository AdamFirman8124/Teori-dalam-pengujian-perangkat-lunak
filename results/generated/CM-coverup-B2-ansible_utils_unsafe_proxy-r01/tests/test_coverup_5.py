# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafe
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes
from ansible.utils.unsafe_proxy import AnsibleUnsafeText


def test_ansible_unsafe_text_encode_default():
    text = AnsibleUnsafeText(u"hello world")
    result = text.encode()
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b"hello world"
    assert bytes(result) == b"hello world"


def test_ansible_unsafe_text_encode_positional_encoding():
    text = AnsibleUnsafeText(u"caf\u00e9")
    result = text.encode("utf-8")
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u"caf\u00e9".encode("utf-8")
    assert result == b"caf\xc3\xa9"


def test_ansible_unsafe_text_encode_kwargs():
    text = AnsibleUnsafeText(u"caf\u00e9")
    result = text.encode(encoding="utf-8", errors="strict")
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b"caf\xc3\xa9"
