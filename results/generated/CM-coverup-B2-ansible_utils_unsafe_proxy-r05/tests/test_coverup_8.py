# file: project/ansible/utils/unsafe_proxy.py:141-142
# asked: {"lines": [142], "branches": []}
# gained: {"lines": [142], "branches": []}

import ansible.utils.unsafe_proxy as unsafe_proxy


def test_to_unsafe_bytes_forwards_arguments_and_wraps_result(monkeypatch):
    calls = []

    def fake_to_bytes(*args, **kwargs):
        calls.append((args, kwargs))
        return b"converted"

    monkeypatch.setattr(unsafe_proxy, "to_bytes", fake_to_bytes)

    result = unsafe_proxy.to_unsafe_bytes(
        "value",
        encoding="utf-8",
        errors="strict",
    )

    assert calls == [
        (("value",), {"encoding": "utf-8", "errors": "strict"}),
    ]
    assert type(result) is unsafe_proxy.AnsibleUnsafeBytes
    assert result == b"converted"
    assert result.__UNSAFE__ is True
