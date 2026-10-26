# file: project/ansible/utils/unsafe_proxy.py:145-146
# asked: {"lines": [146], "branches": []}
# gained: {"lines": [146], "branches": []}

from ansible.utils.unsafe_proxy import AnsibleUnsafeText, to_unsafe_text


def test_to_unsafe_text_from_str():
    result = to_unsafe_text("hello")
    assert result == "hello"
    assert type(result) is AnsibleUnsafeText
    assert isinstance(result, str)
    assert getattr(result, "__UNSAFE__", False) is True


def test_to_unsafe_text_from_bytes():
    result = to_unsafe_text(b"hello")
    assert result == "hello"
    assert type(result) is AnsibleUnsafeText
    assert getattr(result, "__UNSAFE__", False) is True


def test_to_unsafe_text_forwards_encoding_kwarg():
    result = to_unsafe_text(b"caf\xc3\xa9", encoding="utf-8")
    assert result == "café"
    assert type(result) is AnsibleUnsafeText

    result_latin1 = to_unsafe_text(b"\xff", encoding="latin-1")
    assert result_latin1 == "ÿ"
    assert type(result_latin1) is AnsibleUnsafeText


def test_to_unsafe_text_forwards_errors_kwarg():
    result = to_unsafe_text(b"\xff", encoding="utf-8", errors="replace")
    assert result == "\ufffd"
    assert type(result) is AnsibleUnsafeText
    assert getattr(result, "__UNSAFE__", False) is True


def test_to_unsafe_text_empty_and_nonstring():
    empty = to_unsafe_text(b"")
    assert empty == ""
    assert type(empty) is AnsibleUnsafeText

    number = to_unsafe_text(123)
    assert number == "123"
    assert type(number) is AnsibleUnsafeText
    assert getattr(number, "__UNSAFE__", False) is True


def test_to_unsafe_text_delegates_to_wrap_var(monkeypatch):
    calls = []

    def fake_wrap_var(value):
        calls.append(value)
        return ("wrapped", value)

    monkeypatch.setattr(
        "ansible.utils.unsafe_proxy.wrap_var", fake_wrap_var
    )
    result = to_unsafe_text(b"hi", encoding="utf-8")
    assert result == ("wrapped", "hi")
    assert calls == ["hi"]
