# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, AnsibleUnsafeText


def test_ansible_unsafe_text_encode_preserves_unsafe_context():
    value = AnsibleUnsafeText("café")

    encoded = value.encode("utf-8", errors="strict")

    assert encoded == b"caf\xc3\xa9"
    assert type(encoded) is AnsibleUnsafeBytes
    assert value == "café"
