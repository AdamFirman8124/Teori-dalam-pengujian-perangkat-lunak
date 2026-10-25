# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest

from ansible.module_utils.six import text_type
from ansible.utils.unsafe_proxy import (
    UnsafeProxy,
    AnsibleUnsafe,
    AnsibleUnsafeText,
    AnsibleUnsafeBytes,
)


class _FakeDisplay(object):
    def __init__(self, *args, **kwargs):
        pass

    def deprecated(self, msg, version=None, collection_name=None):
        self.msg = msg
        self.version = version
        self.collection_name = collection_name


@pytest.fixture
def fake_display(monkeypatch):
    import ansible.utils.display as display_mod

    instance = _FakeDisplay()
    monkeypatch.setattr(display_mod, 'Display', lambda *a, **kw: instance)
    return instance


def test_unsafe_proxy_string(fake_display):
    """UnsafeProxy on a plain str wraps it in AnsibleUnsafeText and emits deprecation."""
    result = UnsafeProxy(u'some string')

    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, text_type)
    assert result == u'some string'
    assert result.__UNSAFE__ is True
    # deprecation was emitted
    assert 'UnsafeProxy is being deprecated' in fake_display.msg
    assert fake_display.version == '2.13'
    assert fake_display.collection_name == 'ansible.builtin'


def test_unsafe_proxy_bytes_passthrough(fake_display):
    """Bytes are not string_types, so they are returned unchanged (line 100 False branch)."""
    obj = b'byte string'
    result = UnsafeProxy(obj)

    assert result is obj
    assert isinstance(result, AnsibleUnsafeBytes) is False
    assert isinstance(result, AnsibleUnsafe) is False


def test_unsafe_proxy_passthrough_already_unsafe(fake_display):
    """An already-unsafe object is returned as-is (lines 97-98)."""
    already = AnsibleUnsafeText(u'already unsafe')
    result = UnsafeProxy(already)

    assert result is already
    assert isinstance(result, AnsibleUnsafe)


def test_unsafe_proxy_non_string_passthrough(fake_display):
    """Non-string objects are returned unchanged (line 100 False branch)."""
    obj = {'key': 'value'}
    result = UnsafeProxy(obj)

    assert result is obj
    assert not isinstance(result, AnsibleUnsafe)


def test_unsafe_proxy_none(fake_display):
    """None is returned unchanged."""
    result = UnsafeProxy(None)

    assert result is None
    assert not isinstance(result, AnsibleUnsafe)
