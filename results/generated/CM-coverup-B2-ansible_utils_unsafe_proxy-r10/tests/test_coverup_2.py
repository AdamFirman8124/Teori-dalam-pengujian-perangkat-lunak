# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import sys
import types

import pytest

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    UnsafeProxy,
)

DEPRECATION_MSG = u'UnsafeProxy is being deprecated. Use wrap_var or AnsibleUnsafeBytes/AnsibleUnsafeText directly instead'


class _FakeDisplay(object):
    """Minimal stand-in for ansible.utils.display.Display that records deprecated() calls."""

    def __init__(self, *args, **kwargs):
        self.deprecated_calls = []

    def deprecated(self, msg, version=None, removed=False, collection_name=None, **kwargs):
        self.deprecated_calls.append({
            'msg': msg,
            'version': version,
            'removed': removed,
            'collection_name': collection_name,
        })


@pytest.fixture
def fake_display(monkeypatch):
    """Replace ansible.utils.display with a stub module so that the lazy
    ``from ansible.utils.display import Display`` inside UnsafeProxy.__new__
    picks up the fake instead of the real Display (no real output emitted,
    and the patch is fully reverted after each test)."""
    fake = _FakeDisplay()
    stub_module = types.ModuleType(u'ansible.utils.display')
    stub_module.Display = lambda *args, **kwargs: fake
    monkeypatch.setitem(sys.modules, u'ansible.utils.display', stub_module)
    return fake


def test_unsafe_proxy_wraps_text_and_deprecates(fake_display):
    """Lines 88-91, 100-102: a text string is wrapped in AnsibleUnsafeText
    and the deprecation warning is emitted exactly once with expected args."""
    result = UnsafeProxy(u'foo')

    assert type(result) is AnsibleUnsafeText
    assert result == u'foo'
    assert result.__UNSAFE__ is True
    assert fake_display.deprecated_calls == [{
        'msg': DEPRECATION_MSG,
        'version': u'2.13',
        'removed': False,
        'collection_name': u'ansible.builtin',
    }]


def test_unsafe_proxy_passes_bytes_through_unchanged(fake_display):
    """Lines 100-102: bytes are not an instance of string_types on py3, so
    they are returned unchanged instead of being wrapped in AnsibleUnsafeText."""
    result = UnsafeProxy(b'foo')

    assert result == b'foo'
    assert type(result) is bytes
    assert not isinstance(result, AnsibleUnsafe)
    assert len(fake_display.deprecated_calls) == 1


def test_unsafe_proxy_returns_existing_unsafe_text_unchanged(fake_display):
    """Lines 97-98: an already-unsafe object short-circuits and is returned as-is."""
    obj = AnsibleUnsafeText(u'foo')
    result = UnsafeProxy(obj)

    assert result is obj
    assert isinstance(result, AnsibleUnsafe)
    assert len(fake_display.deprecated_calls) == 1


def test_unsafe_proxy_returns_existing_unsafe_bytes_unchanged(fake_display):
    """Lines 97-98: unsafe bytes are returned as-is, not re-wrapped as text."""
    obj = AnsibleUnsafeBytes(b'foo')
    result = UnsafeProxy(obj)

    assert result is obj
    assert isinstance(result, AnsibleUnsafe)
    assert len(fake_display.deprecated_calls) == 1


def test_unsafe_proxy_passes_through_non_string_objects(fake_display):
    """Line 102: non-string, non-unsafe objects are returned unchanged."""
    passthrough_objects = [[u'foo'], {u'key': u'value'}, 42, None]

    for obj in passthrough_objects:
        result = UnsafeProxy(obj)
        assert result is obj
        assert not isinstance(result, AnsibleUnsafe)

    assert len(fake_display.deprecated_calls) == len(passthrough_objects)
