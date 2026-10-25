# file: project/ansible/utils/unsafe_proxy.py:141-142
# asked: {"lines": [142], "branches": []}
# gained: {"lines": [142], "branches": []}

import ansible.utils.unsafe_proxy as unsafe_proxy


def test_to_unsafe_bytes_converts_and_wraps_result(monkeypatch):
    converted = object()
    wrapped = object()
    to_bytes_calls = []
    wrap_var_calls = []

    def fake_to_bytes(*args, **kwargs):
        to_bytes_calls.append((args, kwargs))
        return converted

    def fake_wrap_var(value):
        wrap_var_calls.append(value)
        return wrapped

    monkeypatch.setattr(unsafe_proxy, "to_bytes", fake_to_bytes)
    monkeypatch.setattr(unsafe_proxy, "wrap_var", fake_wrap_var)

    result = unsafe_proxy.to_unsafe_bytes(
        "value",
        encoding="utf-8",
        errors="strict",
    )

    assert result is wrapped
    assert to_bytes_calls == [
        (("value",), {"encoding": "utf-8", "errors": "strict"})
    ]
    assert wrap_var_calls == [converted]
