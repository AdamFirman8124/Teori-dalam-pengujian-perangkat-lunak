# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeText, UnsafeProxy


@pytest.fixture
def fake_display(monkeypatch):
    calls = []

    class FakeDisplay:
        def deprecated(self, message, version=None, collection_name=None, *args, **kwargs):
            calls.append(
                {
                    "message": message,
                    "version": version,
                    "collection_name": collection_name,
                    "args": args,
                    "kwargs": kwargs,
                }
            )

    monkeypatch.setattr("ansible.utils.display.Display", FakeDisplay)
    return calls


def _assert_deprecated_called_once(calls):
    assert len(calls) == 1
    assert calls[0]["message"] == (
        "UnsafeProxy is being deprecated. Use wrap_var or "
        "AnsibleUnsafeBytes/AnsibleUnsafeText directly instead"
    )
    assert calls[0]["version"] == "2.13"
    assert calls[0]["collection_name"] == "ansible.builtin"


def test_unsafe_proxy_returns_existing_unsafe_text_unchanged(fake_display):
    obj = AnsibleUnsafeText("already unsafe")

    result = UnsafeProxy(obj)

    assert result is obj
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, AnsibleUnsafeText)
    assert result == "already unsafe"
    _assert_deprecated_called_once(fake_display)


def test_unsafe_proxy_returns_existing_unsafe_object_unchanged(fake_display):
    class CustomUnsafe(AnsibleUnsafe):
        pass

    obj = CustomUnsafe()

    result = UnsafeProxy(obj)

    assert result is obj
    assert isinstance(result, AnsibleUnsafe)
    _assert_deprecated_called_once(fake_display)


def test_unsafe_proxy_wraps_str_as_ansible_unsafe_text(fake_display):
    result = UnsafeProxy("hello")

    assert result == "hello"
    assert type(result) is AnsibleUnsafeText
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, str)
    _assert_deprecated_called_once(fake_display)


def test_unsafe_proxy_wraps_unicode_str_as_ansible_unsafe_text(fake_display):
    result = UnsafeProxy("héllo wörld")

    assert result == "héllo wörld"
    assert type(result) is AnsibleUnsafeText
    assert isinstance(result, AnsibleUnsafe)
    _assert_deprecated_called_once(fake_display)


def test_unsafe_proxy_wraps_empty_str_as_ansible_unsafe_text(fake_display):
    result = UnsafeProxy("")

    assert result == ""
    assert type(result) is AnsibleUnsafeText
    assert isinstance(result, AnsibleUnsafe)
    _assert_deprecated_called_once(fake_display)


@pytest.mark.parametrize(
    "obj",
    [
        42,
        3.14,
        True,
        None,
        b"bytes-are-not-string-types-on-py3",
        ["a", "b"],
        {"key": "value"},
        (1, 2),
        object(),
    ],
)
def test_unsafe_proxy_returns_non_string_non_unsafe_unchanged(fake_display, obj):
    # On Python 3, string_types == (str,), so bytes also take this branch.
    # The identity assertion verifies the final `return obj` path.
    if isinstance(obj, bytes):
        # Guard against Python 2 semantics where bytes are string_types;
        # in the supported Python 3 test environment this is identity.
        result = UnsafeProxy(obj)
        assert result == obj
    else:
        result = UnsafeProxy(obj)
        assert result is obj

    assert not isinstance(result, AnsibleUnsafeText) or isinstance(obj, AnsibleUnsafeText)
    _assert_deprecated_called_once(fake_display)


def test_unsafe_proxy_ignores_extra_args_and_kwargs(fake_display):
    result = UnsafeProxy("extra args", "ignored", flag=True)

    assert result == "extra args"
    assert type(result) is AnsibleUnsafeText
    assert isinstance(result, AnsibleUnsafe)
    _assert_deprecated_called_once(fake_display)


def test_unsafe_proxy_deprecated_called_for_each_invocation(fake_display):
    first = UnsafeProxy("one")
    second = UnsafeProxy(123)

    assert first == "one"
    assert type(first) is AnsibleUnsafeText
    assert second == 123
    assert second is not first
    assert len(fake_display) == 2
    for call in fake_display:
        assert call["version"] == "2.13"
        assert call["collection_name"] == "ansible.builtin"
