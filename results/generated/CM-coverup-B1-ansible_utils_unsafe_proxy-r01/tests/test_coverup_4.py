# file: project/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [73], "branches": []}
# gained: {"lines": [73], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText


def test_unsafe_bytes_decode_preserves_unsafe_context():
    value = AnsibleUnsafeBytes(b"hello")

    result = value.decode("utf-8")

    assert result == "hello"
    assert type(result) is AnsibleUnsafeText
    assert value == b"hello"


def test_unsafe_bytes_decode_forwards_keyword_arguments():
    value = AnsibleUnsafeBytes(b"\xff")

    result = value.decode(encoding="ascii", errors="replace")

    assert result == "\ufffd"
    assert type(result) is AnsibleUnsafeText
    assert value == b"\xff"
