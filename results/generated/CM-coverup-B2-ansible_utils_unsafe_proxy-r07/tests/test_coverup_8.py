# file: project/ansible/utils/unsafe_proxy.py:141-142
# asked: {"lines": [142], "branches": []}
# gained: {"lines": [142], "branches": []}

import ansible.utils.unsafe_proxy as unsafe_proxy


def test_to_unsafe_bytes_converts_and_wraps_text():
    result = unsafe_proxy.to_unsafe_bytes("hello", encoding="utf-8")

    assert isinstance(result, unsafe_proxy.AnsibleUnsafeBytes)
    assert result == b"hello"


def test_to_unsafe_bytes_forwards_arguments_and_wraps_result(monkeypatch):
    calls = {}
    wrapped = object()

    def fake_to_bytes(*args, **kwargs):
        calls["to_bytes"] = (args, kwargs)
        return b"converted"

    def fake_wrap_var(value):
        calls["wrap_var"] = value
        return wrapped

    monkeypatch.setattr(unsafe_proxy, "to_bytes", fake_to_bytes)
    monkeypatch.setattr(unsafe_proxy, "wrap_var", fake_wrap_var)

    result = unsafe_proxy.to_unsafe_bytes(
        "value",
        encoding="utf-8",
        errors="strict",
    )

    assert result is wrapped
    assert calls["to_bytes"] == (
        ("value",),
        {"encoding": "utf-8", "errors": "strict"},
    )
    assert calls["wrap_var"] == b"converted"
