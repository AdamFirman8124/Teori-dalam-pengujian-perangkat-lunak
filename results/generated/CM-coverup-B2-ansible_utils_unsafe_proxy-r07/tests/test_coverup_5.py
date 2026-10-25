# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes
from ansible.utils.unsafe_proxy import AnsibleUnsafeText


def test_encode_preserves_unsafe_bytes_type_with_positional_arguments():
    value = AnsibleUnsafeText("café")

    encoded = value.encode("utf-8")

    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert isinstance(encoded, bytes)
    assert encoded == b"caf\xc3\xa9"


def test_encode_preserves_unsafe_bytes_type_with_keyword_arguments():
    value = AnsibleUnsafeText("café")

    encoded = value.encode(encoding="ascii", errors="ignore")

    assert isinstance(encoded, AnsibleUnsafeBytes)
    assert isinstance(encoded, bytes)
    assert encoded == b"caf"
