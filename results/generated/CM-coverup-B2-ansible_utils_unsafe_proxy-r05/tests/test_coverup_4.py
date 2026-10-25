# file: project/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [73], "branches": []}
# gained: {"lines": [73], "branches": []}

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
)


def test_ansible_unsafe_bytes_decode_preserves_unsafe_context():
    result = AnsibleUnsafeBytes(b"\xc3\xa9").decode("utf-8")

    assert result == "\u00e9"
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)


def test_ansible_unsafe_bytes_decode_accepts_keyword_arguments():
    result = AnsibleUnsafeBytes(b"\xff").decode(
        encoding="ascii",
        errors="replace",
    )

    assert result == "\ufffd"
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
