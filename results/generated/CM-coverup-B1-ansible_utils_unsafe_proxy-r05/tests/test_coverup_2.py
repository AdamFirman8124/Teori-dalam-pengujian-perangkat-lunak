# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest

from ansible.module_utils.six import text_type
from ansible.utils.unsafe_proxy import UnsafeProxy, AnsibleUnsafe, AnsibleUnsafeText, AnsibleUnsafeBytes


class _FakeDisplay(object):
    def __init__(self):
        self.calls = []

    def deprecated(self, msg, version=None, collection_name=None, **kwargs):
        self.calls.append({'msg': msg, 'version': version, 'collection_name': collection_name})


@pytest.fixture
def fake_display(monkeypatch):
    display = _FakeDisplay()
    monkeypatch.setattr('ansible.utils.display.Display', lambda: display)
    return display


def test_unsafe_proxy_string(fake_display):
    result = UnsafeProxy(u'some string')

    assert isinstance(result, AnsibleUnsafeText)
    assert not isinstance(result, bytes)
    assert result == u'some string'
    assert result.__UNSAFE__ is True
    assert len(fake_display.calls) == 1
    assert 'UnsafeProxy is being deprecated' in fake_display.calls[0]['msg']
    assert fake_display.calls[0]['version'] == '2.13'
    assert fake_display.calls[0]['collection_name'] == 'ansible.builtin'


def test_unsafe_proxy_bytes_passthrough(fake_display):
    obj = b'byte string'
    result = UnsafeProxy(obj)

    # on Python3 bytes is not in string_types, so returned unchanged
    assert result is obj
    assert type(result) is bytes
    assert not isinstance(result, AnsibleUnsafe)
    assert len(fake_display.calls) == 1


def test_unsafe_proxy_passthrough_already_unsafe_text(fake_display):
    already = AnsibleUnsafeText(u'already unsafe')
    result = UnsafeProxy(already)

    assert result is already
    assert isinstance(result, AnsibleUnsafe)
    assert len(fake_display.calls) == 1


def test_unsafe_proxy_passthrough_already_unsafe_bytes(fake_display):
    already = AnsibleUnsafeBytes(b'already unsafe')
    result = UnsafeProxy(already)

    assert result is already
    assert isinstance(result, AnsibleUnsafe)
    assert len(fake_display.calls) == 1


def test_unsafe_proxy_non_string_passthrough(fake_display):
    obj = {'key': 'value'}
    result = UnsafeProxy(obj)

    assert result is obj
    assert not isinstance(result, AnsibleUnsafe)
    assert len(fake_display.calls) == 1
