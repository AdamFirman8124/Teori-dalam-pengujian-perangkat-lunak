# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafe
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes
from ansible.utils.unsafe_proxy import AnsibleUnsafeText


def test_ansible_unsafe_text_encode_default():
    text = AnsibleUnsafeText(u"hello")
    result = text.encode()
    assert result == b"hello"
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, bytes)
    assert getattr(result, "__UNSAFE__", False) is True
    assert isinstance(result, AnsibleUnsafe)


def test_ansible_unsafe_text_encode_with_positional_args():
    text = AnsibleUnsafeText(u"h\xe9llo \u2603")
    result = text.encode("utf-8", "strict")
    assert result == u"h\xe9llo \u2603".encode("utf-8", "strict")
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, bytes)
    assert getattr(result, "__UNSAFE__", False) is True


def test_ansible_unsafe_text_encode_with_kwargs():
    text = AnsibleUnsafeText(u"h\xe9llo")
    result = text.encode(encoding="utf-8", errors="strict")
    assert result == u"h\xe9llo".encode(encoding="utf-8", errors="strict")
    assert isinstance(result, AnsibleUnsafeBytes)
    assert getattr(result, "__UNSAFE__", False) is True
    # original value unchanged and still unsafe
    assert text == u"h\xe9llo"
    assert isinstance(text, AnsibleUnsafeText)
    assert getattr(text, "__UNSAFE__", False) is True
