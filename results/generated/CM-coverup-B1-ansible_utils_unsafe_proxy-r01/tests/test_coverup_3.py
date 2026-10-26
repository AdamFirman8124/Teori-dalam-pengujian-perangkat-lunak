# file: project/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    _wrap_sequence,
)


@pytest.mark.parametrize("sequence_type", [list, tuple])
def test_wrap_sequence_preserves_type_and_wraps_each_item(sequence_type):
    original = sequence_type(["text", b"bytes"])

    wrapped = _wrap_sequence(original)

    assert type(wrapped) is sequence_type
    assert wrapped == original
    assert isinstance(wrapped[0], AnsibleUnsafeText)
    assert isinstance(wrapped[1], AnsibleUnsafeBytes)
    assert wrapped is not original
