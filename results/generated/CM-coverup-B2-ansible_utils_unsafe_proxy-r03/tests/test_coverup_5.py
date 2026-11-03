# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeBytes, AnsibleUnsafeText


def test_ansible_unsafe_text_encode_returns_unsafe_bytes():
    """Calling encode() on an AnsibleUnsafeText must execute line 79 and return
    an AnsibleUnsafeBytes instance that keeps the unsafe marker."""
    unsafe_text = AnsibleUnsafeText(u"hello world")

    result = unsafe_text.encode("utf-8")

    # Postconditions of line 79: the result is an unsafe bytes object holding
    # the expected encoded payload.
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, bytes)
    assert result == b"hello world"
    assert result.__UNSAFE__ is True
    assert AnsibleUnsafe.__UNSAFE__ is True


def test_ansible_unsafe_text_encode_forwards_kwargs():
    """encode() must forward keyword arguments to the underlying
    text_type.encode while preserving the unsafe context (line 79)."""
    unsafe_text = AnsibleUnsafeText(u"caf\u00e9")

    result = unsafe_text.encode(encoding="utf-8", errors="strict")

    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b"caf\xc3\xa9"
    assert result.__UNSAFE__ is True


def test_ansible_unsafe_text_encode_default_arguments():
    """encode() with no arguments must still wrap the result in
    AnsibleUnsafeBytes via line 79."""
    unsafe_text = AnsibleUnsafeText(u"abc")

    result = unsafe_text.encode()

    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b"abc"
    assert result.__UNSAFE__ is True
