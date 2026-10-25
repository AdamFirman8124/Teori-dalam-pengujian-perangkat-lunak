# file: project/ansible/utils/unsafe_proxy.py:145-146
# asked: {"lines": [146], "branches": []}
# gained: {"lines": [146], "branches": []}

import ansible.utils.unsafe_proxy as unsafe_proxy


def test_to_unsafe_text_converts_and_wraps_value(monkeypatch):
    converted_value = object()
    wrapped_value = object()
    received = {}

    def fake_to_text(*args, **kwargs):
        received["to_text"] = (args, kwargs)
        return converted_value

    def fake_wrap_var(value):
        received["wrap_var"] = value
        return wrapped_value

    monkeypatch.setattr(unsafe_proxy, "to_text", fake_to_text)
    monkeypatch.setattr(unsafe_proxy, "wrap_var", fake_wrap_var)

    result = unsafe_proxy.to_unsafe_text("value", errors="surrogate_or_strict")

    assert result is wrapped_value
    assert received["to_text"] == (
        ("value",),
        {"errors": "surrogate_or_strict"},
    )
    assert received["wrap_var"] is converted_value
