# file: project/ansible/utils/unsafe_proxy.py:145-146
# asked: {"lines": [146], "branches": []}
# gained: {"lines": [146], "branches": []}

from ansible.utils import unsafe_proxy


def test_to_unsafe_text_converts_and_wraps_value(monkeypatch):
    converted = object()
    wrapped = object()
    calls = []

    def fake_to_text(*args, **kwargs):
        calls.append(("to_text", args, kwargs))
        return converted

    def fake_wrap_var(value):
        calls.append(("wrap_var", value))
        return wrapped

    monkeypatch.setattr(unsafe_proxy, "to_text", fake_to_text)
    monkeypatch.setattr(unsafe_proxy, "wrap_var", fake_wrap_var)

    result = unsafe_proxy.to_unsafe_text(
        b"example",
        errors="surrogate_or_strict",
    )

    assert result is wrapped
    assert calls == [
        (
            "to_text",
            (b"example",),
            {"errors": "surrogate_or_strict"},
        ),
        ("wrap_var", converted),
    ]
