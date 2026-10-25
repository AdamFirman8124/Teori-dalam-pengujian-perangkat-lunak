# file: project/ansible/utils/unsafe_proxy.py:145-146
# asked: {"lines": [146], "branches": []}
# gained: {"lines": [146], "branches": []}

import ansible.utils.unsafe_proxy as unsafe_proxy


def test_to_unsafe_text_converts_and_wraps_bytes():
    result = unsafe_proxy.to_unsafe_text(
        b"caf\xe9",
        encoding="latin-1",
        errors="strict",
    )

    assert result == "café"
    assert isinstance(result, unsafe_proxy.AnsibleUnsafeText)


def test_to_unsafe_text_forwards_arguments_and_wraps_result(monkeypatch):
    converted = object()
    wrapped = object()
    calls = {}

    def fake_to_text(*args, **kwargs):
        calls["to_text"] = (args, kwargs)
        return converted

    def fake_wrap_var(value):
        calls["wrap_var"] = value
        return wrapped

    monkeypatch.setattr(unsafe_proxy, "to_text", fake_to_text)
    monkeypatch.setattr(unsafe_proxy, "wrap_var", fake_wrap_var)

    result = unsafe_proxy.to_unsafe_text(
        b"value",
        encoding="ascii",
        errors="strict",
        nonstring="passthru",
    )

    assert result is wrapped
    assert calls["to_text"] == (
        (b"value",),
        {
            "encoding": "ascii",
            "errors": "strict",
            "nonstring": "passthru",
        },
    )
    assert calls["wrap_var"] is converted
