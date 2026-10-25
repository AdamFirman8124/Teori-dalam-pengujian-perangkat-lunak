# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeBytes, AnsibleUnsafeText


def test_ansible_unsafe_text_encode_default():
    text = AnsibleUnsafeText("hello")
    result = text.encode()

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, bytes)
    assert isinstance(result, AnsibleUnsafe)
    assert getattr(result, "__UNSAFE__", False) is True
    assert result == b"hello"


def test_ansible_unsafe_text_encode_with_encoding_arg():
    text = AnsibleUnsafeText("héllo")
    result = text.encode("utf-8")

    assert isinstance(result, AnsibleUnsafeBytes)
    assert getattr(result, "__UNSAFE__", False) is True
    assert result == "héllo".encode("utf-8")
    assert result.decode("utf-8") == "héllo"


def test_ansible_unsafe_text_encode_with_kwargs():
    text = AnsibleUnsafeText("héllo")
    result = text.encode(encoding="utf-16", errors="strict")

    assert isinstance(result, AnsibleUnsafeBytes)
    assert getattr(result, "__UNSAFE__", False) is True
    assert result == "héllo".encode(encoding="utf-16", errors="strict")


@pytest.mark.parametrize(
    "value,encoding,expected",
    [
        ("", "utf-8", b""),
        ("abc", "ascii", b"abc"),
        ("café", "latin-1", "café".encode("latin-1")),
    ],
)
def test_ansible_unsafe_text_encode_parametrized(value, encoding, expected):
    result = AnsibleUnsafeText(value).encode(encoding)

    assert isinstance(result, AnsibleUnsafeBytes)
    assert getattr(result, "__UNSAFE__", False) is True
    assert result == expected
