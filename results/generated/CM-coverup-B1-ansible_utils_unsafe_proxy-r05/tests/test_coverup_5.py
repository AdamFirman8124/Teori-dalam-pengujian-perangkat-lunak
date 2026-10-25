# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText


def test_ansible_unsafe_text_encode_returns_unsafe_bytes():
    value = AnsibleUnsafeText("unsafe text")

    result = value.encode("utf-8")

    assert type(result) is AnsibleUnsafeBytes
    assert result == b"unsafe text"
    assert result.__UNSAFE__ is True


def test_ansible_unsafe_text_encode_forwards_keyword_arguments():
    value = AnsibleUnsafeText("caf\u00e9")

    result = value.encode(encoding="ascii", errors="replace")

    assert type(result) is AnsibleUnsafeBytes
    assert result == b"caf?"
    assert result.__UNSAFE__ is True
